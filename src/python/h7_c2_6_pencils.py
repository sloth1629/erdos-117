"""Exact normalized pencil certificate in ``Alt(6,2)``.

Fix the standard nondegenerate alternating form ``beta`` on ``F_2^6``.
Every two-dimensional scalar-form subspace containing ``beta`` is
``<beta,gamma>`` for a unique pair ``{gamma,beta+gamma}``.  Thus the
16,383 representatives below exhaust those pencils without using a group
classification.  The associated graph joins ``x`` and ``y`` when either
scalar form is nonzero on ``(x,y)``.
"""

from __future__ import annotations

from collections import Counter, deque
from typing import Dict, Iterable, Sequence, Set, Tuple

from exact_invariants import maximum_clique, verify_clique


VECTOR_DIMENSION = 6
FORM_PAIRS = tuple(
    (left, right)
    for left in range(VECTOR_DIMENSION)
    for right in range(left + 1, VECTOR_DIMENSION)
)
FORM_DIMENSION = len(FORM_PAIRS)
VECTOR_COUNT = 1 << VECTOR_DIMENSION
FORM_COUNT = 1 << FORM_DIMENSION
PARITY = tuple(bin(value).count("1") % 2 for value in range(FORM_COUNT))


def wedge_vector(left: int, right: int) -> int:
    result = 0
    for bit, (i, j) in enumerate(FORM_PAIRS):
        if (((left >> i) & 1) & ((right >> j) & 1)) ^ (
            ((left >> j) & 1) & ((right >> i) & 1)
        ):
            result |= 1 << bit
    return result


WEDGES = tuple(
    tuple(wedge_vector(left, right) for right in range(VECTOR_COUNT))
    for left in range(VECTOR_COUNT)
)


