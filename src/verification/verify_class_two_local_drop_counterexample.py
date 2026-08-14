#!/usr/bin/env python3
"""Verify the explicit class-two order-512 local-drop counterexample."""

from __future__ import annotations

import json
from itertools import combinations
from typing import Dict, Sequence, Tuple


Vector = int
Central = int
Element = Tuple[Vector, Central]

V_ORDER = 1 << 5
W_ORDER = 1 << 4
EDGES = ((0, 2), (0, 4), (1, 4), (3, 4))
TARGET_VECTOR = (1 << 0) | (1 << 4)

CLIQUE = (
    1,
    5,
    6,
    16,
    17,
    18,
    19,
    21,
    23,
    24,
    25,
    26,
    27,
    29,
    31,
)

COMMUTING_CLASSES = (
    (0, 17),
    (19,),
    (21,),
    (23,),
    (25,),
    (27,),
    (29,),
    (31,),
    (4, 16, 20),
    (18, 22),
    (24, 28),
    (26, 30),
    (1, 2, 3, 8, 9, 10, 11),
    (5, 7, 13, 15),
    (6, 12, 14),
)


def coordinate(vector: Vector, index: int) -> int:
    return (vector >> index) & 1


def cocycle(left: Vector, right: Vector) -> Central:
    """Return c(left,right), with one output bit for each ordered edge."""

    value = 0
    for output_index, (lower, upper) in enumerate(EDGES):
        value ^= (
            coordinate(left, upper) & coordinate(right, lower)
        ) << output_index
    return value


def beta(left: Vector, right: Vector) -> Central:
    return cocycle(left, right) ^ cocycle(right, left)


def multiply(left: Element, right: Element) -> Element:
    left_vector, left_central = left
    right_vector, right_central = right
    return (
        left_vector ^ right_vector,
        left_central ^ right_central ^ cocycle(left_vector, right_vector),
    )


def inverse(element: Element) -> Element:
    vector, central = element
    return vector, central ^ cocycle(vector, vector)


def commutator(left: Element, right: Element) -> Element:
    """Use the convention [left,right]=left^-1 right^-1 left right."""

    value = multiply(inverse(left), inverse(right))
    value = multiply(value, left)
    return multiply(value, right)


def commute(left: Element, right: Element) -> bool:
    return commutator(left, right) == (0, 0)


def all_elements() -> Tuple[Element, ...]:
    return tuple(
        (vector, central)
        for vector in range(V_ORDER)
        for central in range(W_ORDER)
    )


def verify_cocycle() -> None:
    for left in range(V_ORDER):
        if cocycle(0, left) != 0 or cocycle(left, 0) != 0:
            raise AssertionError("the cocycle is not normalized")
        for right in range(V_ORDER):
            for third in range(V_ORDER):
                lhs = cocycle(left, right) ^ cocycle(left ^ right, third)
                rhs = cocycle(right, third) ^ cocycle(left, right ^ third)
                if lhs != rhs:
                    raise AssertionError("the cocycle identity failed")


def verify_presentation(elements: Sequence[Element]) -> None:
    identity = (0, 0)
    for element in elements:
        if multiply(identity, element) != element:
            raise AssertionError("left identity failed")
        if multiply(element, identity) != element:
            raise AssertionError("right identity failed")
        element_inverse = inverse(element)
        if multiply(element, element_inverse) != identity:
            raise AssertionError("right inverse failed")
        if multiply(element_inverse, element) != identity:
            raise AssertionError("left inverse failed")

    generators = tuple((1 << index, 0) for index in range(5))
    central_generators = tuple((0, 1 << index) for index in range(4))
    for generator in generators + central_generators:
        if multiply(generator, generator) != identity:
            raise AssertionError("a named generator is not an involution")
    for generator in central_generators:
        if any(not commute(generator, element) for element in elements):
            raise AssertionError("a named central generator is not central")

    edge_positions = {edge: index for index, edge in enumerate(EDGES)}
    for lower in range(5):
        for upper in range(lower + 1, 5):
            output_index = edge_positions.get((lower, upper))
            expected = 0 if output_index is None else 1 << output_index
            actual = commutator(generators[lower], generators[upper])
            if actual != (0, expected):
                raise AssertionError("a basic commutator has the wrong value")

    for left in range(V_ORDER):
        for right in range(V_ORDER):
            if commutator((left, 0), (right, 0)) != (0, beta(left, right)):
                raise AssertionError("the tuple and bilinear commutators disagree")


