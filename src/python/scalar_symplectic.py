"""Exact scalar-symplectic graphs, spreads, and independent certificates."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from exact_invariants import (
    abelian_subgroups_from_coloring,
    commuting_probability,
    compressed_noncommuting_graph,
    exact_chromatic_number,
    maximum_clique,
    verify_abelian_cover,
    verify_clique,
    verify_coloring,
)
from finite_groups import FiniteGroup, extraspecial_prime_group


Vector = Tuple[int, ...]


def _is_prime(value: int) -> bool:
    return value >= 2 and not any(value % divisor == 0 for divisor in range(2, int(value ** 0.5) + 1))


def _popcount(mask: int) -> int:
    return bin(mask).count("1")


def quotient_vectors(prime: int, rank: int) -> Tuple[Vector, ...]:
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if rank < 1:
        raise ValueError("rank must be positive")
    return tuple(product(range(prime), repeat=2 * rank))


def symplectic_value(prime: int, rank: int, left: Vector, right: Vector) -> int:
    if len(left) != 2 * rank or len(right) != 2 * rank:
        raise ValueError("vector has the wrong dimension")
    return sum(
        left[i] * right[rank + i] - right[i] * left[rank + i]
        for i in range(rank)
    ) % prime


def scalar_symplectic_adjacency(prime: int, rank: int) -> Tuple[Vector, Tuple[int, ...]]:
    """Return all vectors and adjacency ``B(v,w) != 0``."""

    vectors = quotient_vectors(prime, rank)
    adjacency = []
    for left in vectors:
        mask = 0
        for index, right in enumerate(vectors):
            if symplectic_value(prime, rank, left, right):
                mask |= 1 << index
        adjacency.append(mask)
    return vectors, tuple(adjacency)


def _polynomial_remainder_zero(polynomial: Sequence[int], divisor: Sequence[int], prime: int) -> bool:
    remainder = [value % prime for value in polynomial]
    divisor_degree = len(divisor) - 1
    for degree in range(len(remainder) - 1, divisor_degree - 1, -1):
        coefficient = remainder[degree]
        if not coefficient:
            continue
        offset = degree - divisor_degree
        for index, value in enumerate(divisor):
            remainder[offset + index] = (remainder[offset + index] - coefficient * value) % prime
    return not any(remainder[:divisor_degree])


def first_irreducible_polynomial(prime: int, degree: int) -> Tuple[int, ...]:
    """Find the first monic irreducible polynomial in lexicographic order."""

    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if degree < 1:
        raise ValueError("degree must be positive")
    for lower in product(range(prime), repeat=degree):
        if lower[0] == 0:
            continue
        polynomial = tuple(lower) + (1,)
        reducible = False
        for divisor_degree in range(1, degree // 2 + 1):
            for divisor_lower in product(range(prime), repeat=divisor_degree):
                if divisor_lower[0] == 0:
                    continue
                divisor = tuple(divisor_lower) + (1,)
                if _polynomial_remainder_zero(polynomial, divisor, prime):
                    reducible = True
                    break
            if reducible:
                break
        if not reducible:
            return polynomial
    raise AssertionError("no irreducible polynomial found")


@dataclass(frozen=True)
class FiniteFieldModel:
    prime: int
    degree: int
    modulus: Tuple[int, ...]

    @classmethod
    def create(cls, prime: int, degree: int) -> "FiniteFieldModel":
        return cls(prime, degree, first_irreducible_polynomial(prime, degree))

    @property
    def elements(self) -> Tuple[Vector, ...]:
        return tuple(product(range(self.prime), repeat=self.degree))

    def multiply(self, left: Vector, right: Vector) -> Vector:
        p, m = self.prime, self.degree
        coefficients = [0] * (2 * m - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                coefficients[i + j] = (coefficients[i + j] + x * y) % p
        for degree in range(2 * m - 2, m - 1, -1):
            coefficient = coefficients[degree]
            if not coefficient:
                continue
            for index in range(m):
                target = degree - m + index
                coefficients[target] = (coefficients[target] - coefficient * self.modulus[index]) % p
        return tuple(coefficients[:m])

    def trace(self, element: Vector) -> int:
        """Trace of multiplication by ``element`` over the prime field."""

        total = 0
        for index in range(self.degree):
            basis = tuple(1 if coordinate == index else 0 for coordinate in range(self.degree))
            total += self.multiply(element, basis)[index]
        return total % self.prime

    def trace_gram_matrix(self) -> Tuple[Tuple[int, ...], ...]:
        basis = tuple(
            tuple(1 if coordinate == index else 0 for coordinate in range(self.degree))
            for index in range(self.degree)
        )
        return tuple(
            tuple(self.trace(self.multiply(left, right)) for right in basis)
            for left in basis
        )


def _matrix_vector(matrix: Sequence[Sequence[int]], vector: Vector, prime: int) -> Vector:
    return tuple(sum(row[index] * vector[index] for index in range(len(vector))) % prime for row in matrix)


def _matrix_rank(matrix: Sequence[Sequence[int]], prime: int) -> int:
    rows = [list(row) for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column] % prime, -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            coefficient = rows[row][column] % prime
            if coefficient:
                rows[row] = [
                    (value - coefficient * pivot_value) % prime
                    for value, pivot_value in zip(rows[row], rows[rank])
                ]
        rank += 1
    return rank


@dataclass(frozen=True)
class SymplecticSpread:
    modulus: Tuple[int, ...]
    trace_gram: Tuple[Tuple[int, ...], ...]
    subspaces: Tuple[Tuple[int, ...], ...]
    colors: Tuple[int, ...]


def symplectic_spread(prime: int, rank: int, vectors: Sequence[Vector]) -> SymplecticSpread:
    """Construct the Desarguesian spread of ``F_p^(2m)`` exactly.

    With ``F_q=F_p[t]/(f)``, the trace-pairing Gram matrix H maps the field
    symplectic form ``Tr(x*y' - x'*y)`` to the standard scalar form. Thus the
    q finite-slope lines and the vertical line become totally isotropic
    m-spaces for the graph's exact coordinate convention.
    """

    field = FiniteFieldModel.create(prime, rank)
    gram = field.trace_gram_matrix()
    if _matrix_rank(gram, prime) != rank:
        raise AssertionError("trace pairing is degenerate")
    vector_index = {vector: index for index, vector in enumerate(vectors)}
    zero = (0,) * rank
    subspaces: List[Tuple[int, ...]] = []
    for slope in field.elements:
        space = []
        for x in field.elements:
            product_value = field.multiply(slope, x)
            vector = tuple(x) + _matrix_vector(gram, product_value, prime)
            space.append(vector_index[vector])
        subspaces.append(tuple(sorted(space)))
    vertical = tuple(
        sorted(vector_index[zero + _matrix_vector(gram, y, prime)] for y in field.elements)
    )
    subspaces.append(vertical)

    q = prime ** rank
    zero_index = vector_index[(0,) * (2 * rank)]
    if any(len(space) != q or zero_index not in space for space in subspaces):
        raise AssertionError("spread subspace has the wrong size")
    for i, space in enumerate(subspaces):
        if any(
            symplectic_value(prime, rank, vectors[x], vectors[y])
            for x in space
            for y in space
        ):
            raise AssertionError("spread member is not totally isotropic")
        for other in subspaces[i + 1 :]:
            if set(space).intersection(other) != {zero_index}:
                raise AssertionError("spread members meet outside zero")
    nonzero_union = set().union(*(set(space) - {zero_index} for space in subspaces))
    if nonzero_union != set(range(len(vectors))) - {zero_index}:
        raise AssertionError("spread does not partition the nonzero vectors")

    colors = [-1] * len(vectors)
    colors[zero_index] = 0
    for color, space in enumerate(subspaces):
        for vertex in space:
            if vertex == zero_index:
                continue
            if colors[vertex] != -1:
                raise AssertionError("spread color was assigned twice")
            colors[vertex] = color
    if any(color < 0 for color in colors):
        raise AssertionError("spread coloring is incomplete")
    return SymplecticSpread(field.modulus, gram, tuple(subspaces), tuple(colors))


def normalize_projective(vector: Vector, prime: int) -> Vector:
    first = next((value for value in vector if value), None)
    if first is None:
        raise ValueError("zero has no projective normalization")
    inverse = pow(first, -1, prime)
    return tuple(value * inverse % prime for value in vector)


def projective_symplectic_graph(prime: int, rank: int) -> Tuple[Tuple[Vector, ...], Tuple[int, ...]]:
    representatives = tuple(
        vector
        for vector in quotient_vectors(prime, rank)
        if any(vector) and normalize_projective(vector, prime) == vector
    )
    adjacency = []
    for left in representatives:
        mask = 0
        for index, right in enumerate(representatives):
            if symplectic_value(prime, rank, left, right):
                mask |= 1 << index
        adjacency.append(mask)
    return representatives, tuple(adjacency)


@dataclass(frozen=True)
class FixedCliqueResult:
    exists: bool
    witness: Tuple[int, ...]
    search_nodes: int
    cache_hits: int


def fixed_size_clique(adjacency: Sequence[int], target: int) -> FixedCliqueResult:
    """Independent include/exclude decision recursion for a target clique.

    This deliberately does not use the color bounds or branching recurrence of
    ``maximum_clique``. Every target clique either contains the selected vertex
    (first branch) or omits it (second branch), which makes a false result an
    exhaustive certificate when the routine is rerun.
    """

    nodes = 0
    hits = 0
    cache: Dict[Tuple[int, int], Optional[Tuple[int, ...]]] = {}

    def search(candidates: int, need: int) -> Optional[Tuple[int, ...]]:
        nonlocal nodes, hits
        key = (candidates, need)
        if key in cache:
            hits += 1
            return cache[key]
        nodes += 1
        if need == 0:
            result: Optional[Tuple[int, ...]] = ()
        elif _popcount(candidates) < need:
            result = None
        else:
            vertices = [vertex for vertex in range(len(adjacency)) if candidates & (1 << vertex)]
            selected = max(vertices, key=lambda vertex: _popcount(candidates & adjacency[vertex]))
            with_selected = search(candidates & adjacency[selected], need - 1)
            if with_selected is not None:
                result = (selected,) + with_selected
            else:
                result = search(candidates & ~(1 << selected), need)
        cache[key] = result
        return result

    witness = search((1 << len(adjacency)) - 1, target)
    return FixedCliqueResult(witness is not None, witness or (), nodes, hits)


def multiplication_table_sha256(group: FiniteGroup) -> str:
    digest = hashlib.sha256()
    for row in group.table:
        digest.update((",".join(str(value) for value in row) + "\n").encode("ascii"))
    return digest.hexdigest()


def analyze_scalar_symplectic(prime: int, rank: int) -> Dict[str, object]:
    """Compute redundant exact certificates for one scalar symplectic group."""

    group = extraspecial_prime_group(prime, rank)
    group.validate()
    vectors, direct_adjacency = scalar_symplectic_adjacency(prime, rank)
    graph = compressed_noncommuting_graph(group)
    expected_cosets = tuple(
        tuple(range(vertex * prime, (vertex + 1) * prime))
        for vertex in range(len(vectors))
    )
    if graph.cosets != expected_cosets:
        raise AssertionError("central cosets do not match quotient-vector ordering")
    if graph.adjacency != direct_adjacency:
        raise AssertionError("group commutation and scalar symplectic adjacency disagree")

    clique = maximum_clique(graph.adjacency)
    coloring = exact_chromatic_number(graph.adjacency, clique.size)
    if not verify_clique(graph.adjacency, clique.vertices):
        raise AssertionError("clique witness failed")
    if not verify_coloring(graph.adjacency, coloring.colors):
        raise AssertionError("exact coloring witness failed")

    spread = symplectic_spread(prime, rank, vectors)
    if not verify_coloring(graph.adjacency, spread.colors):
        raise AssertionError("spread coloring failed")
    spread_subgroups = tuple(
        tuple(element for vertex in space for element in graph.cosets[vertex])
        for space in spread.subspaces
    )
    if not verify_abelian_cover(group, spread_subgroups):
        raise AssertionError("spread preimages are not an abelian subgroup cover")
    generated_cover = abelian_subgroups_from_coloring(group, graph, spread.colors)
    if not verify_abelian_cover(group, generated_cover):
        raise AssertionError("spread coloring did not generate an abelian cover")

    projective_vectors, projective_adjacency = projective_symplectic_graph(prime, rank)
    projective_index = {vector: index for index, vector in enumerate(projective_vectors)}
    vector_to_projective = [
        -1 if not any(vector) else projective_index[normalize_projective(vector, prime)]
        for vector in vectors
    ]
    for left, vector_left in enumerate(vectors):
        if not any(vector_left):
            continue
        i = vector_to_projective[left]
        for right, vector_right in enumerate(vectors):
            if not any(vector_right):
                continue
            j = vector_to_projective[right]
            if bool(graph.adjacency[left] & (1 << right)) != bool(projective_adjacency[i] & (1 << j)):
                raise AssertionError("projective twin compression changed adjacency")
    exclusion = fixed_size_clique(projective_adjacency, clique.size + 1)
    if exclusion.exists:
        raise AssertionError("independent clique exclusion contradicts maximum-clique result")

    q = prime ** rank
    counting_lower_bound = q + 1
    if coloring.size != counting_lower_bound or len(spread.subspaces) != counting_lower_bound:
        raise AssertionError("exact coloring and isotropic-spread count disagree")
    candidate_bound = max(clique.size, 2 ** ((clique.size - 1) // 2) + 1)

    return {
        "status": "[COMPUTED]",
        "prime": prime,
        "rank": rank,
        "group_id": group.group_id,
        "group_order": group.order,
        "multiplication_table_sha256": multiplication_table_sha256(group),
        "center_order": len(group.center()),
        "compressed_vertex_count": graph.order,
        "commuting_probability": str(commuting_probability(group)),
        "quotient_vectors": [list(vector) for vector in vectors],
        "compressed_adjacency": [
            [neighbor for neighbor in range(graph.order) if mask & (1 << neighbor)]
            for mask in graph.adjacency
        ],
        "nu": clique.size,
        "a": coloring.size,
        "candidate_bound": candidate_bound,
        "candidate_bound_slack": candidate_bound - coloring.size,
        "candidate_bound_status": "[DISPROVED]" if coloring.size > candidate_bound else "[COMPUTED]",
        "clique_certificate": {
            "vertices": list(clique.vertices),
            "vectors": [list(vectors[vertex]) for vertex in clique.vertices],
            "search_nodes": clique.search_nodes,
        },
        "exact_coloring_certificate": {
            "colors": list(coloring.colors),
            "search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
        },
        "projective_clique_exclusion": {
            "projective_vertex_count": len(projective_vectors),
            "representatives": [list(vector) for vector in projective_vectors],
            "adjacency": [
                [neighbor for neighbor in range(len(projective_vectors)) if mask & (1 << neighbor)]
                for mask in projective_adjacency
            ],
            "excluded_clique_size": clique.size + 1,
            "exists": exclusion.exists,
            "search_nodes": exclusion.search_nodes,
            "cache_hits": exclusion.cache_hits,
        },
        "isotropic_counting_lower_bound": counting_lower_bound,
        "spread_certificate": {
            "field_modulus_low_to_high": list(spread.modulus),
            "trace_gram": [list(row) for row in spread.trace_gram],
            "subspace_vertices": [list(space) for space in spread.subspaces],
            "colors": list(spread.colors),
            "abelian_subgroup_element_indices": [list(subgroup) for subgroup in spread_subgroups],
            "generated_abelian_subgroup_element_indices": [list(subgroup) for subgroup in generated_cover],
        },
    }
