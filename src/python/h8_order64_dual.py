#!/usr/bin/env python3
"""Exact cutoff-eight dual searches for the eleven generic order-64 cases.

The GAP exports and their structural parser are shared with the cutoff-seven
certificate.  This module performs a new search: it retains precisely the
action-invariant character subgroups whose union graph has no 9-clique.

Completeness uses two monotonicity facts.  A subgroup containing a scalar
character whose scalar graph has a 9-clique is immediately impossible.  A
supergroup of a pruned boundary subgroup contains its saved 9-clique.  Hence
it is enough to breadth-first enumerate invariant closures inside the set of
scalar characters of clique number at most eight.
"""

from __future__ import annotations

import itertools
from collections import Counter, deque
from functools import reduce
from pathlib import Path
from typing import Dict, Iterable, Sequence, Tuple

from exact_invariants import (
    exact_chromatic_number,
    maximum_clique,
    verify_clique,
    verify_coloring,
)
from h7_order64_dual import _add, _character_value, parse_export


Vector = Tuple[int, ...]
Adjacency = Tuple[int, ...]


def adjacency_sha256_payload(adjacency: Sequence[int]) -> bytes:
    """Return the canonical bytes hashed by the aggregate certificate."""

    return (",".join(map(str, adjacency)) + "\n").encode("ascii")


def compress_independent_twins(
    adjacency: Sequence[int],
) -> Tuple[Tuple[int, ...], Adjacency, Tuple[int, ...]]:
    """Collapse vertices with equal open neighbourhoods.

    Equal open neighbourhoods are necessarily nonadjacent, so their classes
    are independent twins.  Choosing one representative from each class
    preserves both clique and chromatic number.  The returned ``classes``
    tuple maps every original vertex to its compressed vertex.
    """

    n = len(adjacency)
    allowed = (1 << n) - 1
    for vertex, mask in enumerate(adjacency):
        if mask < 0 or mask & ~allowed or mask & (1 << vertex):
            raise AssertionError("invalid simple-graph adjacency")
        for target in range(n):
            if bool(mask & (1 << target)) != bool(
                adjacency[target] & (1 << vertex)
            ):
                raise AssertionError("asymmetric graph adjacency")

    mask_to_class: Dict[int, int] = {}
    representatives = []
    classes = []
    for vertex, mask in enumerate(adjacency):
        if mask not in mask_to_class:
            mask_to_class[mask] = len(representatives)
            representatives.append(vertex)
        classes.append(mask_to_class[mask])

    for left in range(n):
        for right in range(left + 1, n):
            if classes[left] == classes[right] and adjacency[left] & (1 << right):
                raise AssertionError("equal-neighbourhood class is not independent")

    reduced = tuple(
        sum(
            1 << target_class
            for target_class, target in enumerate(representatives)
            if adjacency[source] & (1 << target)
        )
        for source in representatives
    )
    return tuple(representatives), reduced, tuple(classes)


def lift_clique(
    representatives: Sequence[int], compressed_clique: Sequence[int]
) -> Tuple[int, ...]:
    return tuple(representatives[vertex] for vertex in compressed_clique)


def lift_coloring(
    classes: Sequence[int], compressed_coloring: Sequence[int]
) -> Tuple[int, ...]:
    return tuple(compressed_coloring[vertex_class] for vertex_class in classes)


def greedy_target_clique(
    adjacency: Sequence[int], target: int
) -> Tuple[int, ...]:
    """Deterministic multi-start clique search used only for witnesses."""

    starts = sorted(
        range(len(adjacency)),
        key=lambda vertex: (-bin(adjacency[vertex]).count("1"), vertex),
    )
    for start in starts:
        clique = [start]
        candidates = adjacency[start]
        while candidates and len(clique) < target:
            choices = [
                vertex
                for vertex in range(len(adjacency))
                if candidates & (1 << vertex)
            ]
            chosen = min(
                choices,
                key=lambda vertex: (
                    -bin(candidates & adjacency[vertex]).count("1"), vertex
                ),
            )
            clique.append(chosen)
            candidates &= adjacency[chosen]
        if len(clique) == target:
            return tuple(clique)
    return ()


def _generated_subgroup(
    subgroup: Iterable[int], generator: int, addition: Sequence[Sequence[int]]
) -> frozenset[int]:
    subgroup = frozenset(subgroup)
    if generator in subgroup:
        return subgroup
    identity = 0
    cyclic = [identity]
    current = generator
    while current != identity:
        cyclic.append(current)
        current = addition[current][generator]
    return frozenset(
        addition[left][right] for left in subgroup for right in cyclic
    )


