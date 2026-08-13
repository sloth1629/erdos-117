#!/usr/bin/env python3
"""Run deterministic exact computations from a JSON configuration."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence

from exact_invariants import analyze_group
from finite_groups import named_group


SCHEMA_VERSION = 1


def run(config_path: Path) -> Dict[str, object]:
    raw = config_path.read_bytes()
    config = json.loads(raw)
    records: List[Dict[str, object]] = []
    for entry in config["groups"]:
        group = named_group(entry["id"])
        records.append(analyze_group(group, bool(entry.get("independent_cover", True))))
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "[COMPUTED]",
        "configuration": str(config_path),
        "configuration_sha256": hashlib.sha256(raw).hexdigest(),
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "external_dependencies": [],
        },
        "records": records,
    }


def write_group_csv(path: Path, records: Sequence[Dict[str, object]], witness_path: str) -> None:
    fieldnames = [
        "group_id",
        "order",
        "center_order",
        "central_index",
        "nu",
        "a",
        "derived_length",
        "nilpotency_class",
        "solvable",
        "fitting_order",
        "commuting_probability",
        "method",
        "status",
        "witness_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for record in records:
            center_order = len(record["center"])  # type: ignore[arg-type]
            writer.writerow(
                {
                    "group_id": record["group_id"],
                    "order": record["order"],
                    "center_order": center_order,
                    "central_index": int(record["order"]) // center_order,
                    "nu": record["nu"],
                    "a": record["a"],
                    "derived_length": "",
                    "nilpotency_class": "",
                    "solvable": "",
                    "fitting_order": "",
                    "commuting_probability": record["commuting_probability"],
                    "method": "exact central-coset graph; color-bounded clique branch-and-bound; exact DSATUR; certificate verification; optional maximal-abelian set cover",
                    "status": "[COMPUTED]",
                    "witness_path": witness_path,
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--group-csv", type=Path)
    args = parser.parse_args()
    result = run(args.config)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.group_csv:
        write_group_csv(args.group_csv, result["records"], str(args.output))  # type: ignore[arg-type]
    print("wrote %d exact records to %s" % (len(result["records"]), args.output))  # type: ignore[arg-type]
    for record in result["records"]:  # type: ignore[assignment]
        print(
            "%s: |G|=%s |Z|=%d nu=%s a=%s cp=%s"
            % (
                record["group_id"],
                record["order"],
                len(record["center"]),
                record["nu"],
                record["a"],
                record["commuting_probability"],
            )
        )


if __name__ == "__main__":
    main()
