"""Regression test for the local SG261 target-ten restriction census."""

from __future__ import annotations

import unittest

from src.verification.verify_h9_sg261_target10_restrictions import (
    verify_saved_certificate,
)


class H9SG261TargetTenRestrictionTests(unittest.TestCase):
    def test_saved_certificate(self):
        certificate = verify_saved_certificate()
        self.assertEqual("[COMPUTED]", certificate["status"])
        self.assertEqual(26387, certificate["odd_containing_invariant_subgroup_count"])
        self.assertEqual(26183, certificate["target10_boundary_count"])
        self.assertEqual(22641, certificate["faithful_boundary_count"])
        self.assertEqual(3542, certificate["nonfaithful_boundary_count"])
        self.assertEqual(204, certificate["retained_count"])
        self.assertEqual(204, certificate["retained_distinct_adjacency_count"])
        self.assertEqual(
            [
                {"omega": 5, "radical_size": 8, "count": 8},
                {"omega": 6, "radical_size": 4, "count": 56},
                {"omega": 9, "radical_size": 4, "count": 140},
            ],
            certificate["retained_joint_signature_distribution"],
        )
        self.assertEqual(
            [8, 28, 56, 112],
            sorted(record["size"] for record in certificate["retained_automorphism_orbits"]),
        )
        self.assertEqual(
            [0, 6], certificate["all_even_extension_obstruction"]["derived_subgroup_vertices"]
        )


if __name__ == "__main__":
    unittest.main()
