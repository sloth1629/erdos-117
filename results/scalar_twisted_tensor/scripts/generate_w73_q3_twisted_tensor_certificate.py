#!/usr/bin/env python3
"""Generate the q=3,t=3 twisted-tensor partial ovoid in W(7,3).

The generator uses E=F_27=F_3[a]/(a^3-a-1), constructs the 8-dimensional
F_3 fixed space inside (E^2)^{tensor 3}, changes to an explicit fixed basis,
and exports the 28 PG(1,27) image points and their symplectic form over F_3.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Sequence, Tuple

P = 3
Elt = Tuple[int, int, int]
ZERO: Elt = (0, 0, 0)
ONE: Elt = (1, 0, 0)
A: Elt = (0, 1, 0)
A2: Elt = (0, 0, 1)


def add(x: Elt, y: Elt) -> Elt:
    return tuple((a + b) % P for a, b in zip(x, y))  # type: ignore[return-value]


def neg(x: Elt) -> Elt:
    return tuple((-a) % P for a in x)  # type: ignore[return-value]


def sub(x: Elt, y: Elt) -> Elt:
    return add(x, neg(y))


def mul(x: Elt, y: Elt) -> Elt:
    raw = [0] * 5
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            raw[i + j] = (raw[i + j] + xi * yj) % P
    # a^3=a+1 and a^4=a^2+a
    return (
        (raw[0] + raw[3]) % P,
        (raw[1] + raw[3] + raw[4]) % P,
        (raw[2] + raw[4]) % P,
    )


def pow_elt(x: Elt, n: int) -> Elt:
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
        raise ZeroDivisionError
    return pow_elt(x, 25)


def div(x: Elt, y: Elt) -> Elt:
    return mul(x, inv(y))


def all_elts() -> Iterable[Elt]:
    for a0 in range(P):
        for a1 in range(P):
            for a2 in range(P):
                yield (a0, a1, a2)


def scalar(n: int) -> Elt:
    return (n % P, 0, 0)


def bits(i: int) -> tuple[int, int, int]:
    return ((i >> 2) & 1, (i >> 1) & 1, i & 1)


def index(b: Sequence[int]) -> int:
    return (b[0] << 2) | (b[1] << 1) | b[2]


def shift(b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (b[2], b[0], b[1])


def fixed_orbit_vector(rep: tuple[int, int, int], c: Elt) -> list[Elt]:
    out = [ZERO] * 8
    b = rep
    coeff = c
    while True:
        out[index(b)] = coeff
        b = shift(b)
        coeff = pow_elt(coeff, P)
        if b == rep:
            break
    return out


def mat_solve(columns: list[list[Elt]], rhs: list[Elt]) -> list[Elt]:
    """Solve A x=rhs over F_27; A is supplied as columns."""
    n = len(columns)
    aug = [[columns[c][r] for c in range(n)] + [rhs[r]] for r in range(n)]
    row = 0
    for col in range(n):
        pivot = next((r for r in range(row, n) if aug[r][col] != ZERO), None)
        if pivot is None:
            raise AssertionError("singular fixed basis")
        aug[row], aug[pivot] = aug[pivot], aug[row]
        pivot_inv = inv(aug[row][col])
        aug[row] = [mul(pivot_inv, x) for x in aug[row]]
        for r in range(n):
            if r == row or aug[r][col] == ZERO:
                continue
            f = aug[r][col]
            aug[r] = [sub(aug[r][j], mul(f, aug[row][j])) for j in range(n + 1)]
        row += 1
    return [aug[i][n] for i in range(n)]


def standard_tensor_form() -> list[list[int]]:
    j = [[0, 1], [2, 0]]
    form = [[0] * 8 for _ in range(8)]
    for r in range(8):
        br = bits(r)
        for c in range(8):
            bc = bits(c)
            value = 1
            for i in range(3):
                value = (value * j[br[i]][bc[i]]) % P
            form[r][c] = value
    return form


def pair_e(x: list[Elt], y: list[Elt], form: list[list[int]]) -> Elt:
    out = ZERO
    for i in range(8):
        for j in range(8):
            if form[i][j]:
                out = add(out, mul(mul(x[i], scalar(form[i][j])), y[j]))
    return out


def affine_tensor(z: Elt) -> list[Elt]:
    zq = pow_elt(z, 3)
    zq2 = pow_elt(z, 9)
    factors = [(ONE, z), (ONE, zq), (ONE, zq2)]
    out: list[Elt] = []
    for b in (bits(i) for i in range(8)):
        value = ONE
        for i in range(3):
            value = mul(value, factors[i][b[i]])
        out.append(value)
    return out


def infinity_tensor() -> list[Elt]:
    out = [ZERO] * 8
    out[index((1, 1, 1))] = ONE
    return out


def generate() -> dict:
    # Explicit fixed-space basis: singleton bit orbits and two 3-cycles.
    fixed_basis = [
        fixed_orbit_vector((0, 0, 0), ONE),
        fixed_orbit_vector((1, 1, 1), ONE),
    ]
    for rep in ((0, 0, 1), (0, 1, 1)):
        for c in (ONE, A, A2):
            fixed_basis.append(fixed_orbit_vector(rep, c))
    assert len(fixed_basis) == 8

    std_form = standard_tensor_form()
    fixed_form: list[list[int]] = []
    for x in fixed_basis:
        row: list[int] = []
        for y in fixed_basis:
            value = pair_e(x, y, std_form)
            if value[1:] != (0, 0):
                raise AssertionError(f"fixed pairing not in F_3: {value}")
            row.append(value[0])
        fixed_form.append(row)

    labels: list[str] = []
    std_vectors: list[list[Elt]] = []
    for z in all_elts():
        labels.append(f"[1:{z[0]}+{z[1]}a+{z[2]}a^2]")
        std_vectors.append(affine_tensor(z))
    labels.append("[0:1]")
    std_vectors.append(infinity_tensor())

    vectors: list[list[int]] = []
    for w in std_vectors:
        coeffs = mat_solve(fixed_basis, w)
        if any(c[1:] != (0, 0) for c in coeffs):
            raise AssertionError(f"fixed tensor has non-base-field coordinates: {coeffs}")
        vectors.append([c[0] for c in coeffs])

    counts = {1: 0, 2: 0}
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            val = sum(
                vectors[i][r] * fixed_form[r][c] * vectors[j][c]
                for r in range(8)
                for c in range(8)
            ) % P
            if val == 0:
                raise AssertionError(f"orthogonal pair {i},{j}")
            counts[val] += 1

    return {
        "schema": "erdos117.w73_q3_twisted_tensor_28.v1",
        "field": {
            "q": 3,
            "extension_degree": 3,
            "basis": ["1", "a", "a^2"],
            "defining_relation": "a^3=a+1",
        },
        "construction": {
            "tensor_length": 3,
            "source": "PG(1,27)",
            "description": "[a:b] -> tensor_i (a^(3^i),b^(3^i))",
            "point_labels": labels,
            "fixed_basis_order": [
                "orbit 000, coefficient 1",
                "orbit 111, coefficient 1",
                "orbit 001, coefficient 1",
                "orbit 001, coefficient a",
                "orbit 001, coefficient a^2",
                "orbit 011, coefficient 1",
                "orbit 011, coefficient a",
                "orbit 011, coefficient a^2",
            ],
            "vectors_over_F3": vectors,
        },
        "ambient": {
            "dimension_over_F3": 8,
            "alternating_form_matrix": fixed_form,
        },
        "expected": {
            "point_count": 28,
            "unordered_pair_count": 378,
            "matrix_rank_mod_3": 8,
            "nonzero_pairing_value_counts": {str(k): v for k, v in counts.items()},
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output",
        nargs="?",
        default="certificates/W73_Q3_TWISTED_TENSOR_28.json",
    )
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    data = generate()
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    print(f"points={data['expected']['point_count']}")
    print(f"pairings={data['expected']['unordered_pair_count']}")
    print(f"value_counts={data['expected']['nonzero_pairing_value_counts']}")


if __name__ == "__main__":
    main()
