#!/usr/bin/env python3
"""Verify the complete exterior-square scan needed at clique cutoff six."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from exact_invariants import (
    exact_chromatic_number,
    maximum_clique,
    verify_clique,
    verify_coloring,
)


def parse_export(path: Path):
    metadata = {}
    data_lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            metadata[key] = value
        elif line:
            data_lines.append(line)
    return metadata, list(csv.DictReader(data_lines, delimiter="\t"))


def parse_adjacency(raw: str, count: int):
    rows = raw.split(",")
    if len(rows) != count:
        raise ValueError("wrong adjacency-mask count")
    adjacency = tuple(int(row) for row in rows)
    allowed = (1 << count) - 1
    for source, mask in enumerate(adjacency):
        if mask < 0 or mask & ~allowed or mask & (1 << source):
            raise ValueError("invalid adjacency mask")
        for target in range(count):
            if bool(mask & (1 << target)) != bool(adjacency[target] & (1 << source)):
                raise ValueError("adjacency is not symmetric")
    return adjacency


def parse_vertices(raw: str):
    return tuple(int(value) - 1 for value in raw.split(",") if value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--c2-5-certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()

    raw = args.input.read_bytes()
    gap_raw = args.gap_script.read_bytes()
    c2_raw = args.c2_5_certificate.read_bytes()
    c2_document = json.loads(c2_raw)
    metadata, source_rows = parse_export(args.input)
    cutoff = int(metadata["CLIQUE_CUTOFF"])
    status_distribution = Counter()
    eligible_distribution = Counter()
    unique_faithful_graphs = set()
    quotient_kernel_counts = {}
    quotient_serials = defaultdict(set)
    quotient_summaries = {}
    candidate_records = []
    failures = []
    special_rows = []

    for row_number, row in enumerate(source_rows, 1):
        q_order = int(row["q_order"])
        q_id = int(row["q_id"])
        status = row["status"]
        status_distribution[status] += 1
        key = (q_order, q_id)
        if key not in quotient_summaries:
            quotient_summaries[key] = {
                "q_order": q_order,
                "q_id": q_id,
                "structure": row["structure"],
                "cover_order": int(row["cover_order"]),
                "exterior_order": int(row["exterior_order"]),
                "all_exterior_subgroups": int(row["all_exterior_subgroups"]),
                "normal_kernel_count": int(row["normal_kernel_count"]),
                "status_counts": Counter(),
            }
        summary = quotient_summaries[key]
        if (
            summary["normal_kernel_count"] != int(row["normal_kernel_count"])
            or summary["all_exterior_subgroups"] != int(row["all_exterior_subgroups"])
        ):
            raise ValueError("inconsistent quotient subgroup metadata")
        summary["status_counts"][status] += 1

        if status == "special_c2_5":
            if key != (32, 51) or row["adjacency"] or row["witness"]:
                raise ValueError("malformed special C2^5 row")
            special_rows.append(row_number)
            continue

        kernel_count = int(row["normal_kernel_count"])
        kernel_serial = int(row["kernel_serial"])
        if not 1 <= kernel_serial <= kernel_count:
            raise ValueError("invalid kernel serial")
        quotient_kernel_counts[key] = kernel_count
        quotient_serials[key].add(kernel_serial)
        adjacency = parse_adjacency(row["adjacency"], q_order)
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0)
        if int(row["radical_count"]) != len(radical):
            raise ValueError("radical count does not match adjacency")

        if status == "nonfaithful_radical":
            if len(radical) <= 1 or parse_vertices(row["witness"]) != radical:
                raise ValueError("invalid nonfaithful-radical certificate")
            continue

        if len(radical) != 1:
            raise ValueError("a retained faithful graph has the wrong radical")
        unique_faithful_graphs.add(adjacency)
        if status == "clique_ge_7":
            clique = parse_vertices(row["witness"])
            if len(clique) != cutoff + 1 or not verify_clique(adjacency, clique):
                raise ValueError("invalid clique exclusion witness")
            continue
        if status != "candidate" or row["witness"]:
            raise ValueError("unknown or malformed scan status")

        clique = maximum_clique(adjacency)
        coloring = exact_chromatic_number(adjacency, clique.size)
        if not verify_clique(adjacency, clique.vertices):
            raise AssertionError("candidate clique witness failed")
        if not verify_coloring(adjacency, coloring.colors):
            raise AssertionError("candidate coloring witness failed")
        pair = (clique.size, coloring.size)
        eligible_distribution[pair] += 1
        if clique.size > cutoff or coloring.size > cutoff:
            failures.append(row_number)
        candidate_records.append(
            {
                "row_number": row_number,
                "q_order": q_order,
                "q_id": q_id,
                "kernel_serial": kernel_serial,
                "kernel_order": int(row["kernel_order"]),
                "kernel_index": int(row["kernel_index"]),
                "nu": clique.size,
                "a": coloring.size,
                "clique_certificate": list(clique.vertices),
                "coloring_certificate": list(coloring.colors),
                "clique_search_nodes": clique.search_nodes,
                "coloring_search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
            }
        )

    if special_rows != [next(
        index for index, row in enumerate(source_rows, 1)
        if int(row["q_order"]) == 32 and int(row["q_id"]) == 51
    )]:
        raise ValueError("expected exactly one C2^5 special row")
    if len(quotient_summaries) != 162:
        raise ValueError("wrong quotient count")
    for key, count in quotient_kernel_counts.items():
        if quotient_serials[key] != set(range(1, count + 1)):
            raise ValueError("normal-kernel serial range is incomplete")
    if sum(quotient_kernel_counts.values()) != len(source_rows) - 1:
        raise ValueError("normal-kernel row total is incomplete")

    c2_independent = c2_document["independent_python_certificate"]
    if (
        c2_independent["pencil_count"] != 174251
        or c2_independent["common_radical_zero_pencil_count"] != 156240
        or min(record["omega"] for record in c2_independent["pencil_orbits"]) < 9
        or c2_independent["rank_two_radical_zero_orbit"]["omega"] < 9
    ):
        raise ValueError("C2^5 exception certificate is insufficient")

    quotient_records = []
    for key in sorted(quotient_summaries):
        summary = quotient_summaries[key]
        summary["status_counts"] = dict(sorted(summary["status_counts"].items()))
        quotient_records.append(summary)
    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input": str(args.input),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "gap_script": str(args.gap_script),
        "gap_script_sha256": hashlib.sha256(gap_raw).hexdigest(),
        "c2_5_certificate": str(args.c2_5_certificate),
        "c2_5_certificate_sha256": hashlib.sha256(c2_raw).hexdigest(),
        "gap_metadata": metadata,
        "clique_cutoff": cutoff,
        "quotient_count": len(quotient_summaries),
        "gap_scanned_quotient_count": len(quotient_kernel_counts),
        "normal_kernel_record_count": len(source_rows) - 1,
        "status_distribution": dict(sorted(status_distribution.items())),
        "unique_faithful_graph_count": len(unique_faithful_graphs),
        "eligible_distribution": [
            {"nu": pair[0], "a": pair[1], "count": count}
            for pair, count in sorted(eligible_distribution.items())
        ],
        "eligible_failure_rows": failures,
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "quotients": quotient_records,
        "candidate_records": candidate_records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "quotients=%d gap_scanned=%d normal_kernels=%d"
        % (len(quotient_summaries), len(quotient_kernel_counts), len(source_rows) - 1),
        "statuses=%r" % sorted(status_distribution.items()),
        "faithful_unique_graphs=%d candidates=%d"
        % (len(unique_faithful_graphs), len(candidate_records)),
        "eligible=%r" % sorted(eligible_distribution.items()),
        "eligible_failures=%r" % failures,
        "largest_kernel_counts=%r"
        % sorted(
            ((record["normal_kernel_count"], record["q_order"], record["q_id"], record["structure"])
             for record in quotient_records if (record["q_order"], record["q_id"]) != (32, 51)),
            reverse=True,
        )[:12],
        "wrote exact certificates to %s" % args.output,
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.parent.mkdir(parents=True, exist_ok=True)
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
