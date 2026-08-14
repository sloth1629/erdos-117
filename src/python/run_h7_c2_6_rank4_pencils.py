#!/usr/bin/env python3
"""Write the exact C2^6 rank-four/no-rank-six pencil certificate."""

from __future__ import annotations

import argparse
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from h7_c2_6_rank4_pencils import exact_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    certificate = exact_certificate()
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact rank-four-pencil dichotomy; not by itself a full C2^6 proof",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
        "conclusion": (
            "For every normalized pencil containing the fixed rank-four form and no "
            "rank-six form, either the pencil has a stored verified 8-clique or its common "
            "radical is exactly the radical of the fixed form. The direct 5,471-pencil "
            "loop is load-bearing; the 12-orbit stabilizer table is a cross-check."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    text = "\n".join([
        output["status"],
        "normalized=%d no_rank_six=%d direct=%r"
        % (
            certificate["normalized_pencil_count"],
            certificate["no_rank_six_pencil_count"],
            certificate["direct_dichotomy_distribution"],
        ),
        "stabilizer_generators=%d orbits=%d relevant_orbits=%d low_reps=%r"
        % (
            certificate["stabilizer_generator_count"], certificate["stabilizer_orbit_count"],
            certificate["relevant_orbit_count"], certificate["low_orbit_representatives"],
        ),
        "orbit_table=%r" % [
            (
                record["representative_gamma"], record["orbit_size"],
                record["rank_profile"], record["omega"], len(record["common_radical"]),
            )
            for record in certificate["orbits"]
        ],
        "wrote %s" % args.output,
    ]) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