def standard_symplectic_form() -> int:
    """Return the form pairing coordinates ``i`` and ``i+3``."""

    return sum(
        1 << FORM_PAIRS.index((index, index + VECTOR_DIMENSION // 2))
        for index in range(VECTOR_DIMENSION // 2)
    )


BETA = standard_symplectic_form()


def alternating_rank(form: int) -> int:
    if not 0 <= form < FORM_COUNT:
        raise ValueError("form code is out of range")
    rows = [0] * VECTOR_DIMENSION
    for bit, (left, right) in enumerate(FORM_PAIRS):
        if form & (1 << bit):
            rows[left] |= 1 << right
            rows[right] |= 1 << left
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


FORM_RANKS = tuple(alternating_rank(form) for form in range(FORM_COUNT))


def normalized_gammas() -> Iterable[int]:
    """Yield one gamma from each pair ``{gamma,beta+gamma}``."""

    for gamma in range(1, FORM_COUNT):
        mate = gamma ^ BETA
        if gamma != BETA and gamma < mate:
            yield gamma


def pencil_rank_profile(gamma: int) -> Tuple[int, int, int]:
    return tuple(sorted((FORM_RANKS[BETA], FORM_RANKS[gamma], FORM_RANKS[BETA ^ gamma])))


def pencil_graph(gamma: int) -> Tuple[int, ...]:
    if gamma in (0, BETA) or not 0 <= gamma < FORM_COUNT:
        raise ValueError("gamma does not span a pencil with beta")
    forms = (BETA, gamma)
    adjacency = []
    for row in WEDGES:
        mask = 0
        for target, wedge in enumerate(row):
            if any(PARITY[form & wedge] for form in forms):
                mask |= 1 << target
        adjacency.append(mask)
    return tuple(adjacency)


def form_value(form: int, left: int, right: int) -> int:
    return PARITY[form & WEDGES[left][right]]


def beta_value(left: int, right: int) -> int:
    return form_value(BETA, left, right)


def transvection_images(vector: int) -> Tuple[int, ...]:
    """Images of all vectors under ``x -> x + beta(x,v)v``."""

    if not 0 < vector < VECTOR_COUNT:
        raise ValueError("transvection vector must be nonzero")
    images = tuple(
        source ^ vector if beta_value(source, vector) else source
        for source in range(VECTOR_COUNT)
    )
    if len(set(images)) != VECTOR_COUNT or any(images[images[x]] != x for x in range(VECTOR_COUNT)):
        raise AssertionError("symplectic transvection is not an involutive permutation")
    return images


TRANSVECTION_IMAGES = tuple(transvection_images(vector) for vector in range(1, VECTOR_COUNT))


def transform_form(form: int, images: Sequence[int]) -> int:
    """Pull back an alternating form through a coordinate permutation."""

    transformed = 0
    for bit, (left, right) in enumerate(FORM_PAIRS):
        if form_value(form, images[1 << left], images[1 << right]):
            transformed |= 1 << bit
    return transformed


TRANSVECTION_FORM_IMAGES = tuple(
    tuple(transform_form(1 << bit, images) for bit in range(FORM_DIMENSION))
    for images in TRANSVECTION_IMAGES
)


def transform_form_from_basis(form: int, basis_images: Sequence[int]) -> int:
    transformed = 0
    for bit, image in enumerate(basis_images):
        if form & (1 << bit):
            transformed ^= image
    return transformed


def normalize_gamma(gamma: int) -> int:
    if gamma in (0, BETA):
        raise ValueError("zero and beta do not define a two-dimensional pencil")
    return min(gamma, gamma ^ BETA)


def pencil_orbit(gamma: int) -> Set[int]:
    representative = normalize_gamma(gamma)
    orbit = {representative}
    queue = deque([representative])
    while queue:
        current = queue.popleft()
        for basis_images in TRANSVECTION_FORM_IMAGES:
            transformed = transform_form_from_basis(current, basis_images)
            image = normalize_gamma(transformed)
            if image not in orbit:
                orbit.add(image)
                queue.append(image)
    return orbit


def raw_gamma_orbit(gamma: int) -> Set[int]:
    """Orbit before identifying the two generators of the same pencil."""

    if gamma in (0, BETA):
        raise ValueError("gamma must be nonzero and different from beta")
    orbit = {gamma}
    queue = deque([gamma])
    while queue:
        current = queue.popleft()
        for basis_images in TRANSVECTION_FORM_IMAGES:
            image = transform_form_from_basis(current, basis_images)
            if image not in orbit:
                orbit.add(image)
                queue.append(image)
    return orbit


def verify_graph_transport(gamma: int, generator_index: int) -> None:
    images = TRANSVECTION_IMAGES[generator_index]
    transformed = normalize_gamma(
        transform_form_from_basis(gamma, TRANSVECTION_FORM_IMAGES[generator_index])
    )
    original_graph = pencil_graph(gamma)
    transformed_graph = pencil_graph(transformed)
    for left in range(VECTOR_COUNT):
        for right in range(VECTOR_COUNT):
            if bool(transformed_graph[left] & (1 << right)) != bool(
                original_graph[images[left]] & (1 << images[right])
            ):
                raise AssertionError("symplectic action did not transport pencil graph")


def greedy_target_clique(adjacency: Sequence[int], target: int) -> Tuple[int, ...]:
    """Run the same deterministic multi-start greedy search as the GAP scan."""

    starts = sorted(
        range(len(adjacency)),
        key=lambda vertex: (-bin(adjacency[vertex]).count("1"), vertex),
    )
    for start in starts:
        clique = [start]
        candidates = adjacency[start]
        while candidates and len(clique) < target:
            vertices = tuple(
                vertex for vertex in range(len(adjacency))
                if candidates & (1 << vertex)
            )
            vertex = min(
                vertices,
                key=lambda choice: (
                    -bin(candidates & adjacency[choice]).count("1"), choice
                ),
            )
            clique.append(vertex)
            candidates &= adjacency[vertex]
        if len(clique) == target:
            return tuple(clique)
    return ()


def exact_certificate() -> Dict[str, object]:
    gammas = tuple(normalized_gammas())
    if len(gammas) != 16383 or len({frozenset((gamma, gamma ^ BETA)) for gamma in gammas}) != 16383:
        raise AssertionError("normalized pencil enumeration is incomplete")
    if FORM_RANKS[BETA] != VECTOR_DIMENSION:
        raise AssertionError("beta is not nondegenerate")

    profile_counts = Counter()
    for gamma in gammas:
        profile = pencil_rank_profile(gamma)
        profile_counts[profile] += 1
        adjacency = pencil_graph(gamma)
        # Nondegeneracy of beta makes the common radical exactly {0}.
        if tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0) != (0,):
            raise AssertionError("pencil graph has a nonzero common radical")
        witness = greedy_target_clique(adjacency, 8)
        if len(witness) != 8 or not verify_clique(adjacency, witness):
            raise AssertionError("normalized pencil has no certified 8-clique")
    expected_profiles = {
        (2, 4, 6): 336,
        (2, 6, 6): 315,
        (4, 4, 6): 5040,
        (4, 6, 6): 7812,
        (6, 6, 6): 2880,
    }
    if profile_counts != expected_profiles:
        raise AssertionError("unexpected normalized-pencil rank distribution")

    raw_unseen = set(range(1, FORM_COUNT)) - {BETA}
    raw_orbit_records = []
    while raw_unseen:
        representative = min(raw_unseen)
        orbit = raw_gamma_orbit(representative)
        if not orbit <= raw_unseen:
            raise AssertionError("raw symplectic gamma orbits overlap")
        raw_unseen -= orbit
        raw_orbit_records.append({
            "representative_gamma": representative,
            "orbit_size": len(orbit),
            "gamma_rank": FORM_RANKS[representative],
            "beta_plus_gamma_rank": FORM_RANKS[BETA ^ representative],
        })
    if len(raw_orbit_records) != 12 or sum(record["orbit_size"] for record in raw_orbit_records) != 32766:
        raise AssertionError("unexpected raw symplectic gamma orbit partition")

    unseen = set(gammas)
    orbit_records = []
    while unseen:
        representative = min(unseen)
        orbit = pencil_orbit(representative)
        if not orbit <= unseen:
            raise AssertionError("symplectic pencil orbits overlap")
        unseen -= orbit
        adjacency = pencil_graph(representative)
        clique = maximum_clique(adjacency)
        if not verify_clique(adjacency, clique.vertices):
            raise AssertionError("exact maximum-clique certificate failed")
        orbit_records.append({
            "representative_gamma": representative,
            "orbit_size": len(orbit),
            "rank_profile": list(pencil_rank_profile(representative)),
            "omega": clique.size,
            "clique_certificate": list(clique.vertices),
            "clique_search_nodes": clique.search_nodes,
            "adjacency": list(adjacency),
        })

    if len(orbit_records) != 6 or sum(record["orbit_size"] for record in orbit_records) != 16383:
        raise AssertionError("unexpected symplectic pencil orbit partition")
    for record in orbit_records:
        representative = record["representative_gamma"]
        for generator_index in range(len(TRANSVECTION_IMAGES)):
            verify_graph_transport(representative, generator_index)
    minimum_omega = min(record["omega"] for record in orbit_records)
    if minimum_omega < 8:
        raise AssertionError("8-clique scan and orbit exact invariants disagree")
    invariant_distribution = Counter(
        (record["omega"], tuple(record["rank_profile"]))
        for record in orbit_records
    )
    return {
        "field_order": 2,
        "vector_dimension": VECTOR_DIMENSION,
        "alternating_form_dimension": FORM_DIMENSION,
        "vertex_count": VECTOR_COUNT,
        "standard_nondegenerate_beta": BETA,
        "normalized_pencil_count": len(gammas),
        "symplectic_transvection_generator_count": len(TRANSVECTION_IMAGES),
        # Adding the fixed singleton orbits {0} and {beta} gives all 14 raw
        # form orbits; only the 12 below occur in genuine pencils.
        "all_raw_form_orbit_count_including_zero_and_beta": len(raw_orbit_records) + 2,
        "nontrivial_raw_gamma_orbit_count": len(raw_orbit_records),
        "raw_gamma_orbit_size_sum": sum(record["orbit_size"] for record in raw_orbit_records),
        "raw_gamma_orbits": raw_orbit_records,
        "symplectic_pencil_orbit_count": len(orbit_records),
        "symplectic_pencil_orbit_size_sum": sum(record["orbit_size"] for record in orbit_records),
        "rank_profile_distribution": [
            {"ranks": list(profile), "count": count}
            for profile, count in sorted(profile_counts.items())
        ],
        "minimum_omega": minimum_omega,
        "orbit_invariant_distribution": [
            {
                "omega": omega,
                "rank_profile": list(profile),
                "orbit_count": count,
            }
            for (omega, profile), count in sorted(invariant_distribution.items())
        ],
        "pencil_orbits": orbit_records,
    }
