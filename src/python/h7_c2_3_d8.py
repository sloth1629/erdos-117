#!/usr/bin/env python3
"""Exact affine-dual cutoff-seven certificate for ``C2^3 x D8``.

The nonabelian exterior square of ``SmallGroup(64,261)`` is abelian of type
``C2^9 x C4``.  Instead of enumerating its very large subgroup lattice, this
module works in the character group.  A normal exterior kernel ``K`` is
equivalent to its action-invariant annihilator ``L = K^perp``.  The graph for
``L`` is the union of the scalar character graphs for characters in ``L``.

At clique cutoff seven the good characters have a particularly rigid form:
all 1,024 even characters together with an affine 7-space of 128 odd
characters.  Every faithful eligible ``L`` contains an odd character and is
therefore parametrized exactly by a subspace of ``F_2^6`` and one quotient
coset.  The resulting 26,387 cases are small enough to certify directly.
"""

from __future__ import annotations

import csv
import itertools
from collections import Counter
from functools import reduce
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from exact_invariants import (
    exact_chromatic_number,
    maximum_clique,
    verify_clique,
    verify_coloring,
)


Vector = Tuple[int, ...]
Adjacency = Tuple[int, ...]


def _parse_vector(raw: str) -> Vector:
    return tuple(int(value) for value in raw.split(",") if value != "")


def _parse_vector_list(raw: str) -> Tuple[Vector, ...]:
    return tuple(_parse_vector(value) for value in raw.split(";"))


def parse_export(path: Path) -> Dict[str, object]:
    """Parse and structurally validate the canonical GAP export."""

    metadata: Dict[str, str] = {}
    action_lines: List[str] = []
    commutator_lines: List[str] = []
    section = "metadata"
    action_header = None
    commutator_header = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            if key in metadata:
                raise AssertionError("duplicate export metadata")
            metadata[key] = value
        elif line == "ACTIONS":
            if section != "metadata":
                raise AssertionError("misplaced action section")
            section = "actions_header"
        elif line == "COMMUTATORS":
            if section not in ("actions", "actions_header"):
                raise AssertionError("misplaced commutator section")
            section = "commutators_header"
        elif line:
            if section == "actions_header":
                action_header = line
                section = "actions"
            elif section == "actions":
                action_lines.append(line)
            elif section == "commutators_header":
                commutator_header = line
                section = "commutators"
            elif section == "commutators":
                commutator_lines.append(line)
            else:
                raise AssertionError("data outside an export section")

    expected_metadata = {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "Q_ORDER": "64",
        "Q_ID": "261",
        "STRUCTURE": "C2 x C2 x C2 x D8",
        "Q_PC_RELATIVE_ORDERS": "2,2,2,2,2,2",
        "COVER_ORDER": "65536",
        "PC_CONVERSION_KERNEL_ORDER": "1",
        "COVER_TO_Q_KERNEL_ORDER": "1024",
        "EXTERIOR_ORDER": "2048",
        "EXTERIOR_RELATIVE_ORDERS": "2,2,2,2,2,2,2,2,2,4",
        "ACTION_COUNT": "16",
        "COMMUTATOR_ROW_COUNT": "64",
    }
    if metadata != expected_metadata:
        raise AssertionError("unexpected SG(64,261) export metadata")
    if action_header != "action_index\timage_vectors\tq_conjugation":
        raise AssertionError("wrong action header")
    if commutator_header != "vertex\tq_exponents\tcommutator_vectors":
        raise AssertionError("wrong commutator header")

    exterior_orders = _parse_vector(metadata["EXTERIOR_RELATIVE_ORDERS"])
    q_orders = _parse_vector(metadata["Q_PC_RELATIVE_ORDERS"])
    if exterior_orders != (2,) * 9 + (4,) or q_orders != (2,) * 6:
        raise AssertionError("unexpected coordinate groups")

    actions = []
    for expected_index, line in enumerate(action_lines, 1):
        fields = line.split("\t")
        if len(fields) != 3 or int(fields[0]) != expected_index:
            raise AssertionError("incomplete action serials")
        images = _parse_vector_list(fields[1])
        permutation = tuple(int(value) for value in fields[2].split(","))
        if len(images) != 10 or any(len(vector) != 10 for vector in images):
            raise AssertionError("wrong action-matrix shape")
        if any(
            not 0 <= value < order
            for vector in images
            for value, order in zip(vector, exterior_orders)
        ):
            raise AssertionError("action coordinate out of range")
        if sorted(permutation) != list(range(64)):
            raise AssertionError("invalid quotient conjugation permutation")
        actions.append((images, permutation))
    if len(actions) != int(metadata["ACTION_COUNT"]):
        raise AssertionError("wrong action count")

    q_exponents = []
    commutators = []
    for expected_vertex, line in enumerate(commutator_lines):
        fields = line.split("\t")
        if len(fields) != 3 or int(fields[0]) != expected_vertex:
            raise AssertionError("incomplete commutator row serials")
        exponents = _parse_vector(fields[1])
        row = _parse_vector_list(fields[2])
        if len(exponents) != 6 or any(
            not 0 <= value < order for value, order in zip(exponents, q_orders)
        ):
            raise AssertionError("invalid quotient exponent vector")
        if len(row) != 64 or any(len(vector) != 10 for vector in row):
            raise AssertionError("wrong commutator-table shape")
        if any(
            not 0 <= value < order
            for vector in row
            for value, order in zip(vector, exterior_orders)
        ):
            raise AssertionError("commutator coordinate out of range")
        q_exponents.append(exponents)
        commutators.append(row)
    if len(commutators) != int(metadata["COMMUTATOR_ROW_COUNT"]):
        raise AssertionError("wrong commutator row count")
    if len(set(q_exponents)) != 64 or set(q_exponents) != set(
        itertools.product(*(range(order) for order in q_orders))
    ):
        raise AssertionError("quotient pc exponent enumeration is incomplete")

    parsed = {
        "metadata": metadata,
        "q_orders": q_orders,
        "exterior_orders": exterior_orders,
        "q_exponents": tuple(q_exponents),
        "actions": tuple(actions),
        "commutators": tuple(tuple(row) for row in commutators),
    }
    _validate_export_algebra(parsed)
    return parsed


