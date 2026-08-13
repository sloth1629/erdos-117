"""Independent finite-linear-algebra certificate for the C2^5 h(6) case.

For a kernel K in exterior square Lambda^2(V), put L=ann(K) in the
alternating forms on V=F_2^5.  The graph joins x,y when some form in L is
nonzero on (x,y).  This module verifies that every L with zero common radical
has a clique of size at least nine, without enumerating all 229,755,605
subspaces of the ten-dimensional exterior square.
"""

from __future__ import annotations

from collections import Counter, deque
from typing import Dict, Iterable, List, Sequence, Set, Tuple

from exact_invariants import exact_chromatic_number, maximum_clique, verify_clique, verify_coloring


VECTOR_DIMENSION = 5
FORM_DIMENSION = 10
NONZERO_VECTORS = tuple(range(1, 1 << VECTOR_DIMENSION))
FORM_PAIRS = tuple(
    (i, j)
    for i in range(VECTOR_DIMENSION)
    for j in range(i + 1, VECTOR_DIMENSION)
)
PARITY = tuple(bin(value).count("1") % 2 for value in range(1 << FORM_DIMENSION))


def wedge_vector(x: int, y: int) -> int:
    result = 0
    for bit, (i, j) in enumerate(FORM_PAIRS):
        value = (((x >> i) & 1) & ((y >> j) & 1)) ^ (
            ((x >> j) & 1) & ((y >> i) & 1)
        )
        if value:
            result |= 1 << bit
    return result


WEDGES = tuple(
    tuple(wedge_vector(x, y) for y in NONZERO_VECTORS)
    for x in NONZERO_VECTORS
)


