#!/usr/bin/env python3
"""Exact character-dual cutoff-seven certificates for order-64 quotients.

For an abelian exterior square ``E=Q wedge Q`` and an action-invariant kernel
``K<=E``, Pontryagin annihilation replaces ``K`` by the action-invariant
character subgroup ``L=K^perp<=E^*``.  The graph for ``K`` is the union of
the scalar graphs defined by characters in ``L``.  A graph with no
eight-clique can use only scalar characters whose own graph has no
eight-clique.  Breadth-first invariant closure therefore enumerates every
possible no-eight-clique ``L``; this module deliberately performs no
automorphism-orbit quotient, keeping the completeness check transparent.
"""

from __future__ import annotations

import itertools
from collections import Counter, deque
from functools import reduce
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from exact_invariants import maximum_clique, verify_clique


Vector = Tuple[int, ...]
Adjacency = Tuple[int, ...]


def _vector(raw: str) -> Vector:
    return tuple(int(value) for value in raw.split(",") if value != "")


def _vectors(raw: str) -> Tuple[Vector, ...]:
    return tuple(_vector(value) for value in raw.split(";"))


def _add(left: Vector, right: Vector, orders: Vector) -> Vector:
    return tuple((a + b) % order for a, b, order in zip(left, right, orders))


def _negate(value: Vector, orders: Vector) -> Vector:
    return tuple((-entry) % order for entry, order in zip(value, orders))


def _action_image(value: Vector, images: Sequence[Vector], orders: Vector) -> Vector:
    result = (0,) * len(orders)
    for coefficient, image in zip(value, images):
        for _ in range(coefficient):
            result = _add(result, image, orders)
    return result


def _generated_subgroup(generators: Iterable[Vector], orders: Vector):
    zero = (0,) * len(orders)
    result = {zero}
    for generator in generators:
        if generator in result:
            continue
        cyclic = [zero]
        current = generator
        while current != zero:
            cyclic.append(current)
            current = _add(current, generator, orders)
        result = {_add(a, b, orders) for a in result for b in cyclic}
    return frozenset(result)


