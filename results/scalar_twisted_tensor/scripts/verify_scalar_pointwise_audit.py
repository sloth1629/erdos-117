#!/usr/bin/env python3
"""Finite arithmetic audit of the pointwise inequalities used in Theorem 4.13.

This is not a proof of the infinite theorem. It checks exact squared integer
inequalities over broad boundary ranges, including the unique exception and
equality case, using only the proved lower bounds for pi(q,m).
"""
from __future__ import annotations


def assert_bound(q: int, m: int, pi_lower: int) -> None:
    left = (q**m + 1) ** 2
    right = 2**pi_lower
    assert left <= right, (q, m, pi_lower, left, right)


def main() -> None:
    # q=2: exact pi=2m+1. The m=1 case is the unique exception.
    assert (2**1 + 1) ** 2 > 2 ** (2 * 1 + 1)
    for m in range(2, 501):
        assert_bound(2, m, 2 * m + 1)

    # q=3: block lower bound pi >= 27k+3r+1 for m=4k+r.
    equality_cases = []
    for m in range(1, 501):
        k, r = divmod(m, 4)
        pi_lower = 27 * k + 3 * r + 1
        assert_bound(3, m, pi_lower)
        if (3**m + 1) ** 2 == 2**pi_lower:
            equality_cases.append((3, m))
    assert equality_cases == [(3, 1)]

    # q>=4: generic pi >= mq+1. Checking all integers is stronger than
    # checking prime powers only.
    checked = 0
    for q in range(4, 257):
        assert q * q <= 2**q  # q <= 2^(q/2), squared.
        for m in range(1, 101):
            assert_bound(q, m, m * q + 1)
            checked += 1

    assert 25 < 32  # (5/4)^2 < 2.
    print("PASS: scalar pointwise boundary audit")
    print("q=2 cases checked: m=1..500 (m=1 confirmed exceptional)")
    print("q=3 cases checked: m=1..500 (unique equality at m=1)")
    print(f"q>=4 integer cases checked: {checked}")
    print("all arithmetic used exact integers")


if __name__ == "__main__":
    main()