def alternating_rank(form: int) -> int:
    rows = [0] * VECTOR_DIMENSION
    for bit, (i, j) in enumerate(FORM_PAIRS):
        if form & (1 << bit):
            rows[i] |= 1 << j
            rows[j] |= 1 << i
    rank = 0
    for column in range(VECTOR_DIMENSION):
        pivot = next(
            (row for row in range(rank, VECTOR_DIMENSION) if rows[row] & (1 << column)),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for row in range(VECTOR_DIMENSION):
            if row != rank and rows[row] & (1 << column):
                rows[row] ^= rows[rank]
        rank += 1
    return rank


FORM_RANKS = tuple(alternating_rank(form) for form in range(1 << FORM_DIMENSION))


def radical_mask(form: int) -> int:
    result = 0
    for vertex, row in enumerate(WEDGES):
        if all(PARITY[form & wedge] == 0 for wedge in row):
            result |= 1 << vertex
    return result


RADICAL_MASKS = tuple(radical_mask(form) for form in range(1 << FORM_DIMENSION))


def canonical_pencils() -> Iterable[Tuple[int, int]]:
    """Yield each two-dimensional form subspace once as its two least elements."""

    for a in range(1, 1 << FORM_DIMENSION):
        for b in range(a + 1, 1 << FORM_DIMENSION):
            if b < (a ^ b):
                yield a, b


def pencil_rank_profile(a: int, b: int) -> Tuple[int, int, int]:
    return tuple(sorted((FORM_RANKS[a], FORM_RANKS[b], FORM_RANKS[a ^ b])))


def pencil_common_radical_zero(a: int, b: int) -> bool:
    return RADICAL_MASKS[a] & RADICAL_MASKS[b] == 0


def canonical_pencil(forms: Sequence[int]) -> Tuple[int, int]:
    nonzero = sorted(set(forms) - {0})
    if len(nonzero) != 3 or nonzero[0] ^ nonzero[1] != nonzero[2]:
        raise ValueError("forms do not describe a two-dimensional pencil")
    return nonzero[0], nonzero[1]


def add_to_basis(state: Tuple[int, ...], value: int) -> Tuple[int, ...]:
    rows = list(state)
    for pivot in range(FORM_DIMENSION - 1, -1, -1):
        if value & (1 << pivot) and rows[pivot]:
            value ^= rows[pivot]
    if value == 0:
        return state
    pivot = value.bit_length() - 1
    for row in range(FORM_DIMENSION):
        if rows[row] & (1 << pivot):
            rows[row] ^= value
    rows[pivot] = value
    return tuple(rows)


def subspace_elements(state: Sequence[int]) -> Tuple[int, ...]:
    result = [0]
    for row in state:
        if row:
            result += [value ^ row for value in result]
    return tuple(result)


def canonical_form_subspace(forms: Sequence[int]) -> Tuple[int, ...]:
    state = (0,) * FORM_DIMENSION
    for form in forms:
        state = add_to_basis(state, form)
    return state


def form_graph(forms: Sequence[int]) -> Tuple[int, ...]:
    nonzero_forms = tuple(form for form in forms if form)
    adjacency = []
    for row in WEDGES:
        mask = 0
        for target, wedge in enumerate(row):
            if any(PARITY[form & wedge] for form in nonzero_forms):
                mask |= 1 << target
        adjacency.append(mask)
    return tuple(adjacency)


def transvection_tables() -> Tuple[Tuple[int, ...], ...]:
    """Return pullback actions for all elementary transvections of F_2^5."""

    tables = []
    for source in range(VECTOR_DIMENSION):
        for added in range(VECTOR_DIMENSION):
            if source == added:
                continue
            images = [1 << index for index in range(VECTOR_DIMENSION)]
            images[source] ^= 1 << added
            coordinate_images = []
            for basis_form in range(FORM_DIMENSION):
                transformed = 0
                for bit, (i, j) in enumerate(FORM_PAIRS):
                    wedge = wedge_vector(images[i], images[j])
                    if wedge & (1 << basis_form):
                        transformed |= 1 << bit
                coordinate_images.append(transformed)
            table = []
            for form in range(1 << FORM_DIMENSION):
                transformed = 0
                for basis_form, image in enumerate(coordinate_images):
                    if form & (1 << basis_form):
                        transformed ^= image
                table.append(transformed)
            tables.append(tuple(table))
    return tuple(tables)


TRANSVECTION_TABLES = transvection_tables()


def pencil_orbit(representative: Tuple[int, int]) -> Set[Tuple[int, int]]:
    seen = {representative}
    queue = deque([representative])
    while queue:
        a, b = queue.popleft()
        forms = (a, b, a ^ b)
        for table in TRANSVECTION_TABLES:
            image = canonical_pencil(tuple(table[form] for form in forms))
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return seen


def form_subspace_orbit(representative: Tuple[int, ...]) -> Set[Tuple[int, ...]]:
    seen = {representative}
    queue = deque([representative])
    while queue:
        state = queue.popleft()
        basis = tuple(form for form in state if form)
        for table in TRANSVECTION_TABLES:
            image = canonical_form_subspace(tuple(table[form] for form in basis))
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return seen


def enumerate_rank_two_subspaces() -> Set[Tuple[int, ...]]:
    """Enumerate subspaces whose every nonzero alternating form has rank two."""

    rank_two_forms = tuple(form for form in range(1, 1 << FORM_DIMENSION) if FORM_RANKS[form] == 2)
    zero = (0,) * FORM_DIMENSION
    seen = {zero}
    queue = deque([zero])
    while queue:
        state = queue.popleft()
        elements = subspace_elements(state)
        element_set = set(elements)
        for form in rank_two_forms:
            if form in element_set:
                continue
            if all(FORM_RANKS[form ^ element] == 2 for element in elements):
                child = add_to_basis(state, form)
                if child not in seen:
                    seen.add(child)
                    queue.append(child)
    return seen


def common_radical_mask(forms: Sequence[int]) -> int:
    result = (1 << len(NONZERO_VECTORS)) - 1
    for form in forms:
        if form:
            result &= RADICAL_MASKS[form]
    return result


def independent_certificate() -> Dict[str, object]:
    """Recompute the complete orbit/subspace certificate in pure Python."""

    profile_sets: Dict[Tuple[int, int, int], Set[Tuple[int, int]]] = {
        (2, 4, 4): set(),
        (4, 4, 4): set(),
    }
    pencil_count = 0
    for a, b in canonical_pencils():
        pencil_count += 1
        if pencil_common_radical_zero(a, b):
            profile = pencil_rank_profile(a, b)
            if profile not in profile_sets:
                raise AssertionError("unexpected common-radical-zero rank profile")
            profile_sets[profile].add((a, b))
    if pencil_count != 174251:
        raise AssertionError("Gaussian-binomial pencil count failed")

    pencil_records = []
    for profile in ((2, 4, 4), (4, 4, 4)):
        representative = min(profile_sets[profile])
        orbit = pencil_orbit(representative)
        if orbit != profile_sets[profile]:
            raise AssertionError("transvection orbit does not exhaust its rank profile")
        graph = form_graph(representative)
        clique = maximum_clique(graph)
        coloring = exact_chromatic_number(graph, clique.size)
        if not verify_clique(graph, clique.vertices) or not verify_coloring(graph, coloring.colors):
            raise AssertionError("representative graph witness failed")
        pencil_records.append(
            {
                "rank_profile": list(profile),
                "pencil_count": len(orbit),
                "representative": list(representative),
                "omega": clique.size,
                "chi": coloring.size,
                "clique_certificate_vectors": [NONZERO_VECTORS[v] for v in clique.vertices],
                "coloring_certificate": list(coloring.colors),
                "clique_search_nodes": clique.search_nodes,
                "coloring_search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
            }
        )

    rank_two_subspaces = enumerate_rank_two_subspaces()
    dimension_distribution = Counter(
        sum(bool(form) for form in state) for state in rank_two_subspaces
    )
    radical_distribution = Counter(
        (
            sum(bool(form) for form in state),
            bin(common_radical_mask(state)).count("1"),
        )
        for state in rank_two_subspaces
    )
    radical_zero = {
        state for state in rank_two_subspaces if common_radical_mask(state) == 0
    }
    if len(radical_zero) != 31:
        raise AssertionError("unexpected all-rank-two radical-zero count")
    rank_two_representative = min(radical_zero)
    if form_subspace_orbit(rank_two_representative) != radical_zero:
        raise AssertionError("rank-two radical-zero spaces are not one transvection orbit")
    graph = form_graph(rank_two_representative)
    clique = maximum_clique(graph)
    coloring = exact_chromatic_number(graph, clique.size)
    if not verify_clique(graph, clique.vertices) or not verify_coloring(graph, coloring.colors):
        raise AssertionError("rank-two representative witness failed")

    return {
        "vector_dimension": VECTOR_DIMENSION,
        "form_dimension": FORM_DIMENSION,
        "pencil_count": pencil_count,
        "common_radical_zero_pencil_count": sum(map(len, profile_sets.values())),
        "pencil_orbits": pencil_records,
        "rank_two_form_count": sum(rank == 2 for rank in FORM_RANKS),
        "rank_two_subspace_count": len(rank_two_subspaces),
        "rank_two_subspace_dimension_distribution": [
            {"dimension": dimension, "count": count}
            for dimension, count in sorted(dimension_distribution.items())
        ],
        "rank_two_subspace_radical_distribution": [
            {"dimension": key[0], "nonzero_common_radical_vectors": key[1], "count": count}
            for key, count in sorted(radical_distribution.items())
        ],
        "rank_two_radical_zero_orbit": {
            "subspace_count": len(radical_zero),
            "representative_basis": [form for form in rank_two_representative if form],
            "omega": clique.size,
            "chi": coloring.size,
            "clique_certificate_vectors": [NONZERO_VECTORS[v] for v in clique.vertices],
            "coloring_certificate": list(coloring.colors),
            "clique_search_nodes": clique.search_nodes,
            "coloring_search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
        },
        "conclusion": "every zero-common-radical form subspace has clique number at least 9",
    }
