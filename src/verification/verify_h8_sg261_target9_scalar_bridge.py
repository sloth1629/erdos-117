#!/usr/bin/env python3
"""Repair the target-nine scalar-completeness bridge for SmallGroup(64,261)."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Sequence


REPOSITORY = Path(__file__).resolve().parents[2]
PYTHON_SOURCES = REPOSITORY / "src" / "python"
if str(PYTHON_SOURCES) not in sys.path:
    sys.path.insert(0, str(PYTHON_SOURCES))

import h7_c2_3_d8 as sg261  # noqa: E402
from exact_invariants import maximum_clique, verify_clique  # noqa: E402


EXPORT = REPOSITORY / "experiments" / "logs" / "h7_c2_3_d8.tsv"
H7_DOCUMENT = REPOSITORY / "experiments" / "logs" / "h7_c2_3_d8.json"
DEFAULT_OUTPUT = (
    REPOSITORY
    / "experiments"
    / "logs"
    / "h8_sg261_target9_scalar_bridge.json"
)
EXPECTED_DISTRIBUTION = {
    1: 1,
    3: 155,
    5: 884,
    6: 112,
    11: 448,
    12: 448,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def index_sha256(indices: Sequence[int]) -> str:
    payload = b"".join(int(index).to_bytes(2, "little") for index in indices)
    return hashlib.sha256(payload).hexdigest()


def _saved_h7_good_indices(
    certificate: dict[str, object],
    characters: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    """Recover the complete scalar-good set certified at cutoff seven."""

    records = certificate["scalar_records"]
    if not isinstance(records, list) or len(records) != len(characters) - 1:
        raise AssertionError("the saved h7 scalar serial range is incomplete")
    good = {0}
    for expected_index, record in enumerate(records, 1):
        if record["character_index"] != expected_index:
            raise AssertionError("the saved h7 scalar indices are incomplete")
        if tuple(record["character"]) != characters[expected_index]:
            raise AssertionError("saved h7 scalar character/index mismatch")
        status = record["status"]
        if status == "clique_ge_8":
            witness = tuple(record["witness"])
            if len(witness) != 8:
                raise AssertionError("saved h7 scalar boundary is not a K8")
        elif status in {"omega_3", "omega_5", "omega_6"}:
            if int(record["omega"]) != int(status.split("_")[1]):
                raise AssertionError("saved h7 exact scalar omega mismatch")
            good.add(expected_index)
        else:
            raise AssertionError(f"unknown saved h7 scalar status {status}")
    if len(good) != 1152:
        raise AssertionError(f"wrong saved h7 scalar-good count {len(good)}")
    return tuple(sorted(good))


def _saved_affine_good_indices(
    certificate: dict[str, object],
    characters: tuple[tuple[int, ...], ...],
    orders: tuple[int, ...],
) -> tuple[int, ...]:
    """Rebuild the affine scalar universe used by the h7 subgroup census."""

    if orders != (2,) * 9 + (4,):
        raise AssertionError("unexpected SG261 exterior character coordinates")
    character_indices = {character: index for index, character in enumerate(characters)}
    odd_base = tuple(int(value) for value in certificate["odd_base_character"])
    basis = tuple(int(value) for value in certificate["affine_coordinate_basis"])

    span = {0}
    for vector in basis:
        span |= {value ^ vector for value in tuple(span)}
    if len(span) != 128:
        raise AssertionError("saved SG261 affine coordinates do not span a 7-space")

    def hchar(code: int) -> tuple[int, ...]:
        return tuple((code >> index) & 1 for index in range(9)) + (
            2 * ((code >> 9) & 1),
        )

    all_even = {
        index for index, character in enumerate(characters) if character[-1] % 2 == 0
    }
    odd_affine = {
        character_indices[sg261._add(odd_base, hchar(code), orders)]
        for code in span
    }
    if len(all_even) != 1024 or len(odd_affine) != 128:
        raise AssertionError("wrong SG261 affine scalar-universe component sizes")
    if all_even & odd_affine:
        raise AssertionError("SG261 even and odd affine scalar components overlap")
    return tuple(sorted(all_even | odd_affine))


def build_certificate() -> dict[str, object]:
    """Recompute every scalar graph and the missing target-nine bridge."""

    document = json.loads(H7_DOCUMENT.read_text(encoding="utf-8"))
    certificate = document["certificate"]
    sg261.verify_certificate(certificate, EXPORT)
    parsed = sg261.parse_export(EXPORT)
    orders = tuple(int(order) for order in parsed["exterior_orders"])
    characters = tuple(itertools.product(*(range(order) for order in orders)))
    if len(characters) != 2048:
        raise AssertionError("unexpected SG261 character count")

    h7_good = _saved_h7_good_indices(certificate, characters)
    affine_good = _saved_affine_good_indices(certificate, characters, orders)
    if affine_good != h7_good:
        raise AssertionError(
            "saved h7 scalar-good set differs from its affine-universe parameters"
        )
    distribution: Counter[int] = Counter()
    target9_good = []
    target10_good = []
    boundary_records = []
    for index, character in enumerate(characters):
        adjacency = sg261._scalar_graph(character, parsed["commutators"], orders)
        exact = maximum_clique(adjacency)
        omega = exact.size
        distribution[omega] += 1
        if omega < 9:
            target9_good.append(index)
        if omega < 10:
            target10_good.append(index)
        if omega >= 9:
            witness = tuple(exact.vertices[:9])
            if len(witness) != 9 or not verify_clique(adjacency, witness):
                raise AssertionError("invalid SG261 target-nine scalar boundary")
            boundary_records.append(
                {
                    "character_index": index,
                    "character": list(character),
                    "exact_omega": omega,
                    "nine_clique": list(witness),
                }
            )

    observed = dict(sorted(distribution.items()))
    if observed != EXPECTED_DISTRIBUTION:
        raise AssertionError(f"unexpected exact scalar distribution {observed}")
    target9_good_tuple = tuple(target9_good)
    target10_good_tuple = tuple(target10_good)
    if target9_good_tuple != h7_good:
        raise AssertionError("h7 scalar-good set is not target-nine complete")
    if target9_good_tuple != affine_good:
        raise AssertionError("h7 affine universe is not target-nine complete")
    if target10_good_tuple != h7_good:
        raise AssertionError("h7 scalar-good set is not target-ten complete")
    if len(boundary_records) != 896:
        raise AssertionError("wrong target-nine scalar boundary count")

    producer = Path(__file__).resolve()
    return {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "claim": (
            "For SmallGroup(64,261), the 1152 scalar characters admitted "
            "by the cutoff-seven affine certificate are exactly the scalar "
            "characters with no K9 (and also exactly those with no K10)."
        ),
        "quotient": {
            "small_group": [64, 261],
            "structure": "C2 x C2 x C2 x D8",
        },
        "sources": {
            "export": {
                "path": str(EXPORT.relative_to(REPOSITORY)),
                "sha256": sha256(EXPORT),
            },
            "h7_document": {
                "path": str(H7_DOCUMENT.relative_to(REPOSITORY)),
                "sha256": sha256(H7_DOCUMENT),
            },
            "h7_module": {
                "path": "src/python/h7_c2_3_d8.py",
                "sha256": sha256(PYTHON_SOURCES / "h7_c2_3_d8.py"),
            },
            "exact_invariants": {
                "path": "src/python/exact_invariants.py",
                "sha256": sha256(PYTHON_SOURCES / "exact_invariants.py"),
            },
            "producer": {
                "path": str(producer.relative_to(REPOSITORY)),
                "sha256": sha256(producer),
            },
        },
        "character_count": len(characters),
        "exact_omega_distribution": {
            str(omega): count for omega, count in observed.items()
        },
        "omega_eight_count": distribution[8],
        "omega_nine_count": distribution[9],
        "h7_scalar_good_count": len(h7_good),
        "h7_affine_good_count": len(affine_good),
        "target9_good_count": len(target9_good_tuple),
        "target10_good_count": len(target10_good_tuple),
        "h7_scalar_good_indices_sha256": index_sha256(h7_good),
        "h7_affine_good_indices_sha256": index_sha256(affine_good),
        "target9_good_indices_sha256": index_sha256(target9_good_tuple),
        "target10_good_indices_sha256": index_sha256(target10_good_tuple),
        "target9_boundary_count": len(boundary_records),
        "target9_boundary_records": boundary_records,
    }


def verify_saved_certificate(path: Path = DEFAULT_OUTPUT) -> dict[str, object]:
    saved = json.loads(path.read_text(encoding="utf-8"))
    rebuilt = build_certificate()
    if saved != rebuilt:
        raise AssertionError("saved SG261 target-nine scalar bridge changed")
    for record in saved["target9_boundary_records"]:
        if len(record["nine_clique"]) != 9:
            raise AssertionError("saved SG261 boundary witness has wrong size")
    return saved


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        saved = verify_saved_certificate(args.output)
        print(
            "verified characters=%d good=%d boundary=%d"
            % (
                saved["character_count"],
                saved["target9_good_count"],
                saved["target9_boundary_count"],
            )
        )
        return
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "wrote %s characters=%d distribution=%r boundary=%d"
        % (
            args.output,
            certificate["character_count"],
            certificate["exact_omega_distribution"],
            certificate["target9_boundary_count"],
        )
    )


if __name__ == "__main__":
    main()
