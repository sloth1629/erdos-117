"""Regression test for the bounded finite 3-group cutoff-eight inventory."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "python"))

from analyze_h8_three_group_cutoff import verify_saved_document  # noqa: E402


class H8ThreeGroupCutoffTests(unittest.TestCase):
    def test_saved_three_group_inventory(self):
        path = REPOSITORY / "experiments/logs/h8_three_group_cutoff.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            "[COMPUTED] finite SmallGroups of orders 3 through 729 only; no all-finite-3-group theorem; order 2187 not scanned",
            document["status"],
        )
        certificate = document["certificate"]
        self.assertEqual(594, certificate["total_smallgroups"])
        self.assertEqual(92, certificate["eligible_count"])
        self.assertEqual(502, certificate["excluded_by_nine_clique_count"])
        self.assertEqual(0, certificate["nu_eight_count"])
        self.assertEqual(10, certificate["maximum_a_among_eligible"])
        self.assertEqual(83, certificate["eligible_ac_count"])
        self.assertEqual(9, certificate["eligible_non_ac_count"])
        self.assertEqual(9, certificate["eligible_a_greater_nu_count"])
        self.assertTrue(
            certificate[
                "all_eligible_maximum_clique_centralizers_are_maximal_except_abelian"
            ]
        )
        self.assertEqual(
            {"1": [[1]], "4": [[3, 3, 3, 3]], "7": [[3] * 7]},
            certificate["centralizer_cover_signatures_by_nu"],
        )
        self.assertEqual(2187, certificate["unscanned_next_order"])
        self.assertEqual(9310, certificate["unscanned_next_order_smallgroups_count"])
        self.assertEqual(
            [(3, 1), (9, 2), (27, 5), (81, 11), (243, 24), (729, 49)],
            [
                (record["order"], record["eligible_count"])
                for record in certificate["by_order"]
            ],
        )
        verify_saved_document(path, REPOSITORY)


if __name__ == "__main__":
    unittest.main()
