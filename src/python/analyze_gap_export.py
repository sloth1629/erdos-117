#!/usr/bin/env python3
"""Analyze and certify multiplication tables exported independently by GAP."""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

from exact_invariants import analyze_group
from finite_groups import FiniteGroup


def read_gap_tsv(path: Path) -> Tuple[Dict[str, str], List[Dict[str, str]]]:
    metadata: Dict[str, str] = {}
    data_lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("\t", 1)
            metadata[key] = value
        elif line:
            data_lines.append(line)
    reader = csv.DictReader(data_lines, delimiter="\t")
    return metadata, list(reader)


def parse_group(row: Dict[str, str]) -> FiniteGroup:
    count = int(row["element_count"])
    elements = tuple(row["elements"].split(","))
    table = tuple(tuple(int(value) - 1 for value in raw_row.split(",")) for raw_row in row["multiplication_table"].split(";"))
    if len(elements) != count or len(table) != count:
        raise ValueError("GAP export row has inconsistent dimensions")
    return FiniteGroup(row["group_id"], elements, table)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--omit-multiplication-tables",
        action="store_true",
        help="keep tables only in the checksummed source TSV to reduce JSON size",
    )
    parser.add_argument(
        "--independent-cover-max-order",
        type=int,
        default=32,
        help="enumerate maximal abelian subgroups independently through this order",
    )
    args = parser.parse_args()
    raw = args.input.read_bytes()
    metadata, rows = read_gap_tsv(args.input)
    records = []
    for row in rows:
        group = parse_group(row)
        record = analyze_group(group, group.order <= args.independent_cover_max_order)
        record["smallgroups_structure_description"] = row["structure_description"]
        nu, cover_number = int(record["nu"]), int(record["a"])
        candidate_bound = max(nu, 2 ** ((nu - 1) // 2) + 1)
        record["candidate_bound"] = candidate_bound
        record["candidate_bound_slack"] = candidate_bound - cover_number
        if args.omit_multiplication_tables:
            del record["multiplication_table"]
        records.append(record)
        print("%s: nu=%d a=%d" % (group.group_id, record["nu"], record["a"]))
    distribution = Counter((int(record["nu"]), int(record["a"])) for record in records)
    strict_records = [record["group_id"] for record in records if int(record["a"]) > int(record["nu"])]
    violations = [record["group_id"] for record in records if int(record["candidate_bound_slack"]) < 0]
    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "gap_export": str(args.input),
        "gap_export_sha256": hashlib.sha256(raw).hexdigest(),
        "gap_metadata": metadata,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "python": platform.python_version(),
        "external_python_dependencies": [],
        "multiplication_tables_embedded": not args.omit_multiplication_tables,
        "summary": {
            "record_count": len(records),
            "nu_a_distribution": [
                {"nu": nu, "a": cover_number, "count": count}
                for (nu, cover_number), count in sorted(distribution.items())
            ],
            "a_greater_than_nu_group_ids": strict_records,
            "candidate_bound_violating_group_ids": violations,
            "candidate_bound_formula": "max(nu, 2^floor((nu-1)/2)+1)",
        },
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("wrote %d verified records to %s" % (len(records), args.output))


if __name__ == "__main__":
    main()
