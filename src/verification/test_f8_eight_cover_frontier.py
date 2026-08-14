"""Regression tests for the explicit order-144 irredundant eight-cover."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "verification"))

from verify_f8_order144_witness import verify_certificate  # noqa: E402


class F8EightCoverFrontierTests(unittest.TestCase):
    def test_order_144_witness(self):
        certificate = verify_certificate()
        self.assertEqual("[COMPUTED] order-144 eight-cover witness", certificate["status"])
        self.assertEqual(144, certificate["group_order"])
        self.assertEqual(144**3, certificate["associativity_triples_checked"])
        self.assertEqual((72, 72, 72, 72, 48, 48, 48, 48), certificate["subgroup_orders"])
        self.assertEqual((2, 2, 2, 2, 3, 3, 3, 3), certificate["subgroup_indices"])
        self.assertEqual(144, certificate["union_order"])
        self.assertEqual(1, certificate["intersection_order"])
        self.assertEqual((2,) * 8, certificate["private_set_sizes"])
        self.assertEqual(10, certificate["audit_clique_number"])


if __name__ == "__main__":
    unittest.main()
