#!/usr/bin/env python3
"""Write the exact normalized C2^6 rank-six-pencil certificate."""

from __future__ import annotations

import argparse
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from h7_c2_6_pencils import exact_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    certificate = exact_certificate()
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact normalized rank-six-pencil certificate; not a full C2^6 scan",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
        "conclusion": (
            "Every two-dimensional subspace of Alt(6,2) containing a rank-six form has "
            "clique number at least the recorded exact minimum. The normalized enumeration "
            "and its 6 pencil orbits (from 12 nontrivial raw-gamma orbits, or 14 raw-form "
            "orbits including zero and beta) under 63 symplectic "
            "transvections are exhaustive "
            "after fixing the rank-six form. This does not classify subspaces containing "
            "no rank-six form."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    text = "\n".join([
        output["status"],
        "normalized_pencils=%d raw_form_orbits=%d pencil_orbits=%d minimum_omega=%d"
        % (
            certificate["normalized_pencil_count"],
            certificate["all_raw_form_orbit_count_including_zero_and_beta"],
            certificate["symplectic_pencil_orbit_count"],
            certificate["minimum_omega"],
        ),
        "rank_profiles=%r" % [
            (record["ranks"], record["count"])
            for record in certificate["rank_profile_distribution"]
        ],
        "orbit_omegas=%r" % [
            (record["representative_gamma"], record["orbit_size"], record["omega"])
            for record in certificate["pencil_orbits"]
        ],
        "wrote %s" % args.output,
    ]) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
