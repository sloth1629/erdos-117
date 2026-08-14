"""Exact alternating-map orbit scan for the quotient Q = C3^4.

For an elementary abelian central quotient V, a commutator graph is determined
by a subspace L of alternating scalar forms: x and y are adjacent exactly when
some form in L is nonzero on (x,y).  Faithfulness is the zero-common-radical
condition.  This module enumerates all subspaces of Alt(4,3), partitions the
faithful ones under explicit invertible coordinate changes, and computes exact
graph invariants on every orbit representative using only the standard library.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations, product
from typing import Dict, Iterable, Iterator, List, Sequence, Tuple

from exact_invariants import (
    exact_chromatic_number,
    maximum_clique,
    verify_clique,
    verify_coloring,
)


FIELD = 3
VECTOR_DIMENSION = 4
FORM_DIMENSION = 6
FORM_PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

Vector = Tuple[int, ...]
Subspace = Tuple[Vector, ...]
Graph = Tuple[int, ...]


def enumerate_rref_subspaces() -> Iterator[Subspace]:
    """Yield every subspace of F_3^6 once, by its unique RREF basis."""

    for dimension in range(FORM_DIMENSION + 1):
        for pivots in combinations(range(FORM_DIMENSION), dimension):
            pivot_set = set(pivots)
            free_positions = [
                (row, column)
                for column in range(FORM_DIMENSION)
                if column not in pivot_set
                for row, pivot in enumerate(pivots)
                if pivot < column
            ]
            for values in product(range(FIELD), repeat=len(free_positions)):
                rows = [[0] * FORM_DIMENSION for _ in range(dimension)]
                for row, pivot in enumerate(pivots):
                    rows[row][pivot] = 1
                for value, (row, column) in zip(values, free_positions):
                    rows[row][column] = value
                yield tuple(tuple(row) for row in rows)


def rref(rows: Iterable[Sequence[int]]) -> Subspace:
    matrix = [
        [value % FIELD for value in row]
        for row in rows
        if any(value % FIELD for value in row)
    ]
    leading_row = 0
    for column in range(FORM_DIMENSION):
        pivot = next(
            (row for row in range(leading_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[leading_row], matrix[pivot] = matrix[pivot], matrix[leading_row]
        inverse = 1 if matrix[leading_row][column] == 1 else 2
        matrix[leading_row] = [value * inverse % FIELD for value in matrix[leading_row]]
        for row in range(len(matrix)):
            coefficient = matrix[row][column]
            if row != leading_row and coefficient:
                matrix[row] = [
                    (left - coefficient * right) % FIELD
                    for left, right in zip(matrix[row], matrix[leading_row])
                ]
        leading_row += 1
        if leading_row == len(matrix):
            break
    return tuple(tuple(row) for row in matrix)


def projective_vectors() -> Tuple[Vector, ...]:
    """Canonical representatives of the 40 points of PG(3,3)."""

    return tuple(
        vector
        for vector in product(range(FIELD), repeat=VECTOR_DIMENSION)
        if any(vector) and next(value for value in vector if value) == 1
    )


def wedge(left: Sequence[int], right: Sequence[int]) -> Vector:
    return tuple(
        (left[i] * right[j] - left[j] * right[i]) % FIELD
        for i, j in FORM_PAIRS
    )


def encode_form(row: Sequence[int]) -> int:
    return sum(value * FIELD ** index for index, value in enumerate(row))


def decode_form(code: int) -> Vector:
    return tuple(code // FIELD ** index % FIELD for index in range(FORM_DIMENSION))


def form_value(form: Sequence[int], left: Sequence[int], right: Sequence[int]) -> int:
    return sum(
        form[index] * (left[i] * right[j] - left[j] * right[i])
        for index, (i, j) in enumerate(FORM_PAIRS)
    ) % FIELD


def scalar_form_graphs() -> Tuple[Graph, ...]:
    vectors = projective_vectors()
    wedges = tuple(tuple(wedge(left, right) for right in vectors) for left in vectors)
    result = []
    for code in range(FIELD ** FORM_DIMENSION):
        form = decode_form(code)
        result.append(tuple(
            sum(
                1 << target
                for target, pair_wedge in enumerate(wedges[source])
                if sum(form[index] * pair_wedge[index] for index in range(FORM_DIMENSION)) % FIELD
            )
            for source in range(len(vectors))
        ))
    return tuple(result)


def graph_from_subspace(subspace: Subspace, scalar_graphs: Sequence[Graph]) -> Graph:
    adjacency = [0] * len(projective_vectors())
    for form in subspace:
        scalar = scalar_graphs[encode_form(form)]
        for vertex in range(len(adjacency)):
            adjacency[vertex] |= scalar[vertex]
    return tuple(adjacency)


def linear_generators() -> Tuple[Tuple[Vector, ...], ...]:
    """Five invertible matrices generating coordinate isomorphisms.

    Adjacent swaps, one transvection, and one nonzero coordinate scaling are
    elementary generators of GL(4,3).  Completeness of the computation does
    not require that generation fact: even a smaller generated subgroup would
    merely split orbits and cause more representatives to be checked.
    """

    def identity() -> List[List[int]]:
        return [[int(row == column) for column in range(VECTOR_DIMENSION)] for row in range(VECTOR_DIMENSION)]

    generators = []
    for coordinate in range(VECTOR_DIMENSION - 1):
        matrix = identity()
        matrix[coordinate][coordinate] = 0
        matrix[coordinate + 1][coordinate + 1] = 0
        matrix[coordinate][coordinate + 1] = 1
        matrix[coordinate + 1][coordinate] = 1
        generators.append(tuple(tuple(row) for row in matrix))
    matrix = identity()
    matrix[1][0] = 1
    generators.append(tuple(tuple(row) for row in matrix))
    matrix = identity()
    matrix[0][0] = 2
    generators.append(tuple(tuple(row) for row in matrix))
    return tuple(generators)


def form_action_maps() -> Tuple[Tuple[Vector, ...], ...]:
    maps = []
    for matrix in linear_generators():
        columns = tuple(
            tuple(matrix[row][column] for row in range(VECTOR_DIMENSION))
            for column in range(VECTOR_DIMENSION)
        )
        maps.append(tuple(
            tuple(form_value(decode_form(code), columns[i], columns[j]) for i, j in FORM_PAIRS)
            for code in range(FIELD ** FORM_DIMENSION)
        ))
    return tuple(maps)


def transform_subspace(subspace: Subspace, action_map: Sequence[Vector]) -> Subspace:
    return rref(action_map[encode_form(form)] for form in subspace)


def projective_permutations() -> Tuple[Tuple[int, ...], ...]:
    vectors = projective_vectors()
    index = {vector: position for position, vector in enumerate(vectors)}
    permutations = []
    for matrix in linear_generators():
        image = []
        for vector in vectors:
            transformed = tuple(
                sum(matrix[row][column] * vector[column] for column in range(VECTOR_DIMENSION)) % FIELD
                for row in range(VECTOR_DIMENSION)
            )
            leading = next(value for value in transformed if value)
            inverse = 1 if leading == 1 else 2
            normalized = tuple(inverse * value % FIELD for value in transformed)
            image.append(index[normalized])
        if len(set(image)) != len(vectors):
            raise AssertionError("linear generator did not permute projective points")
        permutations.append(tuple(image))
    return tuple(permutations)


def verify_graph_transport(
    subspace: Subspace,
    transformed: Subspace,
    permutation: Sequence[int],
    scalar_graphs: Sequence[Graph],
) -> None:
    original = graph_from_subspace(subspace, scalar_graphs)
    image = graph_from_subspace(transformed, scalar_graphs)
    for left in range(len(original)):
        for right in range(len(original)):
            # The transformed form is the pullback b^g(x,y)=b(gx,gy).
            if bool(image[left] & (1 << right)) != bool(
                original[permutation[left]] & (1 << permutation[right])
            ):
                raise AssertionError("form action did not transport the graph")


def exact_certificate() -> Dict[str, object]:
    scalar_graphs = scalar_form_graphs()
    subspaces = tuple(enumerate_rref_subspaces())
    if len(subspaces) != 56632 or len(set(subspaces)) != len(subspaces):
        raise AssertionError("wrong RREF subspace enumeration")
    dimension_distribution = Counter(map(len, subspaces))
    radical_distribution = Counter()
    faithful = set()
    for subspace in subspaces:
        graph = graph_from_subspace(subspace, scalar_graphs)
        radical_points = sum(mask == 0 for mask in graph)
        radical_distribution[(len(subspace), radical_points)] += 1
        if radical_points == 0:
            faithful.add(subspace)
    if len(faithful) != 55941:
        raise AssertionError("wrong common-radical-zero count")

    actions = form_action_maps()
    permutations = projective_permutations()
    unseen = set(faithful)
    orbit_records = []
    while unseen:
        representative = min(unseen)
        unseen.remove(representative)
        orbit = {representative}
        queue = deque([representative])
        while queue:
            subspace = queue.popleft()
            for action in actions:
                transformed = transform_subspace(subspace, action)
                if transformed not in faithful:
                    raise AssertionError("invertible action left the faithful set")
                if transformed not in orbit:
                    orbit.add(transformed)
                    unseen.discard(transformed)
                    queue.append(transformed)
        graph = graph_from_subspace(representative, scalar_graphs)
        clique = maximum_clique(graph)
        coloring = exact_chromatic_number(graph, clique.size)
        if not verify_clique(graph, clique.vertices) or not verify_coloring(graph, coloring.colors):
            raise AssertionError("exact graph certificate failed")
        orbit_records.append({
            "dual_form_dimension": len(representative),
            "kernel_dimension": FORM_DIMENSION - len(representative),
            "representative_rref": [list(row) for row in representative],
            "orbit_size": len(orbit),
            "projective_adjacency": list(graph),
            "edge_count": sum(bin(mask).count("1") for mask in graph) // 2,
            "omega": clique.size,
            "chi": coloring.size,
            "clique_certificate": list(clique.vertices),
            "coloring_certificate": list(coloring.colors),
            "clique_search_nodes": clique.search_nodes,
            "coloring_search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
        })

    # Check each generator explicitly on every orbit representative.  Together
    # with the full orbit partition this certifies that representative graph
    # invariants apply to every one of the 55,941 faithful subspaces.
    for record in orbit_records:
        representative = tuple(tuple(row) for row in record["representative_rref"])
        for action, permutation in zip(actions, permutations):
            verify_graph_transport(
                representative,
                transform_subspace(representative, action),
                permutation,
                scalar_graphs,
            )

    weighted_distribution = Counter()
    orbit_distribution = Counter()
    for record in orbit_records:
        pair = (record["omega"], record["chi"])
        weighted_distribution[pair] += record["orbit_size"]
        orbit_distribution[pair] += 1
    eligible = [record for record in orbit_records if record["omega"] <= 7]
    if len(eligible) != 1 or (eligible[0]["omega"], eligible[0]["chi"]) != (7, 10):
        raise AssertionError("unexpected C3^4 cutoff-seven result")
    return {
        "field_order": FIELD,
        "vector_dimension": VECTOR_DIMENSION,
        "alternating_form_dimension": FORM_DIMENSION,
        "projective_vertex_count": len(projective_vectors()),
        "raw_subspace_count": len(subspaces),
        "subspace_dimension_distribution": {
            str(dimension): count for dimension, count in sorted(dimension_distribution.items())
        },
        "radical_distribution": [
            {
                "dual_form_dimension": dimension,
                "projective_radical_point_count": radical,
                "count": count,
            }
            for (dimension, radical), count in sorted(radical_distribution.items())
        ],
        "faithful_subspace_count": len(faithful),
        "nonfaithful_subspace_count": len(subspaces) - len(faithful),
        "linear_generator_count": len(actions),
        "orbit_count": len(orbit_records),
        "orbit_size_sum": sum(record["orbit_size"] for record in orbit_records),
        "weighted_invariant_distribution": [
            {"omega": pair[0], "chi": pair[1], "subspace_count": count}
            for pair, count in sorted(weighted_distribution.items())
        ],
        "orbit_invariant_distribution": [
            {"omega": pair[0], "chi": pair[1], "orbit_count": count}
            for pair, count in sorted(orbit_distribution.items())
        ],
        "eligible_orbit_indices": [
            index for index, record in enumerate(orbit_records) if record["omega"] <= 7
        ],
        "maximum_a_at_nu_at_most_7": max(record["chi"] for record in eligible),
        "orbits": orbit_records,
    }
