#!/usr/bin/env python3
"""Generate a 13-point pairwise-nonorthogonal certificate in W(5,3).

Field model: F_27 = F_3[a]/(a^3-a-1), with a^3=a+1.
The point set is {(x,x^{-1}) : N_{F_27/F_3}(x)=1}.
The verifier deliberately does not implement F_27; it checks only the
exported 6-dimensional matrix and vectors over F_3.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Tuple

P = 3
Elt = Tuple[int, int, int]
ZERO: Elt = (0, 0, 0)
ONE: Elt = (1, 0, 0)


def add(x: Elt, y: Elt) -> Elt:
    return tuple((a + b) % P for a, b in zip(x, y))  # type: ignore[return-value]


def neg(x: Elt) -> Elt:
    return tuple((-a) % P for a in x)  # type: ignore[return-value]


def sub(x: Elt, y: Elt) -> Elt:
    return add(x, neg(y))


def mul(x: Elt, y: Elt) -> Elt:
    # Raw polynomial product, then reduce a^3=a+1 and a^4=a^2+a.
    raw = [0] * 5
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            raw[i + j] = (raw[i + j] + xi * yj) % P
    return (
        (raw[0] + raw[3]) % P,
        (raw[1] + raw[3] + raw[4]) % P,
        (raw[2] + raw[4]) % P,
    )


def pow_elt(x: Elt, n: int) -> Elt:
    if n < 0:
        raise ValueError("negative exponent")
    out = ONE
    base = x
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def inv(x: Elt) -> Elt:
    if x == ZERO:
        raise ZeroDivisionError("zero has no inverse")
    return pow_elt(x, 25)  # x^(27-2)


def trace(x: Elt) -> int:
    # Tr_{27/3}(x)=x+x^3+x^9, which lands in F_3.
    t = add(add(x, pow_elt(x, 3)), pow_elt(x, 9))
    if t[1:] != (0, 0):
        raise AssertionError(f"trace did not land in F_3: {x} -> {t}")
    return t[0]


def norm(x: Elt) -> int:
    # N_{27/3}(x)=x^13, which lands in F_3.
    n = pow_elt(x, 13)
    if n[1:] != (0, 0):
        raise AssertionError(f"norm did not land in F_3: {x} -> {n}")
    return n[0]


def all_elts() -> Iterable[Elt]:
    for a0 in range(P):
        for a1 in range(P):
            for a2 in range(P):
                yield (a0, a1, a2)


def mat_vec_pair(v: list[int], w: list[int], matrix: list[list[int]]) -> int:
    return sum(v[i] * matrix[i][j] * w[j] for i in range(6) for j in range(6)) % P


def generate() -> dict:
    # Irreducibility audit for X^3-X-1: a cubic is irreducible iff root-free.
    roots = [r for r in range(P) if (r**3 - r - 1) % P == 0]
    if roots:
        raise AssertionError(f"defining polynomial has roots: {roots}")

    basis: list[Elt] = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    trace_matrix = [[trace(mul(x, y)) for y in basis] for x in basis]
    zero3 = [[0] * 3 for _ in range(3)]
    matrix = [row0 + row1 for row0, row1 in zip(zero3, trace_matrix)]
    matrix += [
        [(-trace_matrix[i][j]) % P for j in range(3)] + [0] * 3
        for i in range(3)
    ]

    kernel = sorted(x for x in all_elts() if x != ZERO and norm(x) == 1)
    if len(kernel) != 13:
        raise AssertionError(f"expected 13 norm-one elements, found {len(kernel)}")

    vectors = [list(x + inv(x)) for x in kernel]
    values = {1: 0, 2: 0}
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            value = mat_vec_pair(vectors[i], vectors[j], matrix)
            if value == 0:
                raise AssertionError(f"orthogonal pair {i}, {j}")
            values[value] += 1

    return {
        "schema": "erdos117.w53_q3_pairwise_nonorthogonal.v1",
        "field": {
            "q": 3,
            "extension_degree": 3,
            "basis": ["1", "a", "a^2"],
            "defining_relation": "a^3=a+1",
            "defining_polynomial": "X^3-X-1",
        },
        "ambient": {
            "dimension_over_F3": 6,
            "trace_pairing_matrix": trace_matrix,
            "alternating_form_matrix": matrix,
        },
        "construction": {
            "description": "v_x=(x,x^{-1}) for N_{F27/F3}(x)=1",
            "norm_one_elements_coefficients": [list(x) for x in kernel],
            "vectors": vectors,
        },
        "expected": {
            "point_count": 13,
            "unordered_pair_count": 78,
            "nonzero_pairing_value_counts": {str(k): v for k, v in values.items()},
            "matrix_rank_mod_3": 6,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output",
        nargs="?",
        default="certificates/W53_Q3_NORM_ONE_13.json",
        help="output JSON path",
    )
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = generate()
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    print(f"points={payload['expected']['point_count']}")
    print(f"pairings={payload['expected']['unordered_pair_count']}")
    print(f"value_counts={payload['expected']['nonzero_pairing_value_counts']}")


if __name__ == "__main__":
    main()
