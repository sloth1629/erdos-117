"""Exact rank-four pencil certificate in ``Alt(6,2)``.

The load-bearing check is a direct loop over all 5,471 normalized pencils
``<beta,gamma>`` in which none of the three nonzero forms has rank six.  For
each such pencil, either its common radical is exactly ``rad(beta)`` or the
stored vertices form an eight-clique.  A full stabilizer-orbit table is also
computed as a compact cross-check, but completeness does not depend on orbit
generation.
"""

from __future__ import annotations

from collections import Counter, deque
from typing import Dict, Iterable, Sequence, Set, Tuple

from exact_invariants import maximum_clique, verify_clique
from h7_c2_6_pencils import (
    FORM_COUNT,
    FORM_DIMENSION,
    FORM_PAIRS,
    FORM_RANKS,
    PARITY,
    VECTOR_COUNT,
    VECTOR_DIMENSION,
    WEDGES,
    greedy_target_clique,
    transform_form,
    transform_form_from_basis,
)


NONDEGENERATE_COORDINATES = (0, 1, 3, 4)
RADICAL_COORDINATES = (2, 5)
BETA = sum(1 << FORM_PAIRS.index(pair) for pair in ((0, 3), (1, 4)))


def form_value(form: int, left: int, right: int) -> int:
    return PARITY[form & WEDGES[left][right]]


def form_radical(form: int) -> Tuple[int, ...]:
    return tuple(
        vector for vector in range(VECTOR_COUNT)
        if all(form_value(form, vector, target) == 0 for target in range(VECTOR_COUNT))
    )


BETA_RADICAL = form_radical(BETA)


def normalized_gammas() -> Iterable[int]:
    for gamma in range(1, FORM_COUNT):
        if gamma != BETA and gamma < (gamma ^ BETA):
            yield gamma


def normalize_gamma(gamma: int) -> int:
    if gamma in (0, BETA):
        raise ValueError("gamma does not span a pencil with beta")
    return min(gamma, gamma ^ BETA)


def pencil_rank_profile(gamma: int) -> Tuple[int, int, int]:
    return tuple(sorted((FORM_RANKS[BETA], FORM_RANKS[gamma], FORM_RANKS[BETA ^ gamma])))


def pencil_graph(gamma: int) -> Tuple[int, ...]:
    if gamma in (0, BETA) or not 0 <= gamma < FORM_COUNT:
        raise ValueError("gamma does not span a pencil with beta")
    adjacency = []
    for row in WEDGES:
        mask = 0
        for target, wedge in enumerate(row):
            if PARITY[BETA & wedge] or PARITY[gamma & wedge]:
                mask |= 1 << target
        adjacency.append(mask)
    return tuple(adjacency)


def common_radical(adjacency: Sequence[int]) -> Tuple[int, ...]:
    return tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0)


def linear_image_from_basis(basis_images: Sequence[int], vector: int) -> int:
    image = 0
    for coordinate, basis_image in enumerate(basis_images):
        if vector & (1 << coordinate):
            image ^= basis_image
    return image


