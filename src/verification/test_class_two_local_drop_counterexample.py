"""Regression test for the class-two order-512 local-drop counterexample."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "verification"))

from verify_class_two_local_drop_counterexample import (  # noqa: E402
    CLIQUE,
    COMMUTING_CLASSES,
    verify_certificate,
)


class ClassTwoLocalDropCounterexampleTests(unittest.TestCase):
    def test_explicit_order_512_certificate(self):
        certificate = verify_certificate()
        self.assertEqual(
            "[DISPROVED] both linear local-drop inequalities",
            certificate["status"],
        )
        self.assertEqual(512, certificate["group_order"])
        self.assertEqual(16, certificate["center_order"])
        self.assertEqual(17, certificate["target_vector"])
        self.assertEqual(4, certificate["target_order"])
        self.assertEqual(32, certificate["centralizer_order"])
        self.assertEqual(16, certificate["centralizer_index"])
        self.assertEqual(
            (15, 1),
            (certificate["nu_group"], certificate["nu_centralizer"]),
        )
        self.assertEqual(
            (14, 15),
            (certificate["linear_rhs"], certificate["plus_one_rhs"]),
        )
        self.assertEqual(15, len(CLIQUE))
        self.assertEqual(15, len(COMMUTING_CLASSES))
        self.assertEqual(32, certificate["false_surjectivity_product_order"])
        self.assertEqual("[UNVERIFIED]", certificate["quadratic_candidate_status"])


if __name__ == "__main__":
    unittest.main()
