#!/usr/bin/env python3
"""Verify the order-64 selected-cover exterior-zero certificate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Sequence, Tuple


EXPECTED_TRIVIAL_CENTER_IMAGE_IDS_192_267 = (
    192, 193, 195, 202, 203, 207, 211, 216, 226, 236, 242, 250, 261, 267,
)


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


def parse_vector(raw: str) -> Tuple[int, ...]:
    return tuple(int(value) for value in raw.split(",") if value != "")


def parse_vector_list(raw: str) -> Tuple[Tuple[int, ...], ...]:
    return tuple(parse_vector(value) for value in raw.split(";")) if raw else ()


def parse_pc_presentation(raw: str):
    parts = raw.split("|")
    if len(parts) != 3:
        raise AssertionError("malformed pc presentation")
    orders = parse_vector(parts[0])
    powers = parse_vector_list(parts[1])
    commutators = parse_vector_list(parts[2])
    dimension = len(orders)
    if not orders or any(order < 2 for order in orders):
        raise AssertionError("invalid pc relative orders")
    if len(powers) != dimension or any(len(vector) != dimension for vector in powers):
        raise AssertionError("wrong pc power-relation shape")
    if len(commutators) != dimension * (dimension - 1) // 2 or any(
        len(vector) != dimension for vector in commutators
    ):
        raise AssertionError("wrong pc commutator-relation shape")
    for vector in (*powers, *commutators):
        if any(not 0 <= exponent < order for exponent, order in zip(vector, orders)):
            raise AssertionError("pc exponent is out of range")
    # In a polycyclic generating sequence, a power of generator i uses only
    # later generators; [g_i,g_j] for j<i likewise lies after g_i.
    for index, vector in enumerate(powers):
        if any(vector[: index + 1]):
            raise AssertionError("pc power relation is not triangular")
    relation = 0
    for left in range(dimension):
        for _right in range(left):
            vector = commutators[relation]
            relation += 1
            if any(vector[: left + 1]):
                raise AssertionError("pc commutator relation is not triangular")
    return orders, powers, commutators


def _product(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def validate_capability_batches(
    inputs: Sequence[Path], inventory_path: Path,
) -> Dict[str, object]:
    inventory_document = json.loads(inventory_path.read_text(encoding="utf-8"))
    inventory_tsv = Path(inventory_document["inventory"])
    if not inventory_tsv.is_absolute():
        inventory_tsv = Path.cwd() / inventory_tsv
    if sha256(inventory_tsv) != inventory_document["inventory_sha256"]:
        raise AssertionError("quotient inventory hash mismatch")
    _, inventory_rows = parse_tsv(inventory_tsv)
    inventory = {
        (int(row["q_order"]), int(row["q_id"])): row for row in inventory_rows
    }

    all_rows = []
    expected_ids = set()
    batch_metadata = []
    for path in inputs:
        metadata, rows = parse_tsv(path)
        if metadata.get("GAP_VERSION") != "4.16.0" or metadata.get("SMALLGRP_VERSION") != "1.5.4":
            raise AssertionError("unexpected GAP/SmallGrp version")
        if metadata.get("Q_ORDER") != "64" or metadata.get("SCHUR_COVER_PRIMES") != "2":
            raise AssertionError("unexpected capability-batch scope")
        start, end = int(metadata["START_Q_ID"]), int(metadata["END_Q_ID"])
        ids = set(range(start, end + 1))
        if expected_ids & ids:
            raise AssertionError("capability batches overlap")
        expected_ids |= ids
        batch_metadata.append(metadata)
        all_rows.extend(rows)
    if expected_ids != set(range(192, 268)):
        raise AssertionError("canonical capability batches must cover IDs 192..267")

    by_id = defaultdict(list)
    for row in all_rows:
        q_id = int(row["q_id"])
        if q_id not in expected_ids:
            raise AssertionError("capability row is outside declared batches")
        by_id[q_id].append(row)
    if set(by_id) != expected_ids:
        raise AssertionError("capability quotient serials are incomplete")

    epicentre_distribution = Counter()
    trivial_center_image_ids = []
    witness_records = []
    quotient_records = []
    for q_id in sorted(by_id):
        rows = by_id[q_id]
        first = rows[0]
        invariant_fields = (
            "structure", "q_pc_presentation", "cover_order", "cover_pc_presentation",
            "pc_conversion_kernel_order", "cover_kernel_order", "cover_kernel_central",
            "cover_kernel_in_derived", "exterior_order", "exterior_orders",
            "epicentre_size", "runtime_ms",
        )
        if any(any(row[field] != first[field] for field in invariant_fields) for row in rows[1:]):
            raise AssertionError("inconsistent per-quotient capability fields")
        inventory_row = inventory[(64, q_id)]
        # GAP's StructureDescription is not canonical: some calls append a
        # redundant ``: 1``.  The SmallGroup ID and checked pc presentation,
        # not this display string, identify the quotient.

        q_orders, _, _ = parse_pc_presentation(first["q_pc_presentation"])
        cover_orders, _, _ = parse_pc_presentation(first["cover_pc_presentation"])
        if _product(q_orders) != 64:
            raise AssertionError("quotient pc presentation has wrong order")
        cover_order = int(first["cover_order"])
        cover_kernel_order = int(first["cover_kernel_order"])
        if _product(cover_orders) != cover_order:
            raise AssertionError("cover pc presentation has wrong order")
        if int(first["pc_conversion_kernel_order"]) != 1:
            raise AssertionError("Schur-cover pc conversion is not injective")
        if first["cover_kernel_central"] != "true":
            raise AssertionError("selected Schur-cover kernel is not certified central")
        if first["cover_kernel_in_derived"] != "true":
            raise AssertionError("selected Schur-cover kernel is not certified stem")
        if cover_order != 64 * cover_kernel_order:
            raise AssertionError("cover/kernel/quotient orders disagree")
        if cover_kernel_order != int(inventory_row["multiplier_order"]):
            raise AssertionError("cover kernel disagrees with multiplier inventory")
        exterior_orders = parse_vector(first["exterior_orders"])
        exterior_order = int(first["exterior_order"])
        if not exterior_orders or _product(exterior_orders) != exterior_order:
            raise AssertionError("exterior invariant factors have wrong product")
        if exterior_order != int(inventory_row["exterior_order"]):
            raise AssertionError("derived cover has wrong exterior-square order")

        epicentre_size = int(first["epicentre_size"])
        if epicentre_size != len(rows):
            raise AssertionError("epicentre row count disagrees")
        positions = [int(row["epicentre_position"]) for row in rows]
        if len(set(positions)) != epicentre_size or any(not 1 <= value <= 64 for value in positions):
            raise AssertionError("invalid epicentre element positions")
        epicentre_distribution[epicentre_size] += 1
        if epicentre_size == 1:
            trivial_center_image_ids.append(q_id)

        identity_rows = []
        q_exponent_vectors = set()
        for row in rows:
            q_exponents = parse_vector(row["q_exponents"])
            lift_exponents = parse_vector(row["lift_exponents"])
            lift_commutators = parse_vector_list(row["lift_commutators"])
            witness_commutator_row = parse_vector_list(row["witness_commutator_row"])
            if len(q_exponents) != len(q_orders) or any(
                not 0 <= exponent < order for exponent, order in zip(q_exponents, q_orders)
            ):
                raise AssertionError("invalid quotient epicentre exponent vector")
            if q_exponents in q_exponent_vectors:
                raise AssertionError("duplicate epicentre exponent vector")
            q_exponent_vectors.add(q_exponents)
            if len(lift_exponents) != len(cover_orders) or any(
                not 0 <= exponent < order for exponent, order in zip(lift_exponents, cover_orders)
            ):
                raise AssertionError("invalid cover-lift exponent vector")
            if len(lift_commutators) != len(cover_orders) or any(
                len(vector) != len(cover_orders) or any(vector)
                for vector in lift_commutators
            ):
                raise AssertionError("cover lift is not certified central")
            if len(witness_commutator_row) != 64 or any(
                len(vector) != len(exterior_orders)
                or any(not 0 <= exponent < order for exponent, order in zip(vector, exterior_orders))
                or any(vector)
                for vector in witness_commutator_row
            ):
                raise AssertionError("saved universal exterior commutator row is not zero")
            is_identity = row["is_identity"] == "true"
            if row["is_identity"] not in ("true", "false"):
                raise AssertionError("invalid identity flag")
            if is_identity != (not any(q_exponents) and not any(lift_exponents)):
                raise AssertionError("identity flag disagrees with exponent witnesses")
            if is_identity:
                identity_rows.append(row)
            else:
                witness_records.append({
                    "q_id": q_id,
                    "epicentre_position": int(row["epicentre_position"]),
                    "q_exponents": list(q_exponents),
                    "lift_exponents": list(lift_exponents),
                    "cover_generator_commutators": [list(vector) for vector in lift_commutators],
                    "universal_exterior_commutator_row": [
                        list(vector) for vector in witness_commutator_row
                    ],
                })
        if len(identity_rows) != 1:
            raise AssertionError("epicentre has wrong identity-row count")
        quotient_records.append({
            "q_id": q_id,
            "structure": first["structure"],
            "q_pc_relative_orders": list(q_orders),
            "cover_order": cover_order,
            "cover_pc_relative_orders": list(cover_orders),
            "cover_kernel_order": cover_kernel_order,
            "exterior_order": exterior_order,
            "exterior_relative_orders": list(exterior_orders),
            "epicentre_size": epicentre_size,
            "epicentre_positions": sorted(positions),
            "trivial_center_image": epicentre_size == 1,
            "runtime_ms": int(first["runtime_ms"]),
        })

    if tuple(trivial_center_image_ids) != EXPECTED_TRIVIAL_CENTER_IMAGE_IDS_192_267:
        raise AssertionError("unexpected trivial-center-image quotient list")
    exterior_zero_excluded_ids = sorted(expected_ids - set(trivial_center_image_ids))
    for q_id in exterior_zero_excluded_ids:
        nonidentity = [record for record in witness_records if record["q_id"] == q_id]
        if not nonidentity:
            raise AssertionError("excluded quotient lacks a nonidentity exterior-zero witness")
        for record in nonidentity:
            if not any(record["q_exponents"]):
                raise AssertionError("purported epicentre witness is the identity")
            if any(any(vector) for vector in record["universal_exterior_commutator_row"]):
                raise AssertionError("epicentre exterior-commutator witness is nonzero")
    for q_id in range(262, 267):
        nonidentity = [record for record in witness_records if record["q_id"] == q_id]
        if len(nonidentity) != 1 or nonidentity[0]["epicentre_position"] != 7:
            raise AssertionError("unexpected SG(64,262..266) epicentre witness")
        if nonidentity[0]["q_exponents"] != [0, 0, 0, 0, 0, 1]:
            raise AssertionError("epicentre witness is not Pcgs(Q)[6]")
    return {
        "batch_metadata": batch_metadata,
        "quotient_count": len(by_id),
        "epicentre_size_distribution": {
            str(key): value for key, value in sorted(epicentre_distribution.items())
        },
        # The first field is only the complementary GAP cover-center census.
        # The load-bearing conclusion uses the explicit one-way exclusions in
        # ``exterior_zero_excluded_ids`` and does not assert a converse.
        "trivial_center_image_ids": trivial_center_image_ids,
        "exterior_zero_excluded_ids": exterior_zero_excluded_ids,
        "quotients": quotient_records,
        "nonidentity_epicentre_witnesses": witness_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--gap-stdout", type=Path, action="append", required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    if len(args.input) != len(args.gap_stdout):
        raise ValueError("each input batch requires one GAP stdout log")
    certificate = validate_capability_batches(args.input, args.inventory)
    output = {
        "schema_version": 1,
        "status": "[COMPUTED] exact selected-cover exterior-zero census for SmallGroups(64,192..267)",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "inputs": [
            {"path": str(path), "sha256": sha256(path)} for path in args.input
        ],
        "gap_stdout": [
            {"path": str(path), "sha256": sha256(path)} for path in args.gap_stdout
        ],
        "gap_script": str(args.gap_script),
        "gap_script_sha256": sha256(args.gap_script),
        "inventory": str(args.inventory),
        "inventory_sha256": sha256(args.inventory),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
        "conclusion": (
            "The image of the center of each selected injectively pc-converted 2-Schur "
            "cover was enumerated in Q. For 62 quotients, a saved nonidentity quotient "
            "element has a complete 64-entry universal exterior-commutator row equal to "
            "zero. These explicit rows give the load-bearing one-way exterior-zero "
            "exclusions; no converse capability assertion is used."
        ),
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    text = "\n".join([
        output["status"],
        "quotients=%d epicentre_sizes=%r"
        % (certificate["quotient_count"], certificate["epicentre_size_distribution"]),
        "trivial_center_image_ids=%r" % certificate["trivial_center_image_ids"],
        "exterior_zero_excluded_count=%d witness_count=%d"
        % (
            len(certificate["exterior_zero_excluded_ids"]),
            len(certificate["nonidentity_epicentre_witnesses"]),
        ),
        "wrote %s" % args.output,
    ]) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
