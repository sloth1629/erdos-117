#!/usr/bin/env python3
"""Exact target-ten restriction census for ``SmallGroup(64,261)``.

This is a deliberately local certificate for the index-two quotient
``SmallGroup(128,2320) = C2^4 x D8``.  It classifies the action-invariant
odd-containing character subgroups on its canonical index-two subgroup
``SmallGroup(64,261) = C2^3 x D8``.  It does not enumerate arbitrary groups
or arbitrary quotients of order 128.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter, deque
from functools import reduce
from pathlib import Path
from typing import Iterable, Sequence


REPOSITORY = Path(__file__).resolve().parents[2]
PYTHON_SOURCES = REPOSITORY / "src" / "python"
if str(REPOSITORY) not in sys.path:
    sys.path.insert(0, str(REPOSITORY))
if str(PYTHON_SOURCES) not in sys.path:
    sys.path.insert(0, str(PYTHON_SOURCES))

import h7_c2_3_d8 as sg261  # noqa: E402
from exact_invariants import maximum_clique, verify_clique  # noqa: E402
from src.verification.verify_h8_sg261_target9_scalar_bridge import (  # noqa: E402
    verify_saved_certificate as verify_scalar_bridge,
)


H7_EXPORT = REPOSITORY / "experiments" / "logs" / "h7_c2_3_d8.tsv"
H7_DOCUMENT = REPOSITORY / "experiments" / "logs" / "h7_c2_3_d8.json"
SCALAR_BRIDGE = (
    REPOSITORY / "experiments" / "logs" / "h8_sg261_target9_scalar_bridge.json"
)
SPECIAL_EXPORT = (
    REPOSITORY / "experiments" / "logs" / "h9_sg261_special_data.tsv"
)
SPECIAL_GAP_SOURCE = (
    REPOSITORY / "experiments" / "configs" / "h9_sg261_special_export.g"
)
SPECIAL_GAP_STDOUT = (
    REPOSITORY
    / "experiments"
    / "logs"
    / "h9_sg261_special_data_gap.stdout.txt"
)
DEFAULT_OUTPUT = (
    REPOSITORY
    / "experiments"
    / "logs"
    / "h9_sg261_target10_restrictions.json"
)

EXPECTED_RADICAL_DISTRIBUTION = {1: 22641, 2: 3486, 4: 252, 8: 8}
EXPECTED_JOINT_SIGNATURES = {(5, 8): 8, (6, 4): 56, (9, 4): 140}
EXPECTED_AUTOMORPHISM_ORBIT_SIZES = (8, 28, 56, 112)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def adjacency_sha256(adjacency: Sequence[int]) -> str:
    payload = b"".join(int(mask).to_bytes(8, "little") for mask in adjacency)
    return hashlib.sha256(payload).hexdigest()


def _parse_special_export(
    path: Path,
) -> tuple[dict[str, str], tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    """Parse the independent GAP abelianization/automorphism export."""

    metadata: dict[str, str] = {}
    abelianization: list[tuple[int, ...]] = []
    automorphisms: list[tuple[int, ...]] = []
    section = "metadata"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            if key in metadata:
                raise AssertionError("duplicate SG261 special-export metadata")
            metadata[key] = value
        elif line == "ABELIANIZATION":
            if section != "metadata":
                raise AssertionError("misplaced abelianization section")
            section = "abelianization_header"
        elif line == "AUTOMORPHISMS":
            if section != "abelianization":
                raise AssertionError("misplaced automorphism section")
            section = "automorphisms_header"
        elif not line:
            continue
        elif section == "abelianization_header":
            if line != "vertex\tcoordinates":
                raise AssertionError("wrong abelianization header")
            section = "abelianization"
        elif section == "abelianization":
            raw_vertex, raw_coordinates = line.split("\t")
            if int(raw_vertex) != len(abelianization):
                raise AssertionError("incomplete abelianization vertices")
            coordinates = tuple(int(value) for value in raw_coordinates.split(","))
            if len(coordinates) != 5 or any(value not in (0, 1) for value in coordinates):
                raise AssertionError("invalid SG261 abelianization coordinates")
            abelianization.append(coordinates)
        elif section == "automorphisms_header":
            if line != "generator\tpermutation":
                raise AssertionError("wrong automorphism header")
            section = "automorphisms"
        elif section == "automorphisms":
            raw_generator, raw_permutation = line.split("\t")
            if int(raw_generator) != len(automorphisms) + 1:
                raise AssertionError("incomplete automorphism generators")
            permutation = tuple(int(value) for value in raw_permutation.split(","))
            if sorted(permutation) != list(range(64)):
                raise AssertionError("invalid SG261 automorphism permutation")
            automorphisms.append(permutation)
        else:
            raise AssertionError("data outside SG261 special-export section")

    expected_metadata = {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "Q_ORDER": "64",
        "Q_ID": "261",
        "STRUCTURE": "C2 x C2 x C2 x D8",
        "DERIVED_ORDER": "2",
        "ABELIANIZATION_ORDER": "32",
        "ABELIANIZATION_RELATIVE_ORDERS": "2,2,2,2,2",
        "AUTOMORPHISM_GROUP_ORDER": "688128",
        "AUTOMORPHISM_GENERATOR_COUNT": "2",
    }
    if metadata != expected_metadata:
        raise AssertionError("unexpected SG261 special-export metadata")
    if len(abelianization) != 64 or len(automorphisms) != 2:
        raise AssertionError("incomplete SG261 special export")
    if tuple(index for index, value in enumerate(abelianization) if not any(value)) != (0, 6):
        raise AssertionError("SG261 derived subgroup vertices changed")
    return metadata, tuple(abelianization), tuple(automorphisms)


def _character_action_maps(
    parsed: dict[str, object],
    characters: Sequence[tuple[int, ...]],
) -> tuple[tuple[int, ...], ...]:
    orders = parsed["exterior_orders"]
    indices = {character: index for index, character in enumerate(characters)}
    mappings = []
    for images, _ in parsed["actions"]:
        mapping = []
        for character in characters:
            result = []
            for source_order, image in zip(orders, images):
                value = sg261._character_value(character, image, orders)
                step = 4 // source_order
                if value % step:
                    raise AssertionError("action pullback is not a character")
                result.append((value // step) % source_order)
            mapping.append(indices[tuple(result)])
        if len(set(mapping)) != len(characters):
            raise AssertionError("character action is not bijective")
        mappings.append(tuple(mapping))
    return tuple(mappings)


def _transport_adjacency(
    adjacency: Sequence[int], permutation: Sequence[int],
) -> tuple[int, ...]:
    transported = [0] * len(adjacency)
    for source, mask in enumerate(adjacency):
        target_mask = 0
        remaining = int(mask)
        while remaining:
            bit = remaining & -remaining
            neighbor = bit.bit_length() - 1
            target_mask |= 1 << permutation[neighbor]
            remaining ^= bit
        transported[permutation[source]] = target_mask
    return tuple(transported)


def _automorphism_orbits(
    retained: dict[tuple[int, ...], dict[str, object]],
    generators: Sequence[Sequence[int]],
) -> list[dict[str, object]]:
    unseen = set(retained)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {representative}
        queue = deque([representative])
        while queue:
            adjacency = queue.popleft()
            for generator in generators:
                image = _transport_adjacency(adjacency, generator)
                if image not in retained:
                    raise AssertionError("automorphism leaves retained graph family")
                if image not in orbit:
                    orbit.add(image)
                    queue.append(image)
        unseen -= orbit
        signatures = {
            (int(retained[adjacency]["omega"]), len(retained[adjacency]["radical"]))
            for adjacency in orbit
        }
        if len(signatures) != 1:
            raise AssertionError("automorphism orbit changes graph signature")
        omega, radical_size = signatures.pop()
        orbits.append(
            {
                "size": len(orbit),
                "omega": omega,
                "radical_size": radical_size,
                "representative_adjacency_sha256": adjacency_sha256(representative),
            }
        )
    orbits.sort(key=lambda record: (record["size"], record["omega"], record["representative_adjacency_sha256"]))
    return orbits


def _joint_signature_records(counter: Counter[tuple[int, int]]) -> list[dict[str, int]]:
    return [
        {"omega": omega, "radical_size": radical_size, "count": count}
        for (omega, radical_size), count in sorted(counter.items())
    ]


def build_certificate() -> dict[str, object]:
    """Rebuild the complete local restriction certificate."""

    h7_document = json.loads(H7_DOCUMENT.read_text(encoding="utf-8"))
    h7_certificate = h7_document["certificate"]
    # Recheck every saved h7 subgroup witness before changing the cutoff.
    sg261.verify_certificate(h7_certificate, H7_EXPORT)
    scalar_bridge = verify_scalar_bridge(SCALAR_BRIDGE)
    if scalar_bridge["target10_good_count"] != 1152:
        raise AssertionError("SG261 target-ten scalar bridge changed")

    parsed = sg261.parse_export(H7_EXPORT)
    orders = tuple(parsed["exterior_orders"])
    characters = tuple(itertools.product(*(range(order) for order in orders)))
    indices = {character: index for index, character in enumerate(characters)}
    scalar_graphs = tuple(
        sg261._scalar_graph(character, parsed["commutators"], orders)
        for character in characters
    )
    action_maps = _character_action_maps(parsed, characters)

    odd_base = tuple(h7_certificate["odd_base_character"])
    double_base = int(h7_certificate["twice_odd_base_code"])
    complement = tuple(int(value) for value in h7_certificate["affine_coordinate_basis"])[1:]

    def hchar(code: int) -> tuple[int, ...]:
        return tuple((code >> index) & 1 for index in range(9)) + (
            2 * ((code >> 9) & 1),
        )

    def lift(value: int) -> int:
        result = 0
        for index, vector in enumerate(complement):
            if value & (1 << index):
                result ^= vector
        return result

    seen_subgroups = set()
    radical_distribution: Counter[int] = Counter()
    outcome_distribution: Counter[str] = Counter()
    joint_signatures: Counter[tuple[int, int]] = Counter()
    boundary_records = []
    retained_records = []
    retained_by_adjacency: dict[tuple[int, ...], dict[str, object]] = {}
    faithful_boundary_count = 0
    nonfaithful_boundary_count = 0

    for expected_serial, source_record in enumerate(h7_certificate["subgroup_records"], 1):
        if source_record["serial"] != expected_serial:
            raise AssertionError("incomplete SG261 source serials")
        quotient_basis = tuple(source_record["quotient_subspace_rref_basis"])
        representative = int(source_record["odd_coset_representative"])
        m_codes = sg261._binary_span(
            (double_base,) + tuple(lift(row) for row in quotient_basis)
        )
        shift = sg261._add(odd_base, hchar(lift(representative)), orders)
        subgroup = frozenset(
            {indices[hchar(code)] for code in m_codes}
            | {
                indices[sg261._add(shift, hchar(code), orders)]
                for code in m_codes
            }
        )
        if subgroup in seen_subgroups or len(subgroup) != source_record["subgroup_order"]:
            raise AssertionError("invalid SG261 affine subgroup reconstruction")
        seen_subgroups.add(subgroup)
        for mapping in action_maps:
            if frozenset(mapping[index] for index in subgroup) != subgroup:
                raise AssertionError("SG261 affine subgroup is not action invariant")

        adjacency = tuple(
            reduce(int.__or__, (scalar_graphs[index][vertex] for index in subgroup), 0)
            for vertex in range(64)
        )
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if not mask)
        radical_distribution[len(radical)] += 1
        ten_clique = sg261._greedy_target_clique(adjacency, 10)
        if not ten_clique:
            exact = maximum_clique(adjacency)
            if exact.size >= 10:
                ten_clique = tuple(exact.vertices[:10])
            else:
                if not verify_clique(adjacency, exact.vertices):
                    raise AssertionError("invalid retained exact clique")
                record = {
                    "serial": expected_serial,
                    "quotient_subspace_rref_basis": list(quotient_basis),
                    "odd_coset_representative": representative,
                    "subgroup_order": len(subgroup),
                    "omega": exact.size,
                    "radical": list(radical),
                    "clique": list(exact.vertices),
                    "adjacency": list(adjacency),
                    "adjacency_sha256": adjacency_sha256(adjacency),
                }
                if adjacency in retained_by_adjacency:
                    raise AssertionError("duplicate retained SG261 adjacency")
                retained_by_adjacency[adjacency] = record
                retained_records.append(record)
                outcome_distribution[str(exact.size)] += 1
                joint_signatures[(exact.size, len(radical))] += 1
                continue

        if len(ten_clique) != 10 or not verify_clique(adjacency, ten_clique):
            raise AssertionError("invalid SG261 subgroup K10")
        faithful = radical == (0,)
        faithful_boundary_count += int(faithful)
        nonfaithful_boundary_count += int(not faithful)
        outcome_distribution[">=10"] += 1
        boundary_records.append(
            {
                "serial": expected_serial,
                "subgroup_order": len(subgroup),
                "faithful": faithful,
                "ten_clique": list(ten_clique),
            }
        )

    if len(seen_subgroups) != 26387:
        raise AssertionError("incomplete SG261 affine subgroup census")
    if dict(sorted(radical_distribution.items())) != EXPECTED_RADICAL_DISTRIBUTION:
        raise AssertionError("SG261 radical distribution changed")
    if dict(joint_signatures) != EXPECTED_JOINT_SIGNATURES:
        raise AssertionError("SG261 retained joint signatures changed")
    if len(boundary_records) != 26183 or faithful_boundary_count != 22641 or nonfaithful_boundary_count != 3542:
        raise AssertionError("SG261 target-ten boundary counts changed")
    if len(retained_records) != 204 or len(retained_by_adjacency) != 204:
        raise AssertionError("SG261 retained graph count changed")

    special_metadata, abelianization, automorphism_generators = _parse_special_export(
        SPECIAL_EXPORT
    )
    automorphism_orbits = _automorphism_orbits(
        retained_by_adjacency, automorphism_generators
    )
    if tuple(sorted(record["size"] for record in automorphism_orbits)) != EXPECTED_AUTOMORPHISM_ORBIT_SIZES:
        raise AssertionError("SG261 retained automorphism orbits changed")

    # Exact all-even obstruction.  The first exported conjugation sends the
    # pc element 010000 to 010001, whose quotient is the nonidentity element
    # 000001 (vertex 6).  Thus vertex 6 is a commutator and lies in Q0'.
    q_exponents = tuple(parsed["q_exponents"])
    first_conjugation = parsed["actions"][0][1]
    if (
        q_exponents[2] != (0, 1, 0, 0, 0, 0)
        or first_conjugation[2] != 15
        or q_exponents[15] != (0, 1, 0, 0, 0, 1)
        or q_exponents[6] != (0, 0, 0, 0, 0, 1)
        or abelianization[6] != (0, 0, 0, 0, 0)
    ):
        raise AssertionError("SG261 derived-vertex obstruction changed")
    obstruction_values = set(parsed["commutators"][6])
    twice_c4 = (0,) * 9 + (2,)
    if obstruction_values != {(0,) * 10, twice_c4}:
        raise AssertionError("SG261 all-even commutator obstruction changed")
    even_characters = tuple(character for character in characters if character[-1] % 2 == 0)
    if len(even_characters) != 1024 or any(
        sg261._character_value(character, twice_c4, orders)
        for character in even_characters
    ):
        raise AssertionError("an all-even character detects the obstruction vertex")

    producer = Path(__file__).resolve()
    return {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "scope": (
            "SmallGroup(64,261) restrictions for the SmallGroup(128,2320) "
            "index-two branch only; not a census of all order-128 quotients"
        ),
        "claim": (
            "All 26,387 action-invariant odd-containing target-ten scalar "
            "subgroups are reconstructed.  Exactly 26,183 carry saved K10 "
            "witnesses; the 204 remaining nonfaithful graphs have joint "
            "(omega,radical-size) signatures 8*(5,8), 56*(6,4), 140*(9,4)."
        ),
        "sources": {
            "h7_export": {"path": str(H7_EXPORT.relative_to(REPOSITORY)), "sha256": sha256(H7_EXPORT)},
            "h7_document": {"path": str(H7_DOCUMENT.relative_to(REPOSITORY)), "sha256": sha256(H7_DOCUMENT)},
            "scalar_bridge": {"path": str(SCALAR_BRIDGE.relative_to(REPOSITORY)), "sha256": sha256(SCALAR_BRIDGE)},
            "special_gap_source": {"path": str(SPECIAL_GAP_SOURCE.relative_to(REPOSITORY)), "sha256": sha256(SPECIAL_GAP_SOURCE)},
            "special_gap_export": {"path": str(SPECIAL_EXPORT.relative_to(REPOSITORY)), "sha256": sha256(SPECIAL_EXPORT)},
            "special_gap_stdout": {"path": str(SPECIAL_GAP_STDOUT.relative_to(REPOSITORY)), "sha256": sha256(SPECIAL_GAP_STDOUT)},
            "h7_module": {"path": "src/python/h7_c2_3_d8.py", "sha256": sha256(PYTHON_SOURCES / "h7_c2_3_d8.py")},
            "exact_invariants": {"path": "src/python/exact_invariants.py", "sha256": sha256(PYTHON_SOURCES / "exact_invariants.py")},
            "producer": {"path": str(producer.relative_to(REPOSITORY)), "sha256": sha256(producer)},
        },
        "scalar_target10_good_count": scalar_bridge["target10_good_count"],
        "odd_containing_invariant_subgroup_count": len(seen_subgroups),
        "action_invariance_checked_subgroup_count": len(seen_subgroups),
        "radical_size_distribution": {str(key): value for key, value in sorted(radical_distribution.items())},
        "target10_outcome_distribution": dict(sorted(outcome_distribution.items())),
        "target10_boundary_count": len(boundary_records),
        "faithful_boundary_count": faithful_boundary_count,
        "nonfaithful_boundary_count": nonfaithful_boundary_count,
        "retained_count": len(retained_records),
        "retained_distinct_adjacency_count": len(retained_by_adjacency),
        "retained_joint_signature_distribution": _joint_signature_records(joint_signatures),
        "retained_automorphism_orbits": automorphism_orbits,
        "all_even_extension_obstruction": {
            "status": "[PROVED] from the exact exported group facts below",
            "reason": (
                "vertex 6 lies in Q0', so every cross homomorphism Q0->C2 "
                "annihilates it; every all-even restriction also has vertex 6 "
                "in its radical, contradicting exactness of an extension"
            ),
            "source_vertex": 2,
            "source_pc_exponents": list(q_exponents[2]),
            "first_conjugation_image_vertex": first_conjugation[2],
            "image_pc_exponents": list(q_exponents[15]),
            "derived_vertex": 6,
            "derived_vertex_pc_exponents": list(q_exponents[6]),
            "derived_vertex_abelianization_coordinates": list(abelianization[6]),
            "derived_subgroup_vertices": [0, 6],
            "all_even_character_count": len(even_characters),
            "restriction_commutator_values": [list(value) for value in sorted(obstruction_values)],
        },
        "special_export_metadata": special_metadata,
        "boundary_records": boundary_records,
        "retained_records": retained_records,
    }


def verify_saved_certificate(path: Path = DEFAULT_OUTPUT) -> dict[str, object]:
    saved = json.loads(path.read_text(encoding="utf-8"))
    rebuilt = build_certificate()
    if saved != rebuilt:
        raise AssertionError("saved SG261 target-ten restriction certificate changed")
    return saved


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        certificate = verify_saved_certificate(args.output)
        print(
            "verified subgroups=%d boundary=%d retained=%d signatures=%r"
            % (
                certificate["odd_containing_invariant_subgroup_count"],
                certificate["target10_boundary_count"],
                certificate["retained_count"],
                certificate["retained_joint_signature_distribution"],
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
        "wrote %s subgroups=%d boundary=%d retained=%d signatures=%r"
        % (
            args.output,
            certificate["odd_containing_invariant_subgroup_count"],
            certificate["target10_boundary_count"],
            certificate["retained_count"],
            certificate["retained_joint_signature_distribution"],
        )
    )


if __name__ == "__main__":
    main()
