#!/usr/bin/env python3
"""Independent F_3 linear-algebra verifier for the 28-point W(7,3) file."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List

P = 3


def rank_mod_p(matrix: List[List[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv * x) % p for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                f = a[r][col]
                a[r] = [(a[r][c] - f * a[rank][c]) % p for c in range(cols)]
        rank += 1
    return rank


def normalize(v: List[int]) -> tuple[int, ...]:
    first = next((x % P for x in v if x % P), None)
    if first is None:
        raise AssertionError("zero vector")
    inv = pow(first, -1, P)
    return tuple((inv * x) % P for x in v)


def pair(v: List[int], w: List[int], form: List[List[int]]) -> int:
    n = len(v)
    return sum(v[i] * form[i][j] * w[j] for i in range(n) for j in range(n)) % P


def verify(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["schema"] == "erdos117.w73_q3_twisted_tensor_28.v1"
    assert data["field"]["q"] == 3
    n = data["ambient"]["dimension_over_F3"]
    assert n == 8
    form = [[x % P for x in row] for row in data["ambient"]["alternating_form_matrix"]]
    assert len(form) == n and all(len(row) == n for row in form)
    for i in range(n):
        assert form[i][i] == 0
        for j in range(n):
            assert (form[i][j] + form[j][i]) % P == 0
    rank = rank_mod_p(form, P)
    assert rank == 8

    vectors = [[x % P for x in row] for row in data["construction"]["vectors_over_F3"]]
    assert len(vectors) == 28 and all(len(v) == n for v in vectors)
    norms = [normalize(v) for v in vectors]
    assert len(set(norms)) == 28

    counts = {1: 0, 2: 0}
    checked = 0
    for i, v in enumerate(vectors):
        assert pair(v, v, form) == 0
        for j in range(i + 1, len(vectors)):
            value = pair(v, vectors[j], form)
            assert value != 0, f"orthogonal pair {i},{j}"
            counts[value] += 1
            checked += 1

    exp = data["expected"]
    assert exp["point_count"] == 28
    assert exp["unordered_pair_count"] == checked == 378
    assert exp["matrix_rank_mod_3"] == rank
    assert {int(k): int(v) for k, v in exp["nonzero_pairing_value_counts"].items()} == counts

    print("PASS: twisted-tensor certificate is internally valid")
    print(f"file={path}")
    print("field=F_3")
    print(f"ambient_dimension={n}")
    print(f"form_rank={rank}")
    print(f"projective_points={len(vectors)}")
    print(f"unordered_pairs_checked={checked}")
    print(f"nonzero_pairing_value_counts={counts}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        default="certificates/W73_Q3_TWISTED_TENSOR_28.json",
    )
    args = parser.parse_args()
    verify(Path(args.certificate))


if __name__ == "__main__":
    main()
