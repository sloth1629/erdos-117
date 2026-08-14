#!/usr/bin/env python3
"""Write the exact C3^4 alternating-map orbit certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from h7_c3_4 import exact_certificate


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
    certificate = exact_certificate()
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact for Q=C3^4; no global h(7) upper bound claimed",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "quotient": {"small_group": [81, 15], "structure": "C3^4"},
        "inventory_certificate": str(args.inventory_certificate),
        "inventory_certificate_sha256": hashlib.sha256(inventory_raw).hexdigest(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
        "conclusion": (
            "Among every faithful alternating commutator map on C3^4, the only orbit with "
            "clique number at most 7 has (nu,a)=(7,10). The zero vector is isolated, and "
            "each F3^times-line is an independent twin class, so passing between the "
            "81-coset graph and its 40-point projective graph preserves omega and chi."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    distribution = [
        (record["omega"], record["chi"], record["subspace_count"])
        for record in certificate["weighted_invariant_distribution"]
    ]
    text = "\n".join([
        "status=[COMPUTED] exact for Q=C3^4; no global h(7) upper bound claimed",
        "subspaces=%d faithful=%d nonfaithful=%d orbits=%d"
        % (
            certificate["raw_subspace_count"], certificate["faithful_subspace_count"],
            certificate["nonfaithful_subspace_count"], certificate["orbit_count"],
        ),
        "weighted_distribution=%r" % distribution,
        "eligible_orbits=%r maximum_a=%d"
        % (certificate["eligible_orbit_indices"], certificate["maximum_a_at_nu_at_most_7"]),
        "wrote %s" % args.output,
    ]) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