def stabilizer_generators() -> Tuple[Tuple[int, ...], ...]:
    """Explicit generators of ``2^8 : (Sp(4,2) x GL(2,2))``.

    The 15 symplectic transvections generate ``Sp(4,2)`` on the
    nondegenerate quotient, the eight shears generate ``Hom(U,rad(beta))``,
    and swap plus one transvection generate ``GL(2,2)`` on the radical.
    Each record is the list of images of the six coordinate vectors.
    """

    identity = tuple(1 << coordinate for coordinate in range(VECTOR_DIMENSION))
    generators = []
    for coefficients in range(1, 1 << len(NONDEGENERATE_COORDINATES)):
        vector = sum(
            1 << coordinate
            for bit, coordinate in enumerate(NONDEGENERATE_COORDINATES)
            if coefficients & (1 << bit)
        )
        generators.append(tuple(
            basis ^ vector if form_value(BETA, basis, vector) else basis
            for basis in identity
        ))
    for source in NONDEGENERATE_COORDINATES:
        for radical in RADICAL_COORDINATES:
            images = list(identity)
            images[source] ^= 1 << radical
            generators.append(tuple(images))
    images = list(identity)
    images[RADICAL_COORDINATES[0]], images[RADICAL_COORDINATES[1]] = (
        images[RADICAL_COORDINATES[1]], images[RADICAL_COORDINATES[0]]
    )
    generators.append(tuple(images))
    images = list(identity)
    images[RADICAL_COORDINATES[0]] ^= 1 << RADICAL_COORDINATES[1]
    generators.append(tuple(images))

    for generator in generators:
        vector_images = tuple(
            linear_image_from_basis(generator, vector) for vector in range(VECTOR_COUNT)
        )
        if len(set(vector_images)) != VECTOR_COUNT:
            raise AssertionError("stabilizer generator is singular")
        if transform_form(BETA, vector_images) != BETA:
            raise AssertionError("generator does not stabilize beta")
    if len(generators) != 25:
        raise AssertionError("wrong stabilizer generator count")
    return tuple(generators)


STABILIZER_BASIS_IMAGES = stabilizer_generators()
STABILIZER_VECTOR_IMAGES = tuple(
    tuple(linear_image_from_basis(generator, vector) for vector in range(VECTOR_COUNT))
    for generator in STABILIZER_BASIS_IMAGES
)
STABILIZER_FORM_IMAGES = tuple(
    tuple(transform_form(1 << bit, vector_images) for bit in range(FORM_DIMENSION))
    for vector_images in STABILIZER_VECTOR_IMAGES
)


def pencil_orbit(gamma: int) -> Set[int]:
    representative = normalize_gamma(gamma)
    orbit = {representative}
    queue = deque([representative])
    while queue:
        current = queue.popleft()
        for form_images in STABILIZER_FORM_IMAGES:
            image = normalize_gamma(transform_form_from_basis(current, form_images))
            if image not in orbit:
                orbit.add(image)
                queue.append(image)
    return orbit


def verify_graph_transport(gamma: int, generator_index: int) -> None:
    form_images = STABILIZER_FORM_IMAGES[generator_index]
    image = normalize_gamma(transform_form_from_basis(gamma, form_images))
    permutation = STABILIZER_VECTOR_IMAGES[generator_index]
    source_graph = pencil_graph(gamma)
    image_graph = pencil_graph(image)
    for left in range(VECTOR_COUNT):
        for right in range(VECTOR_COUNT):
            if bool(image_graph[left] & (1 << right)) != bool(
                source_graph[permutation[left]] & (1 << permutation[right])
            ):
                raise AssertionError("stabilizer action did not transport the graph")


