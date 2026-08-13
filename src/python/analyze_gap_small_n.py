#!/usr/bin/env python3
"""Certify exact invariants in a GAP central-coset graph prefilter export."""

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
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--order", type=int, required=True)
    parser.add_argument("--total-groups", type=int, required=True)
    parser.add_argument("--clique-cutoff", type=int, required=True)
    args = parser.parse_args()

    raw = args.input.read_bytes()
    with args.input.open(newline="", encoding="utf-8") as handle:
        source_rows = list(csv.DictReader(handle, delimiter="\t"))
    records = []
    for row in source_rows:
        adjacency = parse_adjacency(row["adjacency"], int(row["coset_count"]))
        clique = maximum_clique(adjacency)
        coloring = exact_chromatic_number(adjacency, clique.size)
        if clique.size > args.clique_cutoff:
            raise AssertionError("GAP prefilter admitted a graph above the cutoff")
        if not verify_clique(adjacency, clique.vertices):
            raise AssertionError("clique witness failed")
        if not verify_coloring(adjacency, coloring.colors):
            raise AssertionError("coloring witness failed")
        records.append(
            {
                "status": "[COMPUTED]",
                "group_id": row["group_id"],
                "structure": row["structure"],
                "center_order": int(row["center_size"]),
                "compressed_vertex_count": len(adjacency),
                "is_ac_group": row["is_ac"] == "true",
                "nu": clique.size,
                "a": coloring.size,
                "clique_certificate": list(clique.vertices),
                "coloring_certificate": list(coloring.colors),
                "clique_search_nodes": clique.search_nodes,
                "coloring_search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
            }
        )

    distribution = Counter((record["nu"], record["a"]) for record in records)
    non_ac_by_nu = Counter(record["nu"] for record in records if not record["is_ac_group"])
    strict = [record["group_id"] for record in records if record["a"] > record["nu"]]
    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input": str(args.input),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "order": args.order,
        "total_smallgroups": args.total_groups,
        "clique_cutoff": args.clique_cutoff,
        "survivor_count": len(records),
        "excluded_count": args.total_groups - len(records),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "distribution": [
            {"nu": pair[0], "a": pair[1], "count": count}
            for pair, count in sorted(distribution.items())
        ],
        "non_ac_by_nu": [
            {"nu": nu, "count": count} for nu, count in sorted(non_ac_by_nu.items())
        ],
        "strict_a_greater_nu": strict,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "order=%d total=%d survivors=%d excluded_by_clique=%d"
        % (args.order, args.total_groups, len(records), args.total_groups - len(records))
    )
    print("distribution=%r" % sorted(distribution.items()))
    print("non_ac_by_nu=%r" % sorted(non_ac_by_nu.items()))
    print("strict_a_greater_nu=%r" % strict)
    print("wrote %d exact records to %s" % (len(records), args.output))


if __name__ == "__main__":
    main()