def verify_graph_certificates() -> None:
    if len(CLIQUE) != 15 or len(set(CLIQUE)) != 15:
        raise AssertionError("the clique does not contain 15 distinct vectors")
    if any(beta(left, right) == 0 for left, right in combinations(CLIQUE, 2)):
        raise AssertionError("the displayed clique contains a commuting pair")

    if len(COMMUTING_CLASSES) != 15:
        raise AssertionError("the coloring does not have 15 classes")
    flattened = [vector for color in COMMUTING_CLASSES for vector in color]
    if sorted(flattened) != list(range(V_ORDER)):
        raise AssertionError("the coloring classes do not partition V")
    for color in COMMUTING_CLASSES:
        if any(beta(left, right) != 0 for left, right in combinations(color, 2)):
            raise AssertionError("a coloring class contains a noncommuting pair")
        if len(set(color).intersection(CLIQUE)) != 1:
            raise AssertionError("a coloring class does not meet the clique once")


def verify_certificate() -> Dict[str, object]:
    verify_cocycle()
    elements = all_elements()
    if len(elements) != 512 or len(set(elements)) != 512:
        raise AssertionError("the tuple model does not have order 512")
    verify_presentation(elements)

    radical = tuple(
        vector
        for vector in range(V_ORDER)
        if all(beta(vector, other) == 0 for other in range(V_ORDER))
    )
    if radical != (0,):
        raise AssertionError("the commutator map has a nonzero radical")

    center = tuple(
        element
        for element in elements
        if all(commute(element, other) for other in elements)
    )
    expected_center = tuple((0, central) for central in range(W_ORDER))
    if center != expected_center:
        raise AssertionError("the center is not {0} x W")

    verify_graph_certificates()

    target = (TARGET_VECTOR, 0)
    target_square = multiply(target, target)
    if target_square != (0, 1 << EDGES.index((0, 4))):
        raise AssertionError("the target square is not z_04")
    if multiply(target_square, target_square) != (0, 0):
        raise AssertionError("the target does not have order four")
    centralizer = tuple(element for element in elements if commute(target, element))
    if len(centralizer) != 32:
        raise AssertionError("the target centralizer does not have order 32")
    if {element[0] for element in centralizer} != {0, TARGET_VECTOR}:
        raise AssertionError("the target commutator kernel is wrong")
    if any(
        not commute(left, right)
        for left, right in combinations(centralizer, 2)
    ):
        raise AssertionError("the target centralizer is not abelian")

    nu_group = len(CLIQUE)
    nu_centralizer = 1
    centralizer_index = len(elements) // len(centralizer)
    linear_rhs = nu_group - nu_centralizer
    plus_one_rhs = linear_rhs + 1
    if not centralizer_index > plus_one_rhs > linear_rhs:
        raise AssertionError("the two claimed local inequalities did not fail")

    common_centralizer = tuple(
        element for element in elements if commute(target, element)
    )
    product = {
        multiply(left, right)
        for left in centralizer
        for right in common_centralizer
    }
    if product != set(centralizer) or len(product) >= len(elements):
        raise AssertionError("the false surjectivity witness did not fail")

    return {
        "status": "[DISPROVED] both linear local-drop inequalities",
        "group_order": len(elements),
        "center_order": len(center),
        "target_vector": TARGET_VECTOR,
        "target_order": 4,
        "centralizer_order": len(centralizer),
        "centralizer_index": centralizer_index,
        "nu_group": nu_group,
        "nu_centralizer": nu_centralizer,
        "linear_rhs": linear_rhs,
        "plus_one_rhs": plus_one_rhs,
        "clique": list(CLIQUE),
        "commuting_classes": [list(color) for color in COMMUTING_CLASSES],
        "false_surjectivity_product_order": len(product),
        "quadratic_candidate_status": "[UNVERIFIED]",
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
