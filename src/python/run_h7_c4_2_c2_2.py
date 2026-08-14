#!/usr/bin/env python3
"""Write the exact ``SmallGroup(64,192)`` exterior-kernel certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from h7_c4_2_c2_2 import exact_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory-certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    inventory_raw = args.inventory_certificate.read_bytes()
    inventory = json.loads(inventory_raw)
    if inventory["quotient_count"] != 738:
        raise ValueError("complete quotient inventory is required")
    producer_path = Path(__file__).with_name("h7_c4_2_c2_2.py")
    runner_path = Path(__file__)
    producer_record = Path("src/python/h7_c4_2_c2_2.py")
    runner_record = Path("src/python/run_h7_c4_2_c2_2.py")
    producer_raw = producer_path.read_bytes()
    runner_raw = runner_path.read_bytes()
    certificate = exact_certificate()
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact for Q=C4^2 x C2^2; no global h(7) upper bound claimed",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "quotient": {"small_group": [64, 192], "structure": "C4 x C4 x C2 x C2"},
        "inventory_certificate": str(args.inventory_certificate),
        "inventory_certificate_sha256": hashlib.sha256(inventory_raw).hexdigest(),
        "producer": str(producer_record),
        "producer_sha256": hashlib.sha256(producer_raw).hexdigest(),
        "runner": str(runner_record),
        "runner_sha256": hashlib.sha256(runner_raw).hexdigest(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
        "conclusion": (
            "The three-case C4-projection classification enumerates every one of the "
            "5,276 subgroups of C4 x C2^5 exactly once. Of them 2,925 have a nonzero "
            "commutator radical, while every one of the 2,351 faithful kernels has a "
            "saved and verified eight-clique. Thus this quotient has no exact-center "
            "case with clique number at most seven."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    text = "\n".join([
        output["status"],
        "binary_subspaces=%d exterior_subgroups=%d statuses=%r"
        % (
            certificate["binary_subspace_count"], certificate["subgroup_count"],
            certificate["status_distribution"],
        ),
        "unique_graphs=%d unique_faithful_graphs=%d candidates=%d"
        % (
            certificate["unique_graph_count"],
            certificate["unique_faithful_graph_count"],
            certificate["cutoff_seven_candidate_count"],
        ),
        "radical_sizes=%r" % certificate["radical_size_distribution"],
        "wrote %s" % args.output,
    ]) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
