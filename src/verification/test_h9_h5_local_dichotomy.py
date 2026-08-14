"""Regression test for the cutoff-nine local clique-five dichotomy."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.verification.verify_h9_h5_local_dichotomy import build_certificate


REPOSITORY = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    REPOSITORY / "experiments" / "logs" / "h9_h5_local_dichotomy.json"
)


class H9H5LocalDichotomyTests(unittest.TestCase):
    def test_saved_certificate(self):
        saved = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        self.assertEqual(saved, build_certificate())
        self.assertEqual("[COMPUTED]", saved["status"])
        self.assertEqual(225, saved["target_record_count"])
        self.assertEqual(84, saved["exact_center_record_count"])
        self.assertEqual(
            [("scalar", 28, 2), ("determinant", 56, 4)],
            [
                (
                    record["name"],
                    record["count"],
                    record["commutator_image_order"],
                )
                for record in saved["types"]
            ],
        )


if __name__ == "__main__":
    unittest.main()