def exact_certificate() -> Dict[str, object]:
    if FORM_RANKS[BETA] != 4 or BETA_RADICAL != (0, 4, 32, 36):
        raise AssertionError("wrong standard rank-four form or radical")
    gammas = tuple(normalized_gammas())
    if len(gammas) != 16383:
        raise AssertionError("normalized pencil enumeration is incomplete")

    no_rank_six = tuple(
        gamma for gamma in gammas
        if FORM_RANKS[gamma] <= 4 and FORM_RANKS[BETA ^ gamma] <= 4
    )
    if len(no_rank_six) != 5471:
        raise AssertionError("wrong no-rank-six pencil count")
    profile_counts = Counter(pencil_rank_profile(gamma) for gamma in no_rank_six)
    expected_profiles = {
        (2, 2, 4): 10,
        (2, 4, 4): 375,
        (4, 4, 4): 5086,
    }
    if profile_counts != expected_profiles:
        raise AssertionError("wrong no-rank-six profile distribution")

    direct_records = []
    outcome_counts = Counter()
    for gamma in no_rank_six:
        adjacency = pencil_graph(gamma)
        radical = common_radical(adjacency)
        clique = greedy_target_clique(adjacency, 8)
        if clique:
            status = "clique_ge_8"
            witness = clique
            if len(witness) != 8 or not verify_clique(adjacency, witness):
                raise AssertionError("direct rank-four pencil dichotomy failed")
        elif radical == BETA_RADICAL:
            status = "common_radical_equals_beta_radical"
            witness = radical
        else:
            raise AssertionError("direct rank-four pencil dichotomy failed")
        outcome_counts[status] += 1
        direct_records.append({
            "gamma": gamma,
            "rank_profile": list(pencil_rank_profile(gamma)),
            "status": status,
            "witness": list(witness),
        })
    if outcome_counts != {
        "clique_ge_8": 5450,
        "common_radical_equals_beta_radical": 21,
    }:
        raise AssertionError("unexpected direct dichotomy counts: %r" % outcome_counts)

    unseen = set(gammas)
    orbit_records = []
    while unseen:
        representative = min(unseen)
        orbit = pencil_orbit(representative)
        if not orbit <= unseen:
            raise AssertionError("stabilizer pencil orbits overlap")
        unseen -= orbit
        adjacency = pencil_graph(representative)
        clique = maximum_clique(adjacency)
        if not verify_clique(adjacency, clique.vertices):
            raise AssertionError("exact orbit clique certificate failed")
        orbit_records.append({
            "representative_gamma": representative,
            "orbit_size": len(orbit),
            "rank_profile": list(pencil_rank_profile(representative)),
            "common_radical": list(common_radical(adjacency)),
            "omega": clique.size,
            "clique_certificate": list(clique.vertices),
            "clique_search_nodes": clique.search_nodes,
            "adjacency": list(adjacency),
        })
    if len(orbit_records) != 12 or sum(record["orbit_size"] for record in orbit_records) != 16383:
        raise AssertionError("unexpected rank-four stabilizer orbit partition")
    for record in orbit_records:
        for generator_index in range(len(STABILIZER_FORM_IMAGES)):
            verify_graph_transport(record["representative_gamma"], generator_index)

    relevant_orbits = [
        record for record in orbit_records if max(record["rank_profile"]) <= 4
    ]
    if len(relevant_orbits) != 7 or sum(record["orbit_size"] for record in relevant_orbits) != 5471:
        raise AssertionError("orbit compression disagrees with direct relevant set")
    low_orbits = [record for record in relevant_orbits if record["omega"] <= 7]
    if len(low_orbits) != 2 or any(tuple(record["common_radical"]) != BETA_RADICAL for record in low_orbits):
        raise AssertionError("low-clique orbit radical assertion failed")
    return {
        "field_order": 2,
        "vector_dimension": VECTOR_DIMENSION,
        "alternating_form_dimension": FORM_DIMENSION,
        "standard_rank_four_beta": BETA,
        "beta_radical": list(BETA_RADICAL),
        "normalized_pencil_count": len(gammas),
        "no_rank_six_pencil_count": len(no_rank_six),
        "no_rank_six_rank_profile_distribution": [
            {"ranks": list(profile), "count": count}
            for profile, count in sorted(profile_counts.items())
        ],
        "direct_dichotomy_distribution": dict(sorted(outcome_counts.items())),
        "direct_dichotomy_records": direct_records,
        "stabilizer_structure": "2^8 : (Sp(4,2) x GL(2,2))",
        "stabilizer_order": 256 * 720 * 6,
        "stabilizer_generator_count": len(STABILIZER_FORM_IMAGES),
        "stabilizer_orbit_count": len(orbit_records),
        "stabilizer_orbit_size_sum": sum(record["orbit_size"] for record in orbit_records),
        "relevant_orbit_count": len(relevant_orbits),
        "relevant_orbit_size_sum": sum(record["orbit_size"] for record in relevant_orbits),
        "low_orbit_representatives": [record["representative_gamma"] for record in low_orbits],
        "orbits": orbit_records,
    }