def exact_certificate(export_path: Path) -> Dict[str, object]:
    """Compute the complete no-nine-clique invariant-subgroup certificate."""

    parsed = parse_export(export_path)
    metadata = parsed["metadata"]
    orders = parsed["orders"]
    table = parsed["commutators"]
    actions = parsed["actions"]
    q_exponents = parsed["q_exponents"]
    characters = tuple(itertools.product(*(range(order) for order in orders)))
    character_index = {
        character: serial for serial, character in enumerate(characters)
    }
    if character_index[(0,) * len(orders)] != 0:
        raise AssertionError("identity character is not first")

    addition = tuple(
        tuple(character_index[_add(left, right, orders)] for right in characters)
        for left in characters
    )
    scalar_graphs = tuple(
        tuple(
            sum(
                1 << right
                for right, commutator in enumerate(row)
                if left != right
                and _character_value(character, commutator, orders)
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
            mapping.append(character_index[tuple(coordinates)])
        if len(set(mapping)) != len(characters):
            raise AssertionError("character action is not bijective")
        action_maps.append(tuple(mapping))

    scalar_status = Counter()
    scalar_records = []
    good = set()
    for index, adjacency in enumerate(scalar_graphs):
        representatives, reduced, _ = compress_independent_twins(adjacency)
        clique = maximum_clique(reduced)
        lifted = lift_clique(representatives, clique.vertices)
        if not verify_clique(adjacency, lifted):
            raise AssertionError("invalid exact scalar clique")
        if clique.size <= 8:
            good.add(index)
            status = "omega_le_8"
            witness = lifted
        else:
            status = "clique_ge_9"
            witness = lifted[:9]
            if not verify_clique(adjacency, witness):
                raise AssertionError("invalid scalar nine-clique")
        scalar_status["omega_%d" % clique.size] += 1
        scalar_records.append({
            "character_index": index,
            "character": list(characters[index]),
            "status": status,
            "omega": clique.size,
            "clique": list(lifted),
            "nine_clique": list(witness if clique.size >= 9 else ()),
            "twin_quotient_order": len(reduced),
            "clique_search_nodes": clique.search_nodes,
        })
    if 0 not in good:
        raise AssertionError("identity character was excluded")

    def invariant_closure(subgroup: frozenset[int], generator: int) -> frozenset[int]:
        result = _generated_subgroup(subgroup, generator, addition)
        while True:
            images = {
                mapping[value]
                for mapping in action_maps
                for value in result
            }
            new = result
            for image in images - result:
                new = _generated_subgroup(new, image, addition)
            if new == result:
                return result
            result = new

    def union_graph(subgroup: Iterable[int]) -> Adjacency:
        values = tuple(subgroup)
        return tuple(
            reduce(int.__or__, (scalar_graphs[value][vertex] for value in values), 0)
            for vertex in range(64)
        )

    trivial = frozenset((0,))
    queue = deque([trivial])
    seen = {trivial}
    pruned = set()
    retained_records = []
    boundary_records = []
    retained_status = Counter()
    retained_omega = Counter()
    radical_distribution = Counter()
    faithful_records = []

    while queue:
        subgroup = queue.popleft()
        if any(
            {mapping[value] for value in subgroup} != set(subgroup)
            for mapping in action_maps
        ):
            raise AssertionError("retained character subgroup is not invariant")
        if not subgroup <= good:
            raise AssertionError("retained subgroup contains a bad scalar")
        adjacency = union_graph(subgroup)
        representatives, reduced, classes = compress_independent_twins(adjacency)
        clique = maximum_clique(reduced)
        lifted_clique = lift_clique(representatives, clique.vertices)
        if clique.size > 8 or not verify_clique(adjacency, lifted_clique):
            raise AssertionError("retained subgroup is outside cutoff eight")
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if not mask)
        radical_distribution[len(radical)] += 1
        retained_omega[clique.size] += 1
        if radical == (0,):
            status = "faithful_candidate"
            coloring = exact_chromatic_number(reduced, clique.size)
            lifted_coloring = lift_coloring(classes, coloring.colors)
            if not verify_coloring(adjacency, lifted_coloring):
                raise AssertionError("invalid faithful exact coloring")
            faithful_record = {
                "characters": sorted(subgroup),
                "subgroup_order": len(subgroup),
                "omega": clique.size,
                "chi": coloring.size,
                "clique": list(lifted_clique),
                "coloring": list(lifted_coloring),
                "commuting_color_classes": [
                    [
                        vertex
                        for vertex, color in enumerate(lifted_coloring)
                        if color == selected
                    ]
                    for selected in range(coloring.size)
                ],
                "twin_quotient_order": len(reduced),
                "clique_search_nodes": clique.search_nodes,
                "coloring_search_nodes_by_k": [
                    list(item) for item in coloring.search_nodes_by_k
                ],
            }
            faithful_records.append(faithful_record)
        else:
            status = "nonfaithful_radical"
        retained_status[status] += 1
        retained_records.append({
            "characters": sorted(subgroup),
            "subgroup_order": len(subgroup),
            "status": status,
            "radical": list(radical),
            "omega": clique.size,
            "clique": list(lifted_clique),
            "twin_quotient_order": len(reduced),
            "clique_search_nodes": clique.search_nodes,
        })

        candidate_children = set()
        for generator in sorted(good - subgroup):
            child = invariant_closure(subgroup, generator)
            if child in seen or child in pruned or child in candidate_children:
                continue
            candidate_children.add(child)
        for child in sorted(candidate_children, key=lambda value: tuple(sorted(value))):
            if not child <= good:
                # Such a child contains a scalar graph with a saved 9-clique.
                continue
            adjacency = union_graph(child)
            witness = greedy_target_clique(adjacency, 9)
            if witness:
                if not verify_clique(adjacency, witness):
                    raise AssertionError("invalid boundary nine-clique")
                pruned.add(child)
                boundary_records.append({
                    "characters": sorted(child),
                    "subgroup_order": len(child),
                    "nine_clique": list(witness),
                })
                continue
            representatives, reduced, _ = compress_independent_twins(adjacency)
            clique = maximum_clique(reduced)
            if clique.size >= 9:
                lifted = lift_clique(representatives, clique.vertices[:9])
                if not verify_clique(adjacency, lifted):
                    raise AssertionError("invalid exact boundary nine-clique")
                pruned.add(child)
                boundary_records.append({
                    "characters": sorted(child),
                    "subgroup_order": len(child),
                    "nine_clique": list(lifted),
                })
            else:
                seen.add(child)
                queue.append(child)

    identity_vertex = q_exponents.index((0,) * len(q_exponents[0]))
    if identity_vertex != 0:
        raise AssertionError("quotient identity is not first")
    expected = {
        193: (192, 498, 4053),
        195: (64, 450, 1765),
        202: (224, 498, 2609),
        203: (128, 482, 2141),
        207: (96, 466, 1953),
        211: (288, 498, 2453),
        216: (96, 466, 1953),
        226: (128, 482, 2141),
        236: (64, 450, 1765),
        242: (64, 450, 1765),
        250: (96, 466, 1953),
    }
    observed = (len(good), len(seen), len(pruned))
    if parsed["q_id"] not in expected or observed != expected[parsed["q_id"]]:
        raise AssertionError("unexpected cutoff-eight generic-dual census")
    if scalar_status.get("omega_8", 0) or faithful_records:
        raise AssertionError("unexpected generic-dual cutoff-eight candidate")
    return {
        "q_id": parsed["q_id"],
        "metadata": metadata,
        "identity_vertex": identity_vertex,
        "character_count": len(characters),
        "good_character_count": len(good),
        "scalar_exact_omega_distribution": {
            str(key): value for key, value in sorted(scalar_status.items())
        },
        "scalar_records": scalar_records,
        "action_count": len(actions),
        "retained_no_nine_subgroup_count": len(seen),
        "pruned_boundary_subgroup_count": len(pruned),
        "retained_status_distribution": dict(sorted(retained_status.items())),
        "retained_exact_omega_distribution": {
            str(key): value for key, value in sorted(retained_omega.items())
        },
        "radical_size_distribution": {
            str(key): value for key, value in sorted(radical_distribution.items())
        },
        "faithful_candidate_count": len(faithful_records),
        "maximum_faithful_chi": max(
            (record["chi"] for record in faithful_records), default=0
        ),
        "faithful_records": faithful_records,
        "retained_records": retained_records,
        "boundary_records": boundary_records,
        "completeness": (
            "BFS starts at the trivial subgroup and adjoins every scalar-good "
            "character followed by full action-invariant closure. A subgroup "
            "containing a scalar-bad character contains its saved 9-clique; "
            "every supergroup of a pruned boundary subgroup contains that "
            "boundary record's saved 9-clique. Thus every invariant subgroup "
            "with no 9-clique is retained."
        ),
    }


def verify_certificate(certificate: Dict[str, object], export_path: Path) -> None:
    """Recompute the deterministic payload and compare every saved record."""

    rebuilt = exact_certificate(export_path)
    if certificate != rebuilt:
        raise AssertionError("saved cutoff-eight dual certificate changed")
