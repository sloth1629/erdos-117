"""Regression tests for the spectral local-drop partial theorem."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "verification"))

from verify_class_two_spectral_local_drop import verify_certificate  # noqa: E402


class ClassTwoSpectralLocalDropTests(unittest.TestCase):
    def test_refinement_certificates(self):
        certificate = verify_certificate()
        self.assertEqual("[COMPUTED] spectral local-drop refinement", certificate["status"])
        example = certificate["order_32768_example"]
        self.assertEqual(32768, example["group_order"])
        self.assertEqual(100, example["cocycle_basis_checks"])
        self.assertEqual(32, example["center_order"])
        self.assertEqual(5, example["centralizer_clique_number"])
        self.assertEqual("237/32", example["spectral_weighted_sum"])
        self.assertEqual(5, example["oriented_lower_bound"])
        self.assertEqual(32, example["affine_clique_size"])
        self.assertEqual(12, len(certificate["oriented_threshold_table"]))
        self.assertEqual(41, certificate["q64_capacity"]["minimum_saturated_operators"])


if __name__ == "__main__":
    unittest.main()
