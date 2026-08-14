#!/usr/bin/env python3
"""Independent verifier for W53_Q3_NORM_ONE_13.json.

This verifier trusts no F_27 arithmetic. It checks the exported object solely
as exact linear algebra over F_3: an alternating nonsingular 6x6 form and 13
distinct projective points with all 78 mutual pairings nonzero.
"""
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
        pivot = next((r for r in range(rank, rows) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv * x) % p for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col] % p:
                factor = a[r][col] % p
                a[r] = [(a[r][c] - factor * a[rank][c]) % p for c in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def pairing(v: List[int], w: List[int], form: List[List[int]], p: int) -> int:
    n = len(v)
    return sum(v[i] * form[i][j] * w[j] for i in range(n) for j in range(n)) % p


def normalize_projective(v: List[int], p: int) -> tuple[int, ...]:
    first = next((x % p for x in v if x % p), None)
    if first is None:
        raise AssertionError("zero vector")
    inv = pow(first, -1, p)
    return tuple((inv * x) % p for x in v)


def verify(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["schema"] == "erdos117.w53_q3_pairwise_nonorthogonal.v1"
    assert data["field"]["q"] == P
    n = data["ambient"]["dimension_over_F3"]
    assert n == 6
    form = data["ambient"]["alternating_form_matrix"]
    assert len(form) == n and all(len(row) == n for row in form)
    form = [[x % P for x in row] for row in form]

    for i in range(n):
        assert form[i][i] == 0, f"nonzero diagonal entry at {i}"
        for j in range(n):
            assert (form[i][j] + form[j][i]) % P == 0, f"not alternating at {i},{j}"
    rank = rank_mod_p(form, P)
    assert rank == 6, f"form rank {rank}, expected 6"

    vectors = data["construction"]["vectors"]
    assert len(vectors) == 13
    assert all(len(v) == n for v in vectors)
    vectors = [[x % P for x in v] for v in vectors]
    normalized = [normalize_projective(v, P) for v in vectors]
    assert len(set(normalized)) == len(normalized), "duplicate projective points"

    counts = {1: 0, 2: 0}
    checked = 0
    for i in range(len(vectors)):
        assert pairing(vectors[i], vectors[i], form, P) == 0
        for j in range(i + 1, len(vectors)):
            value = pairing(vectors[i], vectors[j], form, P)
            assert value != 0, f"orthogonal pair {i},{j}"
            counts[value] += 1
            checked += 1

    expected = data["expected"]
    assert expected["point_count"] == len(vectors)
    assert expected["unordered_pair_count"] == checked == 78
    assert expected["matrix_rank_mod_3"] == rank
    expected_counts = {int(k): int(v) for k, v in expected["nonzero_pairing_value_counts"].items()}
    assert expected_counts == counts

    print("PASS: certificate is internally valid")
    print(f"file={path}")
    print(f"field=F_{P}")
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
        default="certificates/W53_Q3_NORM_ONE_13.json",
    )
    args = parser.parse_args()
    verify(Path(args.certificate))


if __name__ == "__main__":
    main()
