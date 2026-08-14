#!/usr/bin/env python3
"""Verify a bounded cutoff-seven chosen-Schur-cover kernel batch."""

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
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            metadata[key] = value
        elif line:
            lines.append(line)
    return metadata, list(csv.DictReader(lines, delimiter="\t"))


def parse_adjacency(raw: str, order: int):
    adjacency = tuple(int(mask) for mask in raw.split(","))
    if len(adjacency) != order:
        raise ValueError("wrong adjacency length")
    allowed = (1 << order) - 1
    for source, mask in enumerate(adjacency):
        if mask < 0 or mask & ~allowed or mask & (1 << source):
            raise ValueError("invalid adjacency mask")
        for target in range(order):
            if bool(mask & (1 << target)) != bool(adjacency[target] & (1 << source)):
                raise ValueError("asymmetric adjacency")
    return adjacency


def parse_vertices(raw: str):
    return tuple(int(value) - 1 for value in raw.split(",") if value)


def _resolve(path: str, root: Path) -> Path:
    result = Path(path)
    return result if result.is_absolute() else root / result


def verify_saved_batch(document_path: Path, repository: Path | None = None):
    """Reparse and verify every stored row and witness in a saved batch.

    This verifier deliberately does not trust the JSON aggregates.  It checks
    all file hashes, quotient and kernel serial completeness, adjacency masks,
    radicals, eight-cliques, and saved exact candidate witnesses afresh.
    """

    root = repository or Path.cwd()
    document = json.loads(document_path.read_text(encoding="utf-8"))
    for field in ("input", "gap_script", "inventory", "gap_stdout"):
        path = _resolve(document[field], root)
        if hashlib.sha256(path.read_bytes()).hexdigest() != document[field + "_sha256"]:
            raise AssertionError("saved batch input hash mismatch: " + field)
    for delegated in document.get("delegated_certificates", []):
        path = _resolve(delegated["path"], root)
        if hashlib.sha256(path.read_bytes()).hexdigest() != delegated["sha256"]:
            raise AssertionError("delegated certificate hash mismatch")

    metadata, rows = parse_export(_resolve(document["input"], root))
    if metadata != document["metadata"]:
        raise AssertionError("saved metadata disagrees with TSV")
    inventory_document = json.loads(_resolve(document["inventory"], root).read_text(encoding="utf-8"))
    inventory_tsv = _resolve(inventory_document["inventory"], root)
    if hashlib.sha256(inventory_tsv.read_bytes()).hexdigest() != inventory_document["inventory_sha256"]:
        raise AssertionError("inventory source hash mismatch")
    _, inventory_rows = parse_export(inventory_tsv)
    complete_inventory = {
        (int(row["q_order"]), int(row["q_id"])): row for row in inventory_rows
    }
    start_order = int(metadata["START_Q_ORDER"])
    end_order = int(metadata["END_Q_ORDER"])
    end_id = int(metadata["END_Q_ID"]) if "END_Q_ID" in metadata else None
    start_id = int(metadata["START_Q_ID"])
    expected_quotients = {
        key for key in complete_inventory
        if start_order <= key[0] <= end_order
        and (key[0] != start_order or key[1] >= start_id)
        and (end_id is None or key[0] != end_order or key[1] <= end_id)
    }
    excluded = {tuple(pair) for pair in document["excluded_quotients"]}
    delegated_pairs = [
        tuple(record["small_group"])
        for record in document.get("delegated_certificates", [])
    ]
    if len(delegated_pairs) != len(set(delegated_pairs)) or not set(delegated_pairs) <= excluded:
        raise AssertionError("invalid delegated certificate identities")
    encoded_excluded = {
        tuple(map(int, pair.split(",")))
        for pair in metadata["EXCLUDED_QUOTIENTS"].split(";") if pair
    }
    if encoded_excluded != excluded:
        raise AssertionError("excluded quotient metadata mismatch")
    expected_excluded_records = [
        {
            "q_order": key[0],
            "q_id": key[1],
            "structure": complete_inventory[key]["structure"],
            "exterior_order": int(complete_inventory[key]["exterior_order"]),
            "status": "delegated_outside_this_batch",
        }
        for key in sorted(excluded)
    ]
    if document.get("excluded_records") != expected_excluded_records:
        raise AssertionError("saved excluded-record inventory mismatch")

    quotient_counts = {}
    serials = defaultdict(set)
    statuses = Counter()
    unique_faithful = set()
    excluded_rows = []
    candidates_by_row = {
        record["row_number"]: record for record in document["candidate_records"]
    }
    exact_distribution = Counter()
    failures = []
    for row_number, row in enumerate(rows, 1):
        key = (int(row["q_order"]), int(row["q_id"]))
        if key not in expected_quotients:
            raise AssertionError("out-of-range quotient in saved batch")
        if row["structure"] != complete_inventory[key]["structure"]:
            raise AssertionError("saved quotient structure disagrees with inventory")
        if row["status"] == "excluded_orbit_case":
            if key not in excluded:
                raise AssertionError("undeclared saved exclusion")
            if any(row[field] not in ("", "0") for field in (
                "cover_order", "exterior_order", "all_exterior_subgroups",
                "normal_kernel_count", "kernel_serial", "kernel_order",
                "kernel_index", "radical_count", "witness", "adjacency",
            )):
                raise AssertionError("malformed saved exclusion row")
            excluded_rows.append(key)
            continue
        count = int(row["normal_kernel_count"])
        serial = int(row["kernel_serial"])
        if key in quotient_counts and quotient_counts[key] != count:
            raise AssertionError("inconsistent saved kernel count")
        quotient_counts[key] = count
        serials[key].add(serial)
        if not 1 <= serial <= count:
            raise AssertionError("invalid saved kernel serial")
        if int(row["exterior_order"]) != int(complete_inventory[key]["exterior_order"]):
            raise AssertionError("saved exterior order disagrees with inventory")
        adjacency = parse_adjacency(row["adjacency"], key[0])
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0)
        if int(row["radical_count"]) != len(radical):
            raise AssertionError("saved radical count disagrees")
        status = row["status"]
        statuses[status] += 1
        witness = parse_vertices(row["witness"])
        if status == "nonfaithful_radical":
            if len(radical) <= 1 or witness != radical:
                raise AssertionError("invalid saved radical witness")
            continue
        if radical != (0,):
            raise AssertionError("saved faithful graph has wrong radical")
        unique_faithful.add(adjacency)
        if status == "clique_ge_8":
            if len(witness) != 8 or not verify_clique(adjacency, witness):
                raise AssertionError("invalid saved 8-clique")
            continue
        if status != "candidate" or witness:
            raise AssertionError("unknown saved status")
        record = candidates_by_row.get(row_number)
        if record is None:
            raise AssertionError("saved candidate lacks exact record")
        if (record["q_order"], record["q_id"], record["kernel_serial"]) != (
            key[0], key[1], serial
        ):
            raise AssertionError("saved candidate identity mismatch")
        clique = tuple(record["clique_certificate"])
        colors = tuple(record["coloring_certificate"])
        if not verify_clique(adjacency, clique) or not verify_coloring(adjacency, colors):
            raise AssertionError("invalid saved exact candidate witness")
        if (len(clique), max(colors, default=-1) + 1) != (record["nu"], record["a"]):
            raise AssertionError("saved exact invariant disagrees with witness")
        pair = (record["nu"], record["a"])
        exact_distribution[pair] += 1
        if record["nu"] > 7 or record["a"] > 10:
            failures.append(row_number)

    if set(excluded_rows) != excluded or len(excluded_rows) != len(excluded):
        raise AssertionError("saved exclusion rows are incomplete")
    if set(quotient_counts) != expected_quotients - excluded:
        raise AssertionError("saved quotient range is incomplete")
    if any(serials[key] != set(range(1, count + 1)) for key, count in quotient_counts.items()):
        raise AssertionError("saved kernel serials are incomplete")
    expected_statuses = dict(sorted(statuses.items()))
    expected_distribution = [
        {"nu": pair[0], "a": pair[1], "count": count}
        for pair, count in sorted(exact_distribution.items())
    ]
    comparisons = {
        "quotient_row_count": len(expected_quotients),
        "scanned_quotient_count": len(quotient_counts),
        "kernel_record_count": len(rows) - len(excluded_rows),
        "status_distribution": expected_statuses,
        "unique_faithful_graph_count": len(unique_faithful),
        "exact_candidate_distribution": expected_distribution,
        "failure_rows": failures,
    }
    for field, expected in comparisons.items():
        if document[field] != expected:
            raise AssertionError("saved JSON aggregate mismatch: " + field)
    expected_quotient_records = [
        {
            "q_order": key[0], "q_id": key[1],
            "structure": complete_inventory[key]["structure"],
            "exterior_order": int(complete_inventory[key]["exterior_order"]),
            "normal_kernel_count": quotient_counts[key],
        }
        for key in sorted(quotient_counts)
    ]
    if document["quotients"] != expected_quotient_records:
        raise AssertionError("saved per-quotient summary mismatch")
    if set(candidates_by_row) != {
        row_number for row_number, row in enumerate(rows, 1) if row["status"] == "candidate"
    }:
        raise AssertionError("saved candidate record rows are incomplete")
    return comparisons


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--gap-stdout", type=Path, required=True)
    parser.add_argument("--start-order", type=int, required=True)
    parser.add_argument("--start-id", type=int, default=1)
    parser.add_argument("--end-order", type=int, required=True)
    parser.add_argument("--end-id", type=int)
    parser.add_argument(
        "--excluded", action="append", default=[],
        help="explicit SmallGroup pair ORDER,ID delegated to another certificate",
    )
    parser.add_argument(
        "--delegated-certificate", action="append", default=[],
        help="delegated certificate in ORDER,ID=PATH form",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    metadata, rows = parse_export(args.input)
    excluded = {
        tuple(int(value) for value in raw_pair.split(","))
        for raw_pair in args.excluded
    }
    delegated_certificates = []
    for specification in args.delegated_certificate:
        raw_pair, raw_path = specification.split("=", 1)
        pair = tuple(int(value) for value in raw_pair.split(","))
        if pair not in excluded:
            raise ValueError("delegated certificate is not an excluded quotient")
        path = Path(raw_path)
        delegated_certificates.append({
            "small_group": list(pair),
            "path": str(path),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    expected_metadata = {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "START_Q_ORDER": str(args.start_order),
        "START_Q_ID": str(args.start_id),
        "END_Q_ORDER": str(args.end_order),
        "CLIQUE_CUTOFF": "7",
        "EXCLUDED_QUOTIENTS": ";".join(
            "%d,%d" % pair for pair in sorted(excluded)
        ),
    }
    if args.end_id is not None:
        expected_metadata["END_Q_ID"] = str(args.end_id)
    if metadata != expected_metadata:
        raise AssertionError("unexpected batch metadata")
    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    # The inventory JSON intentionally stores only the 30 largest records, so
    # the complete cross-check below reads its checksummed canonical TSV.
    inventory_tsv = Path(inventory["inventory"])
    if not inventory_tsv.is_absolute():
        inventory_tsv = Path.cwd() / inventory_tsv
    if hashlib.sha256(inventory_tsv.read_bytes()).hexdigest() != inventory["inventory_sha256"]:
        raise AssertionError("inventory source hash mismatch")
    _, all_inventory_rows = parse_export(inventory_tsv)
    complete_inventory = {
        (int(row["q_order"]), int(row["q_id"])): row for row in all_inventory_rows
    }

    expected_quotients = {
        key for key in complete_inventory
        if args.start_order <= key[0] <= args.end_order
        and (key[0] != args.start_order or key[1] >= args.start_id)
        and (args.end_id is None or key[0] != args.end_order or key[1] <= args.end_id)
    }
    quotient_counts = {}
    serials = defaultdict(set)
    status_counts = Counter()
    unique_faithful = set()
    candidate_records = []
    exact_distribution = Counter()
    failures = []
    excluded_rows = []
    for row_number, row in enumerate(rows, 1):
        key = (int(row["q_order"]), int(row["q_id"]))
        if key not in expected_quotients:
            raise AssertionError("out-of-range quotient")
        if row["structure"] != complete_inventory[key]["structure"]:
            raise AssertionError("quotient structure disagrees with inventory")
        if row["status"] == "excluded_orbit_case":
            if key not in excluded:
                raise AssertionError("undeclared excluded quotient")
            if any(row[field] not in ("", "0") for field in (
                "cover_order", "exterior_order", "all_exterior_subgroups",
                "normal_kernel_count", "kernel_serial", "kernel_order",
                "kernel_index", "radical_count", "witness", "adjacency",
            )):
                raise AssertionError("malformed excluded quotient row")
            excluded_rows.append(key)
            continue
        kernel_count = int(row["normal_kernel_count"])
        serial = int(row["kernel_serial"])
        if key in quotient_counts and quotient_counts[key] != kernel_count:
            raise AssertionError("inconsistent kernel count")
        quotient_counts[key] = kernel_count
        serials[key].add(serial)
        if not 1 <= serial <= kernel_count:
            raise AssertionError("invalid kernel serial")
        if int(row["exterior_order"]) != int(complete_inventory[key]["exterior_order"]):
            raise AssertionError("exterior order disagrees with multiplier census")
        adjacency = parse_adjacency(row["adjacency"], key[0])
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0)
        if int(row["radical_count"]) != len(radical):
            raise AssertionError("radical count disagrees")
        status = row["status"]
        status_counts[status] += 1
        witness = parse_vertices(row["witness"])
        if status == "nonfaithful_radical":
            if len(radical) <= 1 or witness != radical:
                raise AssertionError("invalid radical witness")
            continue
        if radical != (0,):
            raise AssertionError("faithful graph has wrong radical")
        unique_faithful.add(adjacency)
        if status == "clique_ge_8":
            if len(witness) != 8 or not verify_clique(adjacency, witness):
                raise AssertionError("invalid 8-clique witness")
            continue
        if status != "candidate" or witness:
            raise AssertionError("unknown candidate status")
        clique = maximum_clique(adjacency)
        coloring = exact_chromatic_number(adjacency, clique.size)
        if not verify_clique(adjacency, clique.vertices):
            raise AssertionError("exact clique failed")
        if not verify_coloring(adjacency, coloring.colors):
            raise AssertionError("exact coloring failed")
        pair = (clique.size, coloring.size)
        exact_distribution[pair] += 1
        if clique.size > 7 or coloring.size > 10:
            failures.append(row_number)
        candidate_records.append({
            "row_number": row_number,
            "q_order": key[0],
            "q_id": key[1],
            "kernel_serial": serial,
            "kernel_order": int(row["kernel_order"]),
            "kernel_index": int(row["kernel_index"]),
            "nu": clique.size,
            "a": coloring.size,
            "clique_certificate": list(clique.vertices),
            "coloring_certificate": list(coloring.colors),
            "clique_search_nodes": clique.search_nodes,
            "coloring_search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
        })

    if set(excluded_rows) != excluded or len(excluded_rows) != len(excluded):
        raise AssertionError("explicit exclusion rows are incomplete")
    if set(quotient_counts) != expected_quotients - excluded:
        raise AssertionError("incomplete quotient range")
    for key, count in quotient_counts.items():
        if serials[key] != set(range(1, count + 1)):
            raise AssertionError("incomplete normal-kernel serial range")
    if sum(quotient_counts.values()) + len(excluded_rows) != len(rows):
        raise AssertionError("wrong kernel-row total")
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact bounded batch; no global h(7) upper bound claimed",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input": str(args.input),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "gap_script": str(args.gap_script),
        "gap_script_sha256": hashlib.sha256(args.gap_script.read_bytes()).hexdigest(),
        "inventory": str(args.inventory),
        "inventory_sha256": hashlib.sha256(args.inventory.read_bytes()).hexdigest(),
        "gap_stdout": str(args.gap_stdout),
        "gap_stdout_sha256": hashlib.sha256(args.gap_stdout.read_bytes()).hexdigest(),
        "metadata": metadata,
        "quotient_row_count": len(expected_quotients),
        "scanned_quotient_count": len(quotient_counts),
        "excluded_quotients": [list(key) for key in sorted(excluded)],
        "excluded_records": [
            {
                "q_order": key[0],
                "q_id": key[1],
                "structure": complete_inventory[key]["structure"],
                "exterior_order": int(complete_inventory[key]["exterior_order"]),
                "status": "delegated_outside_this_batch",
            }
            for key in sorted(excluded)
        ],
        "delegated_certificates": sorted(
            delegated_certificates, key=lambda record: record["small_group"]
        ),
        "kernel_record_count": len(rows) - len(excluded_rows),
        "status_distribution": dict(sorted(status_counts.items())),
        "unique_faithful_graph_count": len(unique_faithful),
        "exact_candidate_distribution": [
            {"nu": pair[0], "a": pair[1], "count": count}
            for pair, count in sorted(exact_distribution.items())
        ],
        "failure_rows": failures,
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "quotients": [
            {
                "q_order": key[0], "q_id": key[1],
                "structure": complete_inventory[key]["structure"],
                "exterior_order": int(complete_inventory[key]["exterior_order"]),
                "normal_kernel_count": quotient_counts[key],
            }
            for key in sorted(quotient_counts)
        ],
        "candidate_records": candidate_records,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    text = "\n".join([
        "status=[COMPUTED] exact bounded batch; no global h(7) upper bound claimed",
        "quotient_rows=%d scanned=%d excluded=%d kernels=%d statuses=%r"
        % (len(expected_quotients), len(quotient_counts), len(excluded),
           len(rows) - len(excluded_rows), sorted(status_counts.items())),
        "faithful_unique_graphs=%d exact_candidates=%d distribution=%r"
        % (len(unique_faithful), len(candidate_records), sorted(exact_distribution.items())),
        "failure_rows=%r" % failures,
        "largest_kernel_counts=%r" % sorted(
            ((count, key[0], key[1], complete_inventory[key]["structure"])
             for key, count in quotient_counts.items()), reverse=True
        )[:12],
        "wrote %s" % args.output,
    ]) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
