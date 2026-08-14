"""Regression test for the repaired SG261 target-nine scalar bridge."""

from __future__ import annotations

import unittest

from src.verification.verify_h8_sg261_target9_scalar_bridge import (
    EXPECTED_DISTRIBUTION,
    verify_saved_certificate,
)


class H8SG261TargetNineScalarBridgeTests(unittest.TestCase):
    def test_saved_certificate(self):
        saved = verify_saved_certificate()
        self.assertEqual("[COMPUTED]", saved["status"])
        self.assertEqual(2048, saved["character_count"])
        self.assertEqual(
            {str(key): value for key, value in EXPECTED_DISTRIBUTION.items()},
            saved["exact_omega_distribution"],
        )
        self.assertEqual(0, saved["omega_eight_count"])
        self.assertEqual(0, saved["omega_nine_count"])
        self.assertEqual(1152, saved["h7_scalar_good_count"])
        self.assertEqual(1152, saved["h7_affine_good_count"])
        self.assertEqual(1152, saved["target9_good_count"])
        self.assertEqual(896, saved["target9_boundary_count"])
        self.assertEqual(
            saved["h7_scalar_good_indices_sha256"],
            saved["target9_good_indices_sha256"],
        )
        self.assertEqual(
            saved["h7_affine_good_indices_sha256"],
            saved["target9_good_indices_sha256"],
        )


if __name__ == "__main__":
    unittest.main()
