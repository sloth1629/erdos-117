#!/usr/bin/env python3
"""Verify the explicit order-144 maximal irredundant eight-cover."""

from __future__ import annotations

import json
from itertools import product
from typing import Dict, Iterable, Tuple


Element = Tuple[int, int, int, int, int, int]


def elements() -> Tuple[Element, ...]:
    return tuple(
        (a0, a1, a2, x, y, epsilon)
        for a0, a1, a2 in product(range(2), repeat=3)
        for x, y in product(range(3), repeat=2)
        for epsilon in range(2)
    )


ELEMENTS = elements()
IDENTITY: Element = (0, 0, 0, 0, 0, 0)


def multiply(left: Element, right: Element) -> Element:
    a0, a1, a2, x, y, epsilon = left
    b0, b1, b2, u, v, eta = right
    sign = 1 if epsilon == 0 else -1
    return (
        a0 ^ b0,
        a1 ^ b1,
        a2 ^ b2,
        (x + sign * u) % 3,
        (y + sign * v) % 3,
        epsilon ^ eta,
    )


def inverse(element: Element) -> Element:
    a0, a1, a2, x, y, epsilon = element
    sign = -1 if epsilon == 0 else 1
    return a0, a1, a2, (sign * x) % 3, (sign * y) % 3, epsilon


def commute(left: Element, right: Element) -> bool:
    return multiply(left, right) == multiply(right, left)


def memberships(element: Element) -> Tuple[bool, ...]:
    a0, a1, a2, x, y, epsilon = element
    return (
        a2 == 0,
        a1 == 0,
        a0 == 0,
        (a0 + a1 + a2 + epsilon) % 2 == 0,
        x == 0,
        (x + y) % 3 == 0,
        (x + 2 * y) % 3 == 0,
        y == epsilon,
    )


SUBGROUPS = tuple(
    frozenset(element for element in ELEMENTS if memberships(element)[index])
    for index in range(8)
)

PRIVATE_POINTS: Tuple[Element, ...] = (
    (1, 1, 0, 1, 0, 1),
    (1, 0, 1, 1, 0, 1),
    (0, 1, 1, 1, 0, 1),
    (1, 1, 1, 1, 0, 1),
    (1, 1, 1, 0, 1, 0),
    (1, 1, 1, 1, 2, 0),
    (1, 1, 1, 1, 1, 0),
    (1, 1, 1, 1, 0, 0),
)


def verify_group() -> int:
    if len(ELEMENTS) != 144 or len(set(ELEMENTS)) != 144:
        raise AssertionError("the tuple model does not have order 144")
    for element in ELEMENTS:
        if multiply(IDENTITY, element) != element:
            raise AssertionError("left identity failed")
        if multiply(element, IDENTITY) != element:
            raise AssertionError("right identity failed")
        element_inverse = inverse(element)
        if multiply(element, element_inverse) != IDENTITY:
            raise AssertionError("right inverse failed")
        if multiply(element_inverse, element) != IDENTITY:
            raise AssertionError("left inverse failed")

    associativity_checks = 0
    for left in ELEMENTS:
        for middle in ELEMENTS:
            left_middle = multiply(left, middle)
            for right in ELEMENTS:
                associativity_checks += 1
                if multiply(left_middle, right) != multiply(
                    left, multiply(middle, right)
                ):
                    raise AssertionError("associativity failed")
    return associativity_checks


def verify_subgroup(subgroup: Iterable[Element]) -> None:
    members = frozenset(subgroup)
    if IDENTITY not in members:
        raise AssertionError("a proposed subgroup omits the identity")
    for left in members:
        if inverse(left) not in members:
            raise AssertionError("a proposed subgroup is not inverse-closed")
        for right in members:
            if multiply(left, right) not in members:
                raise AssertionError("a proposed subgroup is not product-closed")


def verify_cover() -> Tuple[int, ...]:
    expected_sizes = (72, 72, 72, 72, 48, 48, 48, 48)
    actual_sizes = tuple(len(subgroup) for subgroup in SUBGROUPS)
    if actual_sizes != expected_sizes:
        raise AssertionError("the subgroup sizes are wrong")
    for subgroup in SUBGROUPS:
        verify_subgroup(subgroup)

    union = frozenset().union(*SUBGROUPS)
    if union != frozenset(ELEMENTS):
        raise AssertionError("the eight subgroups do not cover the group")
    intersection = frozenset.intersection(*SUBGROUPS)
    if intersection != frozenset((IDENTITY,)):
        raise AssertionError("the intersection is not trivial")

    private_sizes = []
    for index, subgroup in enumerate(SUBGROUPS):
        others = frozenset().union(
            *(SUBGROUPS[other] for other in range(8) if other != index)
        )
        private = subgroup.difference(others)
        private_sizes.append(len(private))
        if PRIVATE_POINTS[index] not in private:
            raise AssertionError("a displayed private point is not private")
    if tuple(private_sizes) != (2,) * 8:
        raise AssertionError("the exact private-set sizes are wrong")
    return tuple(private_sizes)


def verify_ten_clique_audit() -> Tuple[Element, ...]:
    """Check the audit observation that this witness has clique number ten."""

    reflections = tuple((0, 0, 0, x, y, 1) for x, y in product(range(3), repeat=2))
    translation = (0, 0, 0, 1, 0, 0)
    clique = reflections + (translation,)
    for index, left in enumerate(clique):
        for right in clique[index + 1 :]:
            if commute(left, right):
                raise AssertionError("the displayed ten-set contains a commuting pair")

    # The central C_2^3 factor is irrelevant.  In the generalized-dihedral
    # factor all translations commute, and there are exactly nine reflections.
    # Hence no clique can contain more than one translation and nine reflections.
    return clique


def verify_certificate() -> Dict[str, object]:
    associativity_checks = verify_group()
    private_sizes = verify_cover()
    ten_clique = verify_ten_clique_audit()
    return {
        "status": "[COMPUTED] order-144 eight-cover witness",
        "group_order": len(ELEMENTS),
        "associativity_triples_checked": associativity_checks,
        "subgroup_orders": tuple(len(subgroup) for subgroup in SUBGROUPS),
        "subgroup_indices": tuple(len(ELEMENTS) // len(subgroup) for subgroup in SUBGROUPS),
        "union_order": len(frozenset().union(*SUBGROUPS)),
        "intersection_order": len(frozenset.intersection(*SUBGROUPS)),
        "private_set_sizes": private_sizes,
        "audit_clique_number": len(ten_clique),
    }


def main() -> None:
    certificate = verify_certificate()
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
