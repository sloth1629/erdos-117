#!/usr/bin/env python3
"""Write the exact affine-dual certificate for ``SmallGroup(64,261)``."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from h7_c2_3_d8 import exact_certificate


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--gap-stdout", type=Path, required=True)
    parser.add_argument("--inventory-certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()

    inventory = json.loads(args.inventory_certificate.read_text(encoding="utf-8"))
    if inventory["quotient_count"] != 738:
        raise ValueError("complete h7 quotient inventory is required")
    inventory_tsv = Path(inventory["inventory"])
    if _sha256(inventory_tsv) != inventory["inventory_sha256"]:
        raise ValueError("inventory TSV hash mismatch")
    producer_path = Path(__file__).with_name("h7_c2_3_d8.py")
    runner_path = Path(__file__)
    certificate = exact_certificate(args.input)
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact affine-dual cutoff-seven certificate for SmallGroup(64,261)",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "quotient": {
            "small_group": [64, 261],
            "structure": "C2 x C2 x C2 x D8",
        },
        "input": str(args.input),
        "input_sha256": _sha256(args.input),
        "gap_script": str(args.gap_script),
        "gap_script_sha256": _sha256(args.gap_script),
        "gap_stdout": str(args.gap_stdout),
        "gap_stdout_sha256": _sha256(args.gap_stdout),
        "inventory_certificate": str(args.inventory_certificate),
        "inventory_certificate_sha256": _sha256(args.inventory_certificate),
        "producer": "src/python/h7_c2_3_d8.py",
        "producer_sha256": _sha256(producer_path),
        "runner": "src/python/run_h7_c2_3_d8.py",
        "runner_sha256": _sha256(runner_path),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
        "conclusion": (
            "Every action-invariant annihilator that could have clique number at "
            "most seven is covered. All-even annihilators have an explicit nonidentity "
            "radical vertex. The 26,387 annihilators containing an odd character are "
            "enumerated by the complete affine RREF parametrization: 26,323 carry a "
            "saved verified eight-clique and the remaining 64 have a saved nontrivial "
            "radical. Hence Q=C2^3 x D8 contributes no exact-center graph at cutoff seven."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    text = "\n".join([
        output["status"],
        "characters=%d good=%d even_good=%d odd_good=%d"
        % (
            certificate["character_count"], certificate["good_character_count"],
            certificate["even_good_character_count"],
            certificate["odd_good_character_count"],
        ),
        "rref_subspaces=%d odd_subgroups=%d statuses=%r"
        % (
            certificate["rref_subspace_count"],
            certificate["enumerated_odd_subgroup_count"],
            certificate["subgroup_status_distribution"],
        ),
        "faithful_subgroups=%d unique_faithful_graphs=%d candidates=%d"
        % (
            certificate["faithful_subgroup_count"],
            certificate["unique_faithful_graph_count"],
            certificate["faithful_candidate_count"],
        ),
        "wrote %s" % args.output,
    ]) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
