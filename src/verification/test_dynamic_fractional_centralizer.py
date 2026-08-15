"""Regression test for the exact dynamic-centralizer certificate bundle."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from src.verification.verify_dynamic_fractional_centralizer import main


class DynamicFractionalCentralizerTests(unittest.TestCase):
    def test_saved_certificate_bundle(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            main()
        text = output.getvalue()
        self.assertIn("28672 / 28672", text)
        self.assertIn("all exact certificates verified", text)


if __name__ == "__main__":
    unittest.main()
