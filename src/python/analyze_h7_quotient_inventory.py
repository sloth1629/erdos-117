#!/usr/bin/env python3
"""Audit and size the quotient/exterior search implied by f(7)=81.

This is deliberately an inventory, not an h(7) proof.  It validates a fast,
complete Schur-multiplier census and reports which cases require
orbit/structural treatment before any raw normal-kernel scan is attempted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


EXPECTED_SMALLGROUP_COUNTS = {
    1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 2, 7: 1, 8: 5, 9: 2,
    10: 2, 11: 1, 12: 5, 13: 1, 14: 2, 15: 1, 16: 14, 17: 1,
    18: 5, 19: 1, 20: 5, 21: 2, 22: 2, 23: 1, 24: 15, 25: 2,
    26: 2, 27: 5, 28: 4, 29: 1, 30: 4, 31: 1, 32: 51, 33: 1,
    34: 2, 35: 1, 36: 14, 37: 1, 38: 2, 39: 2, 40: 14, 41: 1,
    42: 6, 43: 1, 44: 4, 45: 2, 46: 2, 47: 1, 48: 52, 49: 2,
    50: 5, 51: 1, 52: 5, 53: 1, 54: 15, 55: 2, 56: 13, 57: 2,
    58: 2, 59: 1, 60: 13, 61: 1, 62: 2, 63: 4, 64: 267, 65: 1,
    66: 4, 67: 1, 68: 5, 69: 1, 70: 4, 71: 1, 72: 50, 73: 1,
    74: 2, 75: 3, 76: 4, 77: 1, 78: 6, 79: 1, 80: 52, 81: 15,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_tsv(path: Path):
    metadata = {}
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            metadata[key] = value
        elif line:
            lines.append(line)
    return metadata, list(csv.DictReader(lines, delimiter="\t"))


def gaussian_binomial(n: int, k: int, q: int) -> int:
    value = Fraction(1)
    for index in range(k):
        value *= Fraction(q ** (n - index) - 1, q ** (k - index) - 1)
    if value.denominator != 1:
        raise AssertionError("Gaussian binomial did not simplify")
    return value.numerator


def subspace_count(dimension: int, field_order: int) -> int:
    return sum(
        gaussian_binomial(dimension, subdimension, field_order)
        for subdimension in range(dimension + 1)
    )


def prime(value: int) -> bool:
    return value >= 2 and all(value % divisor for divisor in range(2, int(value ** 0.5) + 1))


def validate_inventory(path: Path):
    """Fully validate and summarize the canonical 738-row GAP inventory."""

    metadata, rows = parse_tsv(path)
    if metadata != {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "MAX_Q_ORDER": "81",
        "IDENTITY": "|Q_wedge_Q|=|M(Q)|*|Q'|",
        "NO_SCHUR_COVER_CONSTRUCTED": "true",
    }:
        raise AssertionError("unexpected complete-inventory metadata")
    if len(rows) != 738:
        raise AssertionError("expected exactly 738 quotient rows")
    by_order = Counter(int(row["q_order"]) for row in rows)
    if dict(sorted(by_order.items())) != EXPECTED_SMALLGROUP_COUNTS:
        raise AssertionError("NumberSmallGroups distribution changed")
    keys = [(int(row["q_order"]), int(row["q_id"])) for row in rows]
    if len(set(keys)) != len(keys):
        raise AssertionError("duplicate quotient row")
    for order, count in EXPECTED_SMALLGROUP_COUNTS.items():
        ids = sorted(group_id for q_order, group_id in keys if q_order == order)
        if ids != list(range(1, count + 1)):
            raise AssertionError("incomplete SmallGroup IDs at order %d" % order)

    indexed = {key: row for key, row in zip(keys, rows)}
    exterior_distribution = Counter()
    elementary_exterior_records = []
    for key, row in indexed.items():
        multiplier = tuple(int(value) for value in row["multiplier_invariants"].split(",") if value)
        multiplier_order = 1
        for invariant in multiplier:
            multiplier_order *= invariant
        if multiplier_order != int(row["multiplier_order"]):
            raise AssertionError("multiplier invariants/order disagree")
        exterior_order = multiplier_order * int(row["q_derived_order"])
        if exterior_order != int(row["exterior_order"]):
            raise AssertionError("exterior order identity failed")
        exterior_distribution[exterior_order] += 1
        if (
            row["q_abelian"] == "true"
            and multiplier
            and len(set(multiplier)) == 1
            and prime(multiplier[0])
        ):
            field_order = multiplier[0]
            dimension = len(multiplier)
            elementary_exterior_records.append({
                "q_order": key[0],
                "q_id": key[1],
                "structure": row["structure"],
                "field_order": field_order,
                "exterior_dimension": dimension,
                "exterior_order": exterior_order,
                "exact_raw_kernel_count": subspace_count(dimension, field_order),
            })

    exact_explosions = sorted(
        (record for record in elementary_exterior_records if record["exact_raw_kernel_count"] > 1_000_000),
        key=lambda record: record["exact_raw_kernel_count"],
        reverse=True,
    )
    if [
        (record["q_order"], record["q_id"], record["exact_raw_kernel_count"])
        for record in exact_explosions
    ] != [
        (64, 267, 623476476706836148),
        (32, 51, 229755605),
        (64, 260, 229755605),
    ]:
        raise AssertionError("unexpected elementary-exterior explosion list")
    tiers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096, 32768]
    tier_counts = {
        str(bound): sum(int(row["exterior_order"]) <= bound for row in rows)
        for bound in tiers
    }
    largest = sorted(
        ({
            "q_order": int(row["q_order"]),
            "q_id": int(row["q_id"]),
            "structure": row["structure"],
            "q_abelian": row["q_abelian"] == "true",
            "q_derived_order": int(row["q_derived_order"]),
            "multiplier_invariants": [
                int(value) for value in row["multiplier_invariants"].split(",") if value
            ],
            "exterior_order": int(row["exterior_order"]),
        } for row in rows),
        key=lambda record: (record["exterior_order"], record["q_order"], record["q_id"]),
        reverse=True,
    )[:30]
    return {
        "metadata": metadata,
        "rows": rows,
        "indexed": indexed,
        "by_order": by_order,
        "exterior_distribution": exterior_distribution,
        "elementary_exterior_records": elementary_exterior_records,
        "exact_explosions": exact_explosions,
        "tier_counts": tier_counts,
        "largest": largest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()

    validated = validate_inventory(args.inventory)
    metadata = validated["metadata"]
    rows = validated["rows"]
    by_order = validated["by_order"]
    exterior_distribution = validated["exterior_distribution"]
    elementary_exterior_records = validated["elementary_exterior_records"]
    exact_explosions = validated["exact_explosions"]
    tier_counts = validated["tier_counts"]
    largest = validated["largest"]

    c3_4 = next(record for record in elementary_exterior_records if (record["q_order"], record["q_id"]) == (81, 15))
    c2_6 = next(record for record in elementary_exterior_records if (record["q_order"], record["q_id"]) == (64, 267))
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] inventory; no h(7) upper bound claimed",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "configuration": str(args.gap_script),
        "configuration_sha256": sha256(args.gap_script),
        "inventory": str(args.inventory),
        "inventory_sha256": sha256(args.inventory),
        "inventory_metadata": metadata,
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "quotient_count": len(rows),
        "smallgroup_counts_by_order": dict(sorted(by_order.items())),
        "abelian_quotient_count": sum(row["q_abelian"] == "true" for row in rows),
        "elementary_abelian_quotient_count": sum(row["q_elementary_abelian"] == "true" for row in rows),
        "exterior_order_distribution": dict(sorted(exterior_distribution.items())),
        "cumulative_exterior_order_tiers": tier_counts,
        "largest_exterior_orders": largest,
        "elementary_abelian_exterior_cases": elementary_exterior_records,
        "exact_raw_kernel_explosions": exact_explosions,
        "planned_separation": {
            "direct_elementary_case": {
                "quotient": [81, 15],
                "description": "C3^4",
                "raw_kernel_count": c3_4["exact_raw_kernel_count"],
                "plan": "direct finite-field subspace scan with GL(4,3) orbit deduplication",
            },
            "mandatory_orbit_case": {
                "quotient": [64, 267],
                "description": "C2^6",
                "raw_kernel_count": c2_6["exact_raw_kernel_count"],
                "plan": "classify GL(6,2)-orbits of common-radical-zero dual subspaces; raw scan impossible",
            },
            "second_mandatory_orbit_case": {
                "quotient": [64, 260],
                "description": "C4 x C2^4 with elementary exterior C2^10",
                "raw_kernel_count": 229755605,
                "plan": "derive faithful alternating-map reduction before enumeration",
            },
            "previously_excluded_case": {
                "quotient": [32, 51],
                "description": "C2^5",
                "raw_kernel_count": 229755605,
                "plan": "reuse the proved >=9-clique exclusion from exact_h6",
            },
        },
        "conclusion": (
            "The complete 738-quotient multiplier inventory is exact.  A raw all-kernel h7 scan is unsafe: "
            "C2^6 alone has 623476476706836148 kernels.  No h(7)<=10 conclusion is inferred."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "status=[COMPUTED] inventory only; no h(7) upper bound claimed",
        "quotients=%d abelian=%d elementary_abelian=%d"
        % (output["quotient_count"], output["abelian_quotient_count"], output["elementary_abelian_quotient_count"]),
        "cumulative_exterior_tiers=%r" % tier_counts,
        "exact_raw_kernel_explosions=%r" % [
            (r["q_order"], r["q_id"], r["structure"], r["exact_raw_kernel_count"])
            for r in exact_explosions
        ],
        "C3^4_raw_kernels=%d; C2^6_raw_kernels=%d"
        % (c3_4["exact_raw_kernel_count"], c2_6["exact_raw_kernel_count"]),
        "wrote %s" % args.output,
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
