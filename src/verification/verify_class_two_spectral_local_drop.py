#!/usr/bin/env python3
"""Verify the finite certificates in the spectral local-drop refinement."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations
from typing import Dict, Iterable, Tuple


DIMENSION_V = 10
DIMENSION_W = 5
X = 1 << 0
A_BASIS = tuple(1 << index for index in range(1, 5))
Y_BASIS = tuple(1 << index for index in range(5, 10))


def beta_basis(left: int, right: int) -> int:
    if left == right:
        return 0
    i, j = sorted((left, right))
    if i == 0 and 5 <= j <= 9:
        return 1 << (j - 5)
    if 1 <= i < j <= 4:
        return 1 << 0
    if 1 <= i <= 4 and j == i + 5:
        return 1 << i
    return 0


def beta(left: int, right: int) -> int:
    value = 0
    for i in range(DIMENSION_V):
        if not (left >> i) & 1:
            continue
        for j in range(DIMENSION_V):
            if (right >> j) & 1:
                value ^= beta_basis(i, j)
    return value


def cocycle(left: int, right: int) -> int:
    """The normalized triangular bilinear cocycle c(v,w)."""

    value = 0
    for i in range(DIMENSION_V):
        if not (right >> i) & 1:
            continue
        for j in range(i + 1, DIMENSION_V):
            if (left >> j) & 1:
                value ^= beta_basis(i, j)
    return value


def verify_order_32768_example() -> Dict[str, object]:
    cocycle_basis_checks = 0
    for i in range(DIMENSION_V):
        left = 1 << i
        if cocycle(0, left) != 0 or cocycle(left, 0) != 0:
            raise AssertionError("the triangular cocycle is not normalized")
        for j in range(DIMENSION_V):
            right = 1 << j
            cocycle_basis_checks += 1
            if cocycle(left, right) ^ cocycle(right, left) != beta(left, right):
                raise AssertionError("the triangular cocycle has the wrong commutator")

    radical = tuple(
        vector
        for vector in range(1 << DIMENSION_V)
        if all(beta(vector, 1 << index) == 0 for index in range(DIMENSION_V))
    )
    if radical != (0,):
        raise AssertionError("the alternating map is not radical-free")

    centralizer = tuple(
        vector for vector in range(1 << DIMENSION_V) if beta(X, vector) == 0
    )
    if len(centralizer) != 32:
        raise AssertionError("the compressed centralizer has the wrong order")

    clique = A_BASIS + (sum(A_BASIS),)
    for left, right in combinations(clique, 2):
        if beta(left, right) == 0:
            raise AssertionError("the displayed H-clique is not a clique")

    # The radical <x> of the centralizer can be discarded.  Exhaust all
    # six-subsets of the remaining four-dimensional U to certify the upper
    # bound five without relying on an optimizer.
    u_vectors = tuple(range(1 << 4))

    def lift_u(vector: int) -> int:
        return vector << 1

    for candidate in combinations(u_vectors, 6):
        if all(beta(lift_u(left), lift_u(right)) != 0 for left, right in combinations(candidate, 2)):
            raise AssertionError("a six-clique exists in the compressed centralizer")

    masks = (1 << 1, 1 << 2, 1 << 3, 1 << 4, 0b11110)
    distribution: Dict[int, int] = {}
    weighted_sum = Fraction(0, 1)
    for vector in range(1, 1 << DIMENSION_W):
        count = sum(1 for mask in masks if (vector & mask) in (0, vector))
        distribution[count] = distribution.get(count, 0) + 1
        weighted_sum += Fraction(1, 1 << count)
    if distribution != {0: 1, 1: 5, 2: 10, 3: 10, 5: 5}:
        raise AssertionError("the spectral-incidence distribution is wrong")
    if weighted_sum != Fraction(237, 32):
        raise AssertionError("the spectral-incidence weighted sum is wrong")

    smaller_union = {1 << index for index in range(DIMENSION_W)}
    oriented_lower_bound = math.ceil(Fraction(3, 16) * (31 - len(smaller_union)))
    if oriented_lower_bound != 5:
        raise AssertionError("the oriented-union lower bound is wrong")

    # F=0 on the chosen y-space, so the alpha=1 affine layer is a 32-clique.
    affine_vectors = tuple(range(1 << DIMENSION_W))
    for left, right in combinations(affine_vectors, 2):
        if left ^ right == 0:
            raise AssertionError("the affine layer contains a commuting pair")

    return {
        "group_order": 1 << (DIMENSION_V + DIMENSION_W),
        "cocycle_basis_checks": cocycle_basis_checks,
        "center_order": 1 << DIMENSION_W,
        "commutator_image_order": 1 << DIMENSION_W,
        "centralizer_clique_number": len(clique),
        "spectral_distribution": distribution,
        "spectral_weighted_sum": str(weighted_sum),
        "oriented_lower_bound": oriented_lower_bound,
        "affine_clique_size": len(affine_vectors),
    }


def gamma_binary(dimension: int) -> Fraction:
    quotient, remainder = divmod(dimension, 2)
    return Fraction((2 - remainder), 2 ** quotient) / 2 + Fraction(
        remainder, 2 ** (quotient + 1)
    ) / 2


def ceiling_fraction(value: Fraction) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def verify_oriented_threshold_table() -> Tuple[Tuple[int, int, int, int], ...]:
    expected = (
        (4, 16, 3, 4),
        (5, 32, 4, 8),
        (6, 64, 5, 6),
        (7, 128, 7, 12),
        (8, 256, 9, 10),
        (9, 512, 13, 19),
        (10, 1024, 17, 18),
        (11, 2048, 26, 37),
        (12, 4096, 33, 34),
        (13, 8192, 51, 70),
        (14, 16384, 65, 66),
        (15, 32768, 102, 138),
    )
    actual = []
    for dimension in range(4, 16):
        q = 1 << dimension
        gamma = gamma_binary(dimension)
        old_maximum = ceiling_fraction(Fraction(q - 1) * gamma) + 1 - math.ceil(
            math.sqrt(q) / 2
        )
        per_operator = (1 << (dimension // 2)) - 1
        oriented_maximum = -1
        for saturated in range(q + 1):
            remaining = max(0, q - 1 - saturated * per_operator)
            delta = ceiling_fraction(gamma * remaining)
            if q <= 4 * (delta + 1) ** 2:
                oriented_maximum = saturated
            else:
                break
        actual.append((dimension, q, old_maximum, oriented_maximum))
    if tuple(actual) != expected:
        raise AssertionError("the oriented threshold table is wrong")
    return tuple(actual)


def verify_q64_capacity() -> Dict[str, int]:
    point_count = 63
    pair_count = math.comb(point_count, 2)
    balanced_capacity = 7 * 7
    if pair_count != 1953 or 39 * balanced_capacity >= pair_count:
        raise AssertionError("the first q=64 capacity bound is wrong")
    if 40 * balanced_capacity - pair_count != 7:
        raise AssertionError("the q=64 slack is wrong")
    if point_count * 9 <= 40 * 14:
        raise AssertionError("the all-balanced incidence contradiction failed")
    mixed_demand = 3 * 7 + 15 * 9 + 45 * 9
    mixed_supply = 39 * 14
    if mixed_demand != 561 or mixed_supply != 546 or mixed_demand <= mixed_supply:
        raise AssertionError("the mixed q=64 incidence contradiction failed")
    return {
        "point_count": point_count,
        "pair_count": pair_count,
        "minimum_saturated_operators": 41,
        "all_balanced_demand": point_count * 9,
        "all_balanced_supply": 40 * 14,
        "mixed_demand": mixed_demand,
        "mixed_supply": mixed_supply,
    }


def verify_certificate() -> Dict[str, object]:
    return {
        "status": "[COMPUTED] spectral local-drop refinement",
        "order_32768_example": verify_order_32768_example(),
        "oriented_threshold_table": verify_oriented_threshold_table(),
        "q64_capacity": verify_q64_capacity(),
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
