#!/usr/bin/env python3
"""Write the compact multi-quotient order-64 character-dual certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from h7_order64_dual import exact_certificate


EXPECTED_IDS = (193, 195, 202, 203, 207, 211, 216, 226, 236, 242, 250)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--gap-stdout", type=Path, action="append", required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--inventory-certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    if len(args.input) != len(args.gap_stdout):
        raise ValueError("each input requires one GAP stdout log")
    inventory = json.loads(args.inventory_certificate.read_text(encoding="utf-8"))
    if inventory["quotient_count"] != 738:
        raise ValueError("complete quotient inventory required")
    inventory_tsv = Path(inventory["inventory"])
    if sha256(inventory_tsv) != inventory["inventory_sha256"]:
        raise ValueError("inventory TSV hash mismatch")

    certificates = [exact_certificate(path) for path in args.input]
    ids = tuple(certificate["metadata"]["Q_ID"] for certificate in certificates)
    if tuple(map(int, ids)) != EXPECTED_IDS:
        raise ValueError("canonical generic dual inputs are incomplete or out of order")
    for expected_id, path in zip(EXPECTED_IDS, args.gap_stdout):
        if "_%d_gap.stdout.txt" % expected_id not in path.name:
            raise ValueError("GAP stdout paths are not aligned with input quotient IDs")
    producer_path = Path(__file__).with_name("h7_order64_dual.py")
    runner_path = Path(__file__)
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact character-dual cutoff-seven certificate for eleven order-64 quotients",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "inputs": [
            {"path": str(path), "sha256": sha256(path)} for path in args.input
        ],
        "gap_stdout": [
            {"path": str(path), "sha256": sha256(path)} for path in args.gap_stdout
        ],
        "gap_script": str(args.gap_script),
        "gap_script_sha256": sha256(args.gap_script),
        "inventory_certificate": str(args.inventory_certificate),
        "inventory_certificate_sha256": sha256(args.inventory_certificate),
        "producer": "src/python/h7_order64_dual.py",
        "producer_sha256": sha256(producer_path),
        "runner": "src/python/run_h7_order64_dual.py",
        "runner_sha256": sha256(runner_path),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificates": certificates,
        "conclusion": (
            "For each quotient, a no-automorphism-quotient BFS enumerates every "
            "action-invariant character subgroup whose union graph has no eight-clique. "
            "Every retained graph has a saved nonidentity radical. Every pruned boundary "
            "subgroup has a saved verified eight-clique, as does every individually bad "
            "scalar character. Thus none of the eleven quotients contributes an "
            "exact-center graph at clique cutoff seven."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    lines = [output["status"]]
    for certificate in certificates:
        lines.append(
            "ID=%s characters=%d good=%d retained=%d boundary=%d radicals=%r"
            % (
                certificate["metadata"]["Q_ID"], certificate["character_count"],
                certificate["good_character_count"],
                certificate["retained_no_eight_subgroup_count"],
                certificate["pruned_boundary_subgroup_count"],
                certificate["radical_size_distribution"],
            )
        )
    lines.append("wrote %s" % args.output)
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
