#!/usr/bin/env python3
"""Exact certificate analysis for the Schur-cover/exterior-square scan."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from collections import Counter
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
    rows = raw.split(";")
    if len(rows) != count:
        raise ValueError("wrong adjacency-row count")
    adjacency = []
    for source, row in enumerate(rows):
        mask = 0
        if row:
            for value in row.split(","):
                target = int(value) - 1
                if not 0 <= target < count or target == source:
                    raise ValueError("invalid adjacency entry")
                mask |= 1 << target
        adjacency.append(mask)
    for source, mask in enumerate(adjacency):
        for target in range(count):
            if bool(mask & (1 << target)) != bool(adjacency[target] & (1 << source)):
                raise ValueError("adjacency is not symmetric")
    return tuple(adjacency)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    parser.add_argument("--clique-cutoff", type=int, default=5)
    args = parser.parse_args()

    raw = args.input.read_bytes()
    gap_raw = args.gap_script.read_bytes()
    metadata, source_rows = parse_export(args.input)
    records = []
    distribution = Counter()
    eligible_distribution = Counter()
    unique_graphs = set()
    failures = []
    quotient_kernel_counts = {}
    for row_number, row in enumerate(source_rows, 1):
        q_order = int(row["q_order"])
        graph = parse_adjacency(row["adjacency"], q_order)
        clique = maximum_clique(graph)
        coloring = exact_chromatic_number(graph, clique.size)
        if not verify_clique(graph, clique.vertices):
            raise AssertionError("clique certificate failed")
        if not verify_coloring(graph, coloring.colors):
            raise AssertionError("coloring certificate failed")
        pair = (clique.size, coloring.size)
        distribution[pair] += 1
        unique_graphs.add(graph)
        quotient_key = (q_order, int(row["q_id"]))
        kernel_count = int(row["normal_kernel_count"])
        if quotient_key in quotient_kernel_counts:
            if quotient_kernel_counts[quotient_key] != kernel_count:
                raise ValueError("inconsistent normal-kernel count")
        else:
            quotient_kernel_counts[quotient_key] = kernel_count
        if not 1 <= int(row["kernel_serial"]) <= kernel_count:
            raise ValueError("invalid kernel serial")
        if clique.size <= args.clique_cutoff:
            eligible_distribution[pair] += 1
            if coloring.size > args.clique_cutoff:
                failures.append(row_number)
        records.append(
            {
                "status": "[COMPUTED]",
                "row_number": row_number,
                "q_order": q_order,
                "q_id": int(row["q_id"]),
                "structure": row["structure"],
                "cover_order": int(row["cover_order"]),
                "exterior_order": int(row["exterior_order"]),
                "all_exterior_subgroups": int(row["all_exterior_subgroups"]),
                "normal_kernel_count": kernel_count,
                "kernel_serial": int(row["kernel_serial"]),
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

    if sum(quotient_kernel_counts.values()) != len(source_rows):
        raise ValueError("kernel serial ranges do not exhaust exported rows")
    expected_serials = {
        key: set(range(1, count + 1)) for key, count in quotient_kernel_counts.items()
    }
    for record in records:
        expected_serials[(record["q_order"], record["q_id"])].discard(record["kernel_serial"])
    if any(expected_serials.values()):
        raise ValueError("a normal-kernel serial is missing")

    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input": str(args.input),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "gap_script": str(args.gap_script),
        "gap_script_sha256": hashlib.sha256(gap_raw).hexdigest(),
        "gap_metadata": metadata,
        "clique_cutoff": args.clique_cutoff,
        "quotient_count": len(quotient_kernel_counts),
        "record_count": len(records),
        "unique_graph_count": len(unique_graphs),
        "distribution": [
            {"nu": pair[0], "a": pair[1], "count": count}
            for pair, count in sorted(distribution.items())
        ],
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
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "records=%d unique_graphs=%d quotients=%d"
        % (len(records), len(unique_graphs), len(quotient_kernel_counts)),
        "distribution=%r" % sorted(distribution.items()),
        "eligible=%r" % sorted(eligible_distribution.items()),
        "eligible_failures=%r" % failures,
        "wrote exact certificates to %s" % args.output,
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.parent.mkdir(parents=True, exist_ok=True)
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