def _add(left: Vector, right: Vector, orders: Vector) -> Vector:
    return tuple((a + b) % order for a, b, order in zip(left, right, orders))


def _negate(value: Vector, orders: Vector) -> Vector:
    return tuple((-entry) % order for entry, order in zip(value, orders))


def _generated_subgroup(generators: Iterable[Vector], orders: Vector):
    zero = (0,) * len(orders)
    subgroup = {zero}
    for generator in generators:
        if generator in subgroup:
            continue
        cyclic = [zero]
        current = generator
        while current != zero:
            cyclic.append(current)
            current = _add(current, generator, orders)
        subgroup = {
            _add(left, right, orders) for left in subgroup for right in cyclic
        }
    return frozenset(subgroup)


def _action_image(value: Vector, images: Sequence[Vector], orders: Vector) -> Vector:
    result = (0,) * len(orders)
    for coefficient, image in zip(value, images):
        for _ in range(coefficient):
            result = _add(result, image, orders)
    return result


def _validate_export_algebra(parsed: Dict[str, object]) -> None:
    orders = parsed["exterior_orders"]
    commutators = parsed["commutators"]
    actions = parsed["actions"]
    q_exponents = parsed["q_exponents"]
    zero = (0,) * len(orders)
    identity_vertex = q_exponents.index((0,) * 6)
    if identity_vertex != 0:
        raise AssertionError("canonical quotient element order does not start at identity")
    for left in range(64):
        if commutators[left][left] != zero:
            raise AssertionError("nonzero commutator diagonal")
        for right in range(64):
            if commutators[right][left] != _negate(commutators[left][right], orders):
                raise AssertionError("commutator table is not skew-symmetric")
    if len(_generated_subgroup(
        (commutators[left][right] for left in range(64) for right in range(64)),
        orders,
    )) != 2048:
        raise AssertionError("lifted commutators do not generate the exterior square")

    elements = tuple(itertools.product(*(range(order) for order in orders)))
    for images, permutation in actions:
        action_lookup = {
            value: _action_image(value, images, orders) for value in elements
        }
        if len(set(action_lookup.values())) != 2048:
            raise AssertionError("cover conjugation is not an exterior automorphism")
        if permutation[identity_vertex] != identity_vertex:
            raise AssertionError("quotient conjugation moves the identity")
        for left in range(64):
            for right in range(64):
                if action_lookup[commutators[left][right]] != (
                    commutators[permutation[left]][permutation[right]]
                ):
                    raise AssertionError("action does not transport lifted commutators")


