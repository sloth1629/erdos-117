"""Regression test for the local centralizer-index counterexample."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "python"))

from analyze_h8_local_inequality_counterexample import (  # noqa: E402
    verify_saved_document,
)


class H8LocalInequalityCounterexampleTests(unittest.TestCase):
    def test_saved_counterexample(self):
        path = REPOSITORY / "experiments/logs/h8_local_inequality_counterexample.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            "[DISPROVED] [G:C_G(x)] <= nu(G)-nu(C_G(x))",
            document["status"],
        )
        certificate = document["certificate"]
        self.assertEqual([48, 15], certificate["small_group"])
        self.assertEqual(12, certificate["group_exact_graph_record"]["nu"])
        self.assertEqual(12, certificate["group_exact_graph_record"]["a"])
        self.assertEqual(4, certificate["centralizer"]["order"])
        self.assertEqual(1, certificate["centralizer"]["exact_graph_record"]["nu"])
        self.assertEqual(
            (12, 11),
            (
                certificate["disproved_inequality"]["left_side"],
                certificate["disproved_inequality"]["right_side"],
            ),
        )
        verify_saved_document(path, REPOSITORY)


if __name__ == "__main__":
    unittest.main()
