"""Regression tests for the scalar twisted-tensor certificate bundle."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
BUNDLE = REPOSITORY / "results" / "scalar_twisted_tensor"


def run_script(script: str, *arguments: Path) -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(BUNDLE / "scripts" / script), *(str(x) for x in arguments)],
        cwd=BUNDLE,
        env=environment,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


class ScalarTwistedTensorBundleTests(unittest.TestCase):
    def test_saved_certificates(self):
        w73 = run_script(
            "verify_w73_q3_twisted_tensor_certificate.py",
            BUNDLE / "certificates" / "W73_Q3_TWISTED_TENSOR_28.json",
        )
        self.assertIn("projective_points=28", w73)
        self.assertIn("unordered_pairs_checked=378", w73)

        w53 = run_script(
            "verify_w53_q3_certificate.py",
            BUNDLE / "certificates" / "W53_Q3_NORM_ONE_13.json",
        )
        self.assertIn("projective_points=13", w53)
        self.assertIn("unordered_pairs_checked=78", w53)

        arithmetic = run_script("verify_scalar_pointwise_audit.py")
        self.assertIn("all arithmetic used exact integers", arithmetic)

    def test_generators_reproduce_saved_certificates(self):
        with tempfile.TemporaryDirectory(prefix="e117-scalar-") as temporary:
            temporary_path = Path(temporary)
            generated_w73 = temporary_path / "W73.json"
            generated_w53 = temporary_path / "W53.json"
            run_script("generate_w73_q3_twisted_tensor_certificate.py", generated_w73)
            run_script("generate_w53_q3_certificate.py", generated_w53)
            self.assertEqual(
                (BUNDLE / "certificates" / "W73_Q3_TWISTED_TENSOR_28.json").read_bytes(),
                generated_w73.read_bytes(),
            )
            self.assertEqual(
                (BUNDLE / "certificates" / "W53_Q3_NORM_ONE_13.json").read_bytes(),
                generated_w53.read_bytes(),
            )

    def test_manifest(self):
        for line in (BUNDLE / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
            expected, relative = line.split(maxsplit=1)
            target = BUNDLE / relative.removeprefix("./")
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
            self.assertEqual(expected, actual, relative)


if __name__ == "__main__":
    unittest.main()