def _character_value(character: Vector, element: Vector, orders: Vector) -> int:
    """Evaluate a character in the common target ``Z/4Z``."""

    return sum(
        coefficient * exponent * (4 // order)
        for coefficient, exponent, order in zip(character, element, orders)
    ) % 4


def _scalar_graph(
    character: Vector, commutators: Sequence[Sequence[Vector]], orders: Vector,
) -> Adjacency:
    adjacency = tuple(
        sum(
            1 << right
            for right, element in enumerate(row)
            if left != right and _character_value(character, element, orders)
        )
        for left, row in enumerate(commutators)
    )
    for left, mask in enumerate(adjacency):
        if mask & (1 << left):
            raise AssertionError("scalar graph has a loop")
        for right in range(64):
            if bool(mask & (1 << right)) != bool(adjacency[right] & (1 << left)):
                raise AssertionError("scalar graph is asymmetric")
    return adjacency


def _greedy_target_clique(adjacency: Adjacency, target: int = 8) -> Tuple[int, ...]:
    starts = sorted(
        range(len(adjacency)),
        key=lambda vertex: (-bin(adjacency[vertex]).count("1"), vertex),
    )
    for start in starts:
        clique = [start]
        candidates = adjacency[start]
        while candidates and len(clique) < target:
            choices = [
                vertex for vertex in range(len(adjacency))
                if candidates & (1 << vertex)
            ]
            vertex = min(
                choices,
                key=lambda value: (
                    -bin(candidates & adjacency[value]).count("1"), value
                ),
            )
            clique.append(vertex)
            candidates &= adjacency[vertex]
        if len(clique) == target:
            return tuple(clique)
    return ()


def _binary_rref(values: Iterable[int], dimension: int) -> Tuple[int, ...]:
    rows = sorted(set(value for value in values if value))
    pivot_row = 0
    for bit in range(dimension):
        pivot = next(
            (index for index in range(pivot_row, len(rows)) if rows[index] & (1 << bit)),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        for index in range(len(rows)):
            if index != pivot_row and rows[index] & (1 << bit):
                rows[index] ^= rows[pivot_row]
        pivot_row += 1
    rows = [value for value in rows if value]
    rows.sort(key=lambda value: ((value & -value).bit_length(), value))
    return tuple(rows)


def _binary_span(basis: Sequence[int]):
    result = {0}
    for vector in basis:
        result |= {value ^ vector for value in tuple(result)}
    return frozenset(result)


def _rref_subspace_bases(dimension: int):
    """Yield every binary RREF row space in ``F_2^dimension`` exactly once."""

    for rank in range(dimension + 1):
        for pivots in itertools.combinations(range(dimension), rank):
            pivot_set = set(pivots)
            free_positions = [
                (row, column)
                for row, pivot in enumerate(pivots)
                for column in range(pivot + 1, dimension)
                if column not in pivot_set
            ]
            for bits in range(1 << len(free_positions)):
                rows = [1 << pivot for pivot in pivots]
                for index, (row, column) in enumerate(free_positions):
                    if bits & (1 << index):
                        rows[row] |= 1 << column
                yield tuple(rows)


def _coset_representatives(basis: Sequence[int], dimension: int) -> Tuple[int, ...]:
    subspace = _binary_span(basis)
    covered = set()
    representatives = []
    for value in range(1 << dimension):
        if value not in covered:
            representatives.append(value)
            covered |= {value ^ member for member in subspace}
    if len(covered) != 1 << dimension:
        raise AssertionError("binary cosets are incomplete")
    return tuple(representatives)


def exact_certificate(export_path: Path) -> Dict[str, object]:
    """Recompute the complete affine-dual certificate from the GAP export."""

    parsed = parse_export(export_path)
    metadata = parsed["metadata"]
    orders = parsed["exterior_orders"]
    commutators = parsed["commutators"]
    actions = parsed["actions"]
    q_exponents = parsed["q_exponents"]
    identity_vertex = q_exponents.index((0,) * 6)

    characters = tuple(itertools.product(*(range(order) for order in orders)))
    character_indices = {character: index for index, character in enumerate(characters)}

    def character_add(left: Vector, right: Vector) -> Vector:
        return _add(left, right, orders)

    scalar_graphs = tuple(
        _scalar_graph(character, commutators, orders) for character in characters
    )
    good = {0}
    scalar_status = Counter()
    scalar_records = []
    for index in range(1, len(characters)):
        adjacency = scalar_graphs[index]
        witness = _greedy_target_clique(adjacency)
        if witness:
            if not verify_clique(adjacency, witness):
                raise AssertionError("invalid scalar eight-clique")
            status = "clique_ge_8"
            scalar_status[status] += 1
            record = {
                "character_index": index,
                "character": list(characters[index]),
                "status": status,
                "witness": list(witness),
            }
        else:
            clique = maximum_clique(adjacency)
            if clique.size >= 8 or not verify_clique(adjacency, clique.vertices):
                raise AssertionError("scalar exact cutoff search failed")
            status = "omega_%d" % clique.size
            scalar_status[status] += 1
            good.add(index)
            record = {
                "character_index": index,
                "character": list(characters[index]),
                "status": status,
                "omega": clique.size,
                "witness": list(clique.vertices),
                "search_nodes": clique.search_nodes,
            }
        scalar_records.append(record)

    odd_good = {index for index in good if characters[index][-1] % 2 == 1}
    even_good = good - odd_good
    all_even = {index for index, character in enumerate(characters) if character[-1] % 2 == 0}
    if good != all_even | odd_good or even_good != all_even:
        raise AssertionError("good-character parity decomposition failed")
    if (len(good), len(even_good), len(odd_good)) != (1152, 1024, 128):
        raise AssertionError("unexpected good-character counts")

    def hcode(character: Vector) -> int:
        if character[-1] not in (0, 2):
            raise AssertionError("H-code requires an even character")
        return sum(character[index] << index for index in range(9)) | (
            (character[-1] // 2) << 9
        )

    def hchar(code: int) -> Vector:
        return tuple((code >> index) & 1 for index in range(9)) + (
            2 * ((code >> 9) & 1),
        )

    odd_base_index = min(odd_good)
    odd_base = characters[odd_base_index]
    odd_base_inverse = _negate(odd_base, orders)
    odd_difference_codes = {
        hcode(character_add(characters[index], odd_base_inverse))
        for index in odd_good
    }
    difference_basis = _binary_rref(odd_difference_codes, 10)
    if len(difference_basis) != 7 or _binary_span(difference_basis) != odd_difference_codes:
        raise AssertionError("odd good characters are not an affine 7-space")
    double_base_code = hcode(character_add(odd_base, odd_base))
    if not double_base_code or double_base_code not in odd_difference_codes:
        raise AssertionError("twice the odd base is not in its difference space")

    affine_basis = [double_base_code]
    current_rank = 1
    for vector in difference_basis:
        trial = _binary_rref((*affine_basis, vector), 10)
        if len(trial) > current_rank:
            affine_basis.append(vector)
            current_rank += 1
    if current_rank != 7 or _binary_span(affine_basis) != odd_difference_codes:
        raise AssertionError("failed to split the affine difference space")
    complement = tuple(affine_basis[1:])

    def lift_quotient_vector(value: int) -> int:
        result = 0
        for index, vector in enumerate(complement):
            if value & (1 << index):
                result ^= vector
        return result

    def character_index_from_hcode(code: int) -> int:
        return character_indices[hchar(code)]

    def subgroup_character_indices(
        quotient_basis: Sequence[int], odd_representative: int,
    ):
        m_basis = (double_base_code,) + tuple(
            lift_quotient_vector(row) for row in quotient_basis
        )
        m_codes = _binary_span(m_basis)
        odd_shift = character_add(odd_base, hchar(lift_quotient_vector(odd_representative)))
        even = {character_index_from_hcode(code) for code in m_codes}
        odd = {
            character_indices[character_add(odd_shift, hchar(code))]
            for code in m_codes
        }
        subgroup = frozenset(even | odd)
        if len(subgroup) != 2 * len(m_codes) or not subgroup <= good:
            raise AssertionError("invalid affine subgroup reconstruction")
        return subgroup

    action_character_images = []
    for images, _ in actions:
        mapping = []
        for character in characters:
            result = []
            for source_order, image in zip(orders, images):
                value = _character_value(character, image, orders)
                step = 4 // source_order
                if value % step:
                    raise AssertionError("action pullback is not a character")
                result.append((value // step) % source_order)
            mapping.append(character_indices[tuple(result)])
        if len(set(mapping)) != 2048:
            raise AssertionError("character pullback is not bijective")
        action_character_images.append(tuple(mapping))

    rref_dimension_counts = Counter()
    weighted_dimension_counts = Counter()
    subgroup_status = Counter()
    status_by_order: Dict[int, Counter] = {}
    radical_size_distribution = Counter()
    unique_faithful_graphs = set()
    faithful_subgroup_count = 0
    candidate_records = []
    subgroup_records = []
    seen = set()
    serial = 0
    for quotient_basis in _rref_subspace_bases(6):
        dimension = len(quotient_basis)
        rref_dimension_counts[dimension] += 1
        representatives = _coset_representatives(quotient_basis, 6)
        weighted_dimension_counts[dimension] += len(representatives)
        for representative in representatives:
            serial += 1
            subgroup = subgroup_character_indices(quotient_basis, representative)
            if subgroup in seen:
                raise AssertionError("affine subgroup parametrization is not injective")
            seen.add(subgroup)
            for mapping in action_character_images:
                if {mapping[value] for value in subgroup} != set(subgroup):
                    raise AssertionError("eligible affine subgroup is not action invariant")

            adjacency = tuple(
                reduce(
                    int.__or__,
                    (scalar_graphs[value][vertex] for value in subgroup),
                    0,
                )
                for vertex in range(64)
            )
            radical = tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0)
            radical_size_distribution[len(radical)] += 1
            subgroup_order = len(subgroup)
            if radical == (identity_vertex,):
                faithful_subgroup_count += 1
                unique_faithful_graphs.add(adjacency)
            witness = _greedy_target_clique(adjacency)
            if witness:
                if not verify_clique(adjacency, witness):
                    raise AssertionError("invalid affine-subgroup eight-clique")
                status = "clique_ge_8"
            elif radical != (identity_vertex,):
                status = "nonfaithful_radical"
                witness = radical
            else:
                clique = maximum_clique(adjacency)
                coloring = exact_chromatic_number(adjacency, clique.size)
                if not verify_clique(adjacency, clique.vertices) or not verify_coloring(
                    adjacency, coloring.colors
                ):
                    raise AssertionError("invalid surviving exact graph certificate")
                status = "faithful_candidate"
                witness = clique.vertices
                candidate_records.append({
                    "serial": serial,
                    "nu": clique.size,
                    "a": coloring.size,
                    "clique": list(clique.vertices),
                    "coloring": list(coloring.colors),
                    "clique_search_nodes": clique.search_nodes,
                    "coloring_search_nodes_by_k": [
                        list(item) for item in coloring.search_nodes_by_k
                    ],
                })
            subgroup_status[status] += 1
            status_by_order.setdefault(subgroup_order, Counter())[status] += 1
            subgroup_records.append({
                "serial": serial,
                "quotient_subspace_rref_basis": list(quotient_basis),
                "odd_coset_representative": representative,
                "subgroup_order": subgroup_order,
                "status": status,
                "witness": list(witness),
            })

    if serial != 26387 or len(seen) != serial:
        raise AssertionError("affine subgroup enumeration is incomplete")
    if dict(subgroup_status) != {
        "nonfaithful_radical": 64,
        "clique_ge_8": 26323,
    } or candidate_records:
        raise AssertionError(
            "unexpected SG(64,261) cutoff-seven disposition: %r"
            % dict(subgroup_status)
        )
    if rref_dimension_counts != Counter({
        0: 1, 1: 63, 2: 651, 3: 1395, 4: 651, 5: 63, 6: 1,
    }):
        raise AssertionError("wrong binary subspace census")
    if weighted_dimension_counts != Counter({
        0: 64, 1: 2016, 2: 10416, 3: 11160, 4: 2604, 5: 126, 6: 1,
    }):
        raise AssertionError("wrong affine subgroup census")

    # This is the exact obstruction excluding every all-even L: vertex 6 has
    # all lifted commutators in {0, 2e_10}, and every even character kills
    # 2e_10.  Its quotient pc exponent vector certifies that it is nonidentity.
    twice_c4 = (0,) * 9 + (2,)
    all_even_obstruction_vertex = 6
    obstruction_values = set(commutators[all_even_obstruction_vertex])
    if obstruction_values != {(0,) * 10, twice_c4}:
        raise AssertionError("all-even radical obstruction changed")
    if not any(q_exponents[all_even_obstruction_vertex]):
        raise AssertionError("all-even obstruction vertex is the identity")
    if any(
        _character_value(characters[index], twice_c4, orders)
        for index in all_even
    ):
        raise AssertionError("an even character does not annihilate twice C4")

    return {
        "metadata": metadata,
        "identity_vertex": identity_vertex,
        "action_count": len(actions),
        "character_count": len(characters),
        "scalar_status_distribution": dict(sorted(scalar_status.items())),
        "scalar_records": scalar_records,
        "good_character_count": len(good),
        "even_good_character_count": len(even_good),
        "odd_good_character_count": len(odd_good),
        "odd_base_character_index": odd_base_index,
        "odd_base_character": list(odd_base),
        "odd_difference_dimension": len(difference_basis),
        "odd_difference_rref_basis": list(difference_basis),
        "twice_odd_base_code": double_base_code,
        "affine_coordinate_basis": list(affine_basis),
        "all_even_obstruction": {
            "quotient_vertex": all_even_obstruction_vertex,
            "quotient_pc_exponents": list(q_exponents[all_even_obstruction_vertex]),
            "commutator_values": [list(value) for value in sorted(obstruction_values)],
            "annihilated_nonzero_exterior_element": list(twice_c4),
        },
        "quotient_parameter_dimension": 6,
        "rref_subspace_count": sum(rref_dimension_counts.values()),
        "rref_subspace_dimension_distribution": {
            str(key): value for key, value in sorted(rref_dimension_counts.items())
        },
        "affine_subgroup_dimension_distribution": {
            str(key): value for key, value in sorted(weighted_dimension_counts.items())
        },
        "enumerated_odd_subgroup_count": serial,
        "action_invariant_odd_subgroup_count": serial,
        "subgroup_status_distribution": dict(sorted(subgroup_status.items())),
        "status_by_subgroup_order": {
            str(key): dict(sorted(value.items()))
            for key, value in sorted(status_by_order.items())
        },
        "radical_size_distribution": {
            str(key): value for key, value in sorted(radical_size_distribution.items())
        },
        "faithful_subgroup_count": faithful_subgroup_count,
        "unique_faithful_graph_count": len(unique_faithful_graphs),
        "faithful_candidate_count": len(candidate_records),
        "candidate_records": candidate_records,
        "subgroup_records": subgroup_records,
    }


def verify_certificate(certificate: Dict[str, object], export_path: Path) -> Dict[str, object]:
    """Reconstruct every saved affine subgroup witness independently."""

    parsed = parse_export(export_path)
    orders = parsed["exterior_orders"]
    commutators = parsed["commutators"]
    characters = tuple(itertools.product(*(range(order) for order in orders)))
    indices = {character: index for index, character in enumerate(characters)}
    scalar_graphs = tuple(
        _scalar_graph(character, commutators, orders) for character in characters
    )
    odd_base = tuple(certificate["odd_base_character"])
    double_base = int(certificate["twice_odd_base_code"])
    affine_basis = tuple(int(value) for value in certificate["affine_coordinate_basis"])
    complement = affine_basis[1:]

    def hchar(code: int) -> Vector:
        return tuple((code >> index) & 1 for index in range(9)) + (
            2 * ((code >> 9) & 1),
        )

    def lift(value: int) -> int:
        result = 0
        for index, vector in enumerate(complement):
            if value & (1 << index):
                result ^= vector
        return result

    statuses = Counter()
    faithful = 0
    seen = set()
    for expected_serial, record in enumerate(certificate["subgroup_records"], 1):
        if record["serial"] != expected_serial:
            raise AssertionError("saved SG261 subgroup serials are incomplete")
        quotient_basis = tuple(record["quotient_subspace_rref_basis"])
        representative = int(record["odd_coset_representative"])
        m_codes = _binary_span((double_base,) + tuple(lift(row) for row in quotient_basis))
        shift = _add(odd_base, hchar(lift(representative)), orders)
        subgroup = frozenset(
            {indices[hchar(code)] for code in m_codes}
            | {indices[_add(shift, hchar(code), orders)] for code in m_codes}
        )
        if subgroup in seen or len(subgroup) != record["subgroup_order"]:
            raise AssertionError("saved SG261 affine parameters are invalid")
        seen.add(subgroup)
        adjacency = tuple(
            reduce(int.__or__, (scalar_graphs[value][vertex] for value in subgroup), 0)
            for vertex in range(64)
        )
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if not mask)
        witness = tuple(record["witness"])
        if radical == (0,):
            faithful += 1
        if record["status"] == "clique_ge_8":
            if len(witness) != 8 or not verify_clique(adjacency, witness):
                raise AssertionError("invalid saved SG261 eight-clique")
        elif record["status"] == "nonfaithful_radical":
            if radical == (0,) or witness != radical:
                raise AssertionError("invalid saved SG261 radical")
        else:
            raise AssertionError("unknown saved SG261 subgroup status")
        statuses[record["status"]] += 1
    result = {
        "subgroup_count": len(seen),
        "status_distribution": dict(sorted(statuses.items())),
        "faithful_subgroup_count": faithful,
    }
    expected = {
        "subgroup_count": certificate["enumerated_odd_subgroup_count"],
        "status_distribution": certificate["subgroup_status_distribution"],
        "faithful_subgroup_count": certificate["faithful_subgroup_count"],
    }
    if result != expected:
        raise AssertionError("saved SG261 certificate aggregates disagree")
    return result