def parse_export(path: Path) -> Dict[str, object]:
    metadata: Dict[str, str] = {}
    actions = []
    commutators = []
    q_exponents = []
    automorphisms = []
    section = None
    header = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            if key in metadata:
                raise AssertionError("duplicate dual-export metadata")
            metadata[key] = value
        elif line in ("ACTIONS", "COMMUTATORS", "AUTOMORPHISMS"):
            section = line.lower()
            header = None
        elif line:
            if header is None:
                header = line
                expected = {
                    "actions": "action_index\timage_vectors\tq_conjugation",
                    "commutators": "vertex\tq_exponents\tcommutator_vectors",
                    "automorphisms": "automorphism_index\tq_permutation",
                }[section]
                if header != expected:
                    raise AssertionError("wrong dual-export section header")
                continue
            fields = line.split("\t")
            if section == "actions":
                if int(fields[0]) != len(actions) + 1:
                    raise AssertionError("incomplete action serials")
                actions.append((_vectors(fields[1]), tuple(map(int, fields[2].split(",")))))
            elif section == "commutators":
                if int(fields[0]) != len(commutators):
                    raise AssertionError("incomplete commutator row serials")
                q_exponents.append(_vector(fields[1]))
                commutators.append(_vectors(fields[2]))
            elif section == "automorphisms":
                if int(fields[0]) != len(automorphisms) + 1:
                    raise AssertionError("incomplete automorphism serials")
                automorphisms.append(tuple(map(int, fields[1].split(","))))
            else:
                raise AssertionError("dual-export data outside a section")

    required = {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "Q_ORDER": "64",
        "PC_CONVERSION_KERNEL_ORDER": "1",
        "COVER_KERNEL_CENTRAL": "true",
        "COVER_KERNEL_IN_DERIVED": "true",
        "COMMUTATOR_ROW_COUNT": "64",
    }
    if any(metadata.get(key) != value for key, value in required.items()):
        raise AssertionError("wrong fixed dual-export metadata")
    q_id = int(metadata["Q_ID"])
    q_orders = _vector(metadata["Q_PC_RELATIVE_ORDERS"])
    orders = _vector(metadata["EXTERIOR_RELATIVE_ORDERS"])
    if not orders or any(order not in (2, 4, 8) for order in orders):
        raise AssertionError("unsupported exterior invariant factors")
    if len(actions) != int(metadata["ACTION_COUNT"]):
        raise AssertionError("wrong action count")
    if len(automorphisms) != int(metadata["AUTOMORPHISM_GENERATOR_COUNT"]):
        raise AssertionError("wrong automorphism count")
    if len(commutators) != 64 or len(q_exponents) != 64:
        raise AssertionError("wrong commutator table size")
    if int(metadata["EXTERIOR_ORDER"]) != _product(orders):
        raise AssertionError("wrong exterior invariant-factor product")
    if int(metadata["COVER_ORDER"]) != 64 * int(metadata["COVER_TO_Q_KERNEL_ORDER"]):
        raise AssertionError("cover/kernel/quotient orders disagree")
    if any(len(images) != len(orders) for images, _ in actions):
        raise AssertionError("wrong action image count")
    if any(len(vector) != len(orders) for images, _ in actions for vector in images):
        raise AssertionError("wrong action-vector dimension")
    if any(len(row) != 64 for row in commutators):
        raise AssertionError("wrong commutator row length")
    if any(len(value) != len(orders) for row in commutators for value in row):
        raise AssertionError("wrong commutator-vector dimension")
    if any(sorted(permutation) != list(range(64)) for _, permutation in actions):
        raise AssertionError("invalid quotient conjugation permutation")
    if any(sorted(permutation) != list(range(64)) for permutation in automorphisms):
        raise AssertionError("invalid quotient automorphism permutation")
    if len(set(q_exponents)) != 64 or set(q_exponents) != set(
        itertools.product(*(range(order) for order in q_orders))
    ):
        raise AssertionError("quotient exponent enumeration is incomplete")
    zero = (0,) * len(orders)
    for left in range(64):
        if commutators[left][left] != zero:
            raise AssertionError("nonzero commutator diagonal")
        for right in range(64):
            if commutators[right][left] != _negate(commutators[left][right], orders):
                raise AssertionError("commutator table is not skew-symmetric")
    if len(_generated_subgroup(
        (commutators[i][j] for i in range(64) for j in range(64)), orders
    )) != int(metadata["EXTERIOR_ORDER"]):
        raise AssertionError("lifted commutators do not generate exterior square")

    exterior_elements = tuple(itertools.product(*(range(order) for order in orders)))
    for images, permutation in actions:
        lookup = {value: _action_image(value, images, orders) for value in exterior_elements}
        if len(set(lookup.values())) != len(exterior_elements):
            raise AssertionError("conjugation action is not bijective")
        for left in range(64):
            for right in range(64):
                if lookup[commutators[left][right]] != (
                    commutators[permutation[left]][permutation[right]]
                ):
                    raise AssertionError("action does not transport commutators")

    # Derive and validate the exterior automorphism induced by every exported
    # quotient automorphism.  This is an independent cross-check; the complete
    # BFS below does not quotient by these automorphisms.
    automorphism_exterior_maps = []
    for permutation in automorphisms:
        mapping = {zero: zero}
        for left in range(64):
            for right in range(64):
                source = commutators[left][right]
                target = commutators[permutation[left]][permutation[right]]
                if source in mapping:
                    if mapping[source] != target:
                        raise AssertionError("automorphism commutator transport conflicts")
                    continue
                cyclic_source = [zero]
                cyclic_target = [zero]
                current_source, current_target = source, target
                while current_source != zero:
                    cyclic_source.append(current_source)
                    cyclic_target.append(current_target)
                    current_source = _add(current_source, source, orders)
                    current_target = _add(current_target, target, orders)
                old = tuple(mapping.items())
                for value, image in old:
                    for add_source, add_target in zip(cyclic_source, cyclic_target):
                        combined = _add(value, add_source, orders)
                        combined_image = _add(image, add_target, orders)
                        if combined in mapping and mapping[combined] != combined_image:
                            raise AssertionError("automorphism extension conflict")
                        mapping[combined] = combined_image
        if len(mapping) != len(exterior_elements) or len(set(mapping.values())) != len(exterior_elements):
            raise AssertionError("quotient automorphism does not induce exterior automorphism")
        automorphism_exterior_maps.append(tuple(mapping[value] for value in exterior_elements))

    return {
        "metadata": metadata,
        "q_id": q_id,
        "q_orders": q_orders,
        "orders": orders,
        "q_exponents": tuple(q_exponents),
        "actions": tuple(actions),
        "commutators": tuple(tuple(row) for row in commutators),
        "automorphisms": tuple(automorphisms),
        "automorphism_exterior_maps": tuple(automorphism_exterior_maps),
    }


