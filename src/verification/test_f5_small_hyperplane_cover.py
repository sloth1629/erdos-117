"""Regression test for the small F_5 hyperplane-cover certificate."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "verification"))

from verify_f5_small_hyperplane_cover import verify_certificate  # noqa: E402


class F5SmallHyperplaneCoverTests(unittest.TestCase):
    def test_every_small_cover_contains_a_pencil(self):
        certificate = verify_certificate()
        self.assertEqual(5, certificate["prime"])
        self.assertEqual(
            "[COMPUTED] every normalized F5 cover of size at most 8 contains a 6-point projective line",
            certificate["status"],
        )
        records = {
            record["dimension"]: record
            for record in certificate["exhaustive_dimensions"]
        }
        self.assertEqual((1, 87, 6), tuple(records[d]["covering_subsets"] for d in (2, 3, 4)))
        self.assertEqual((0, 0, 0), tuple(records[d]["line_failures"] for d in (2, 3, 4)))
        self.assertEqual((4, 28, 152), tuple(records[d]["candidate_normals"] for d in (2, 3, 4)))
        self.assertEqual(
            (5, 6, 7, 8),
            tuple(record["dimension"] for record in certificate["analytic_dimensions"]),
        )


if __name__ == "__main__":
    unittest.main()
