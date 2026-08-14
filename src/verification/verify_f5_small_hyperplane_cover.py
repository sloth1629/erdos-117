#!/usr/bin/env python3
"""Verify the small F_5 hyperplane-cover lemma used at cutoff eight.

After a spanning blocking set is normalized to contain the coordinate
points, only projective vectors with every coordinate nonzero remain to be
covered.  Dimensions two through four are small enough for an exhaustive
check.  Dimensions at least five are excluded by the elementary incidence
bound recorded in the accompanying note.
"""

from __future__ import annotations

import json
from itertools import combinations, product
from typing import Dict, Iterable, List, Sequence, Set, Tuple


PRIME = 5
Vector = Tuple[int, ...]


def normalize(vector: Sequence[int]) -> Vector:
    """Return the canonical representative of a projective point."""

    reduced = tuple(coordinate % PRIME for coordinate in vector)
    for coordinate in reduced:
        if coordinate:
            inverse = pow(coordinate, PRIME - 2, PRIME)
            return tuple((entry * inverse) % PRIME for entry in reduced)
    raise ValueError("the zero vector has no projective normalization")


def projective_points(dimension: int) -> Tuple[Vector, ...]:
    return tuple(
        sorted(
            {
                normalize(vector)
                for vector in product(range(PRIME), repeat=dimension)
                if any(vector)
            }
        )
    )


def coordinate_basis(dimension: int) -> Tuple[Vector, ...]:
    return tuple(
        tuple(1 if row == column else 0 for row in range(dimension))
        for column in range(dimension)
    )


def torus_points(dimension: int) -> Tuple[Vector, ...]:
    """Projective all-nonzero points, normalized in the first coordinate."""

    return tuple(
        (1,) + tail
        for tail in product(range(1, PRIME), repeat=dimension - 1)
    )


def dot(left: Sequence[int], right: Sequence[int]) -> int:
    return sum(a * b for a, b in zip(left, right)) % PRIME


def zero_mask(normal: Vector, torus: Sequence[Vector]) -> int:
    mask = 0
    for index, point in enumerate(torus):
        if dot(normal, point) == 0:
            mask |= 1 << index
    return mask


def population(mask: int) -> int:
    return bin(mask).count("1")


def projective_line(left: Vector, right: Vector) -> Set[Vector]:
    points: Set[Vector] = set()
    for first, second in product(range(PRIME), repeat=2):
        if first == 0 and second == 0:
            continue
        vector = tuple(
            (first * a + second * b) % PRIME
            for a, b in zip(left, right)
        )
        points.add(normalize(vector))
    return points


def contains_projective_line(points: Iterable[Vector]) -> bool:
    point_set = set(points)
    for left, right in combinations(sorted(point_set), 2):
        line = projective_line(left, right)
        if len(line) == PRIME + 1 and line.issubset(point_set):
            return True
    return False


def enumerate_dimension(dimension: int) -> Dict[str, int]:
    """Exhaust the normalized covers in dimension 2, 3, or 4."""

    if dimension not in (2, 3, 4):
        raise ValueError("only dimensions two through four are exhaustive")

    basis = coordinate_basis(dimension)
    torus = torus_points(dimension)
    full_mask = (1 << len(torus)) - 1
    candidates: List[Tuple[Vector, int, int]] = []
    for normal in projective_points(dimension):
        if normal in basis:
            continue
        mask = zero_mask(normal, torus)
        if mask:
            candidates.append((normal, mask, population(mask)))

    maximum_mask_size = max(size for _, _, size in candidates)
    maximum_extra = 8 - dimension

    # In dimension four, four extra hyperplanes must cover 64 torus points,
    # while each covers at most 16.  Thus all four masks must have maximum
    # size; smaller masks and subfamilies of size at most three are excluded
    # by cardinality before the enumeration.
    if dimension == 4:
        usable = tuple(
            candidate
            for candidate in candidates
            if candidate[2] == maximum_mask_size
        )
        subset_sizes = (4,)
    else:
        usable = tuple(candidates)
        subset_sizes = tuple(
            range(0, min(maximum_extra, len(usable)) + 1)
        )

    tested_subsets = 0
    covering_subsets = 0
    line_failures = 0
    for subset_size in subset_sizes:
        for chosen in combinations(usable, subset_size):
            tested_subsets += 1
            union = 0
            for _, mask, _ in chosen:
                union |= mask
            if union != full_mask:
                continue
            covering_subsets += 1
            selected_points = basis + tuple(normal for normal, _, _ in chosen)
            if not contains_projective_line(selected_points):
                line_failures += 1

    if line_failures:
        raise AssertionError(
            f"dimension {dimension} has a cover without a projective line"
        )

    return {
        "dimension": dimension,
        "projective_points": len(projective_points(dimension)),
        "torus_points": len(torus),
        "candidate_normals": len(candidates),
        "maximum_mask_size": maximum_mask_size,
        "enumerated_normals": len(usable),
        "tested_subsets": tested_subsets,
        "covering_subsets": covering_subsets,
        "line_failures": line_failures,
    }


def verify_certificate() -> Dict[str, object]:
    dimensions = tuple(enumerate_dimension(dimension) for dimension in (2, 3, 4))

    expected = {
        2: (6, 4, 4, 1, 4, 16, 1),
        3: (31, 16, 28, 4, 28, 122438, 87),
        4: (156, 64, 152, 16, 24, 10626, 6),
    }
    for record in dimensions:
        dimension = record["dimension"]
        actual = (
            record["projective_points"],
            record["torus_points"],
            record["candidate_normals"],
            record["maximum_mask_size"],
            record["enumerated_normals"],
            record["tested_subsets"],
            record["covering_subsets"],
        )
        if actual != expected[dimension]:
            raise AssertionError(
                f"dimension {dimension} census changed: {actual}"
            )

    analytic_dimensions = []
    for dimension in range(5, 9):
        torus_size = 4 ** (dimension - 1)
        maximum_covered = (8 - dimension) * 4 ** (dimension - 2)
        if maximum_covered >= torus_size:
            raise AssertionError("the high-dimensional incidence bound failed")
        analytic_dimensions.append(
            {
                "dimension": dimension,
                "torus_points": torus_size,
                "maximum_union_bound": maximum_covered,
            }
        )

    return {
        "status": "[COMPUTED] every normalized F5 cover of size at most 8 contains a 6-point projective line",
        "prime": PRIME,
        "exhaustive_dimensions": list(dimensions),
        "analytic_dimensions": analytic_dimensions,
        "dimension_one": "impossible: the only hyperplane is zero",
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