def _product(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def _character_value(character: Vector, element: Vector, orders: Vector) -> int:
    modulus = max(orders)
    return sum(
        coefficient * exponent * (modulus // order)
        for coefficient, exponent, order in zip(character, element, orders)
    ) % modulus


def _greedy(adjacency: Adjacency, target: int = 8) -> Tuple[int, ...]:
    starts = sorted(range(64), key=lambda v: (-bin(adjacency[v]).count("1"), v))
    for start in starts:
        clique = [start]
        candidates = adjacency[start]
        while candidates and len(clique) < target:
            choices = [v for v in range(64) if candidates & (1 << v)]
            chosen = min(
                choices,
                key=lambda v: (-bin(candidates & adjacency[v]).count("1"), v),
            )
            clique.append(chosen)
            candidates &= adjacency[chosen]
        if len(clique) == target:
            return tuple(clique)
    return ()


def exact_certificate(export_path: Path) -> Dict[str, object]:
    parsed = parse_export(export_path)
    metadata = parsed["metadata"]
    orders = parsed["orders"]
    table = parsed["commutators"]
    actions = parsed["actions"]
    q_exponents = parsed["q_exponents"]
    characters = tuple(itertools.product(*(range(order) for order in orders)))
    index = {character: serial for serial, character in enumerate(characters)}
    identity_character = index[(0,) * len(orders)]
    if identity_character != 0:
        raise AssertionError("character enumeration does not start at identity")

    addition = tuple(
        tuple(index[_add(left, right, orders)] for right in characters)
        for left in characters
    )
    scalar_graphs = tuple(
        tuple(
            sum(
                1 << right
                for right, commutator in enumerate(row)
                if left != right and _character_value(character, commutator, orders)
            )
            for left, row in enumerate(table)
        )
        for character in characters
    )

    action_maps = []
    for images, _ in actions:
        mapping = []
        for character in characters:
            coordinates = []
            for source_order, image in zip(orders, images):
                value = _character_value(character, image, orders)
                step = max(orders) // source_order
                if value % step:
                    raise AssertionError("action pullback is not a character")
                coordinates.append((value // step) % source_order)
            mapping.append(index[tuple(coordinates)])
        if len(set(mapping)) != len(characters):
            raise AssertionError("character action is not bijective")
        action_maps.append(tuple(mapping))

    scalar_status = Counter()
    scalar_records = []
    good = {identity_character}
    for character in range(1, len(characters)):
        adjacency = scalar_graphs[character]
        witness = _greedy(adjacency)
        if witness:
            if not verify_clique(adjacency, witness):
                raise AssertionError("invalid scalar eight-clique")
            status = "clique_ge_8"
            scalar_status[status] += 1
            scalar_records.append({
                "character_index": character,
                "character": list(characters[character]),
                "status": status,
                "witness": list(witness),
            })
        else:
            clique = maximum_clique(adjacency)
            if clique.size > 7 or not verify_clique(adjacency, clique.vertices):
                raise AssertionError("scalar cutoff classification failed")
            good.add(character)
            status = "omega_%d" % clique.size
            scalar_status[status] += 1
            scalar_records.append({
                "character_index": character,
                "character": list(characters[character]),
                "status": status,
                "omega": clique.size,
                "witness": list(clique.vertices),
                "search_nodes": clique.search_nodes,
            })

    def generated(subgroup, generator):
        if generator in subgroup:
            return subgroup
        cyclic = [identity_character]
        current = generator
        while current != identity_character:
            cyclic.append(current)
            current = addition[current][generator]
        return frozenset(
            addition[left][right] for left in subgroup for right in cyclic
        )

    def invariant_closure(subgroup, generator):
        result = generated(subgroup, generator)
        while True:
            images = {mapping[value] for mapping in action_maps for value in result}
            new = result
            for image in images - result:
                new = generated(new, image)
            if new == result:
                return result
            result = new

    def union_graph(subgroup):
        return tuple(
            reduce(int.__or__, (scalar_graphs[c][v] for c in subgroup), 0)
            for v in range(64)
        )

    trivial = frozenset((identity_character,))
    queue = deque([trivial])
    seen = {trivial}
    pruned = set()
    retained_records = []
    boundary_records = []
    retained_status = Counter()
    radical_distribution = Counter()
    while queue:
        subgroup = queue.popleft()
        if any(
            {mapping[value] for value in subgroup} != set(subgroup)
            for mapping in action_maps
        ):
            raise AssertionError("retained character subgroup is not action invariant")
        adjacency = union_graph(subgroup)
        if _greedy(adjacency):
            raise AssertionError("retained subgroup has a greedy eight-clique")
        clique = maximum_clique(adjacency)
        if clique.size > 7 or not verify_clique(adjacency, clique.vertices):
            raise AssertionError("retained subgroup is outside cutoff")
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if not mask)
        if radical == (0,):
            status = "faithful_candidate"
        else:
            status = "nonfaithful_radical"
        retained_status[status] += 1
        radical_distribution[len(radical)] += 1
        retained_records.append({
            "characters": sorted(subgroup),
            "subgroup_order": len(subgroup),
            "status": status,
            "radical": list(radical),
            "omega": clique.size,
            "clique": list(clique.vertices),
            "clique_search_nodes": clique.search_nodes,
        })

        candidates = set()
        for generator in sorted(good - subgroup):
            child = invariant_closure(subgroup, generator)
            if child in seen or child in pruned or child in candidates:
                continue
            candidates.add(child)
        for child in sorted(candidates, key=lambda value: tuple(sorted(value))):
            if not child <= good:
                # It contains a scalar whose saved graph already has an
                # eight-clique, so no separate union witness is needed.
                continue
            adjacency = union_graph(child)
            witness = _greedy(adjacency)
            if witness:
                if not verify_clique(adjacency, witness):
                    raise AssertionError("invalid boundary eight-clique")
                pruned.add(child)
                boundary_records.append({
                    "characters": sorted(child),
                    "subgroup_order": len(child),
                    "witness": list(witness),
                })
            else:
                clique = maximum_clique(adjacency)
                if clique.size > 7:
                    raise AssertionError("greedy search missed a boundary eight-clique")
                seen.add(child)
                queue.append(child)

    represented = len(seen)
    if retained_status.get("faithful_candidate", 0):
        raise AssertionError("generic order-64 dual case has a faithful candidate")
    expected = {
        193: (192, 498, 4053, {4: 334, 8: 128, 16: 35, 64: 1}),
        195: (64, 450, 1765, {4: 294, 8: 120, 16: 35, 64: 1}),
        202: (224, 498, 2609, {4: 330, 8: 132, 16: 35, 64: 1}),
        203: (128, 482, 2141, {4: 318, 8: 128, 16: 35, 64: 1}),
        207: (96, 466, 1953, {4: 306, 8: 124, 16: 35, 64: 1}),
        211: (288, 498, 2453, {4: 330, 8: 132, 16: 35, 64: 1}),
        216: (96, 466, 1953, {4: 306, 8: 124, 16: 35, 64: 1}),
        226: (128, 482, 2141, {4: 318, 8: 128, 16: 35, 64: 1}),
        236: (64, 450, 1765, {4: 294, 8: 120, 16: 35, 64: 1}),
        242: (64, 450, 1765, {4: 294, 8: 120, 16: 35, 64: 1}),
        250: (96, 466, 1953, {4: 306, 8: 124, 16: 35, 64: 1}),
    }
    observed = (
        len(good), represented, len(pruned), dict(sorted(radical_distribution.items()))
    )
    if parsed["q_id"] not in expected or observed != expected[parsed["q_id"]]:
        raise AssertionError("unexpected generic order-64 dual census")
    identity_vertex = q_exponents.index((0,) * len(q_exponents[0]))
    if identity_vertex != 0:
        raise AssertionError("quotient element enumeration does not start at identity")
    return {
        "metadata": metadata,
        "identity_vertex": identity_vertex,
        "character_count": len(characters),
        "good_character_count": len(good),
        "scalar_status_distribution": dict(sorted(scalar_status.items())),
        "scalar_records": scalar_records,
        "action_count": len(actions),
        "automorphism_generator_count": len(parsed["automorphisms"]),
        "retained_no_eight_subgroup_count": represented,
        "pruned_boundary_subgroup_count": len(pruned),
        "retained_status_distribution": dict(sorted(retained_status.items())),
        "radical_size_distribution": {
            str(key): value for key, value in sorted(radical_distribution.items())
        },
        "faithful_candidate_count": retained_status.get("faithful_candidate", 0),
        "retained_records": retained_records,
        "boundary_records": boundary_records,
    }
