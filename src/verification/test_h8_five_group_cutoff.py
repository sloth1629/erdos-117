"""Regression test for the bounded finite 5-group cutoff-eight inventory."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "python"))

from analyze_h8_five_group_cutoff import verify_saved_document  # noqa: E402


class H8FiveGroupCutoffTests(unittest.TestCase):
    def test_saved_five_group_inventory(self):
        path = REPOSITORY / "experiments/logs/h8_five_group_cutoff.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            "[COMPUTED] finite SmallGroups of orders 5^3 through 5^6 only; no classification beyond scanned orders",
            document["status"],
        )
        certificate = document["certificate"]
        self.assertEqual(781, certificate["total_smallgroups"])
        self.assertEqual(80, certificate["eligible_count"])
        self.assertEqual(701, certificate["excluded_by_nine_clique_count"])
        self.assertEqual(0, certificate["nu_eight_count"])
        self.assertEqual(6, certificate["maximum_a_among_eligible"])
        self.assertEqual(26, certificate["eligible_abelian_count"])
        self.assertEqual(54, certificate["eligible_nonabelian_count"])
        self.assertTrue(certificate["all_eligible_are_ac"])
        self.assertTrue(certificate["all_eligible_have_a_equal_nu"])
        self.assertTrue(certificate["all_eligible_nonabelian_have_center_index_25"])
        self.assertTrue(
            certificate["all_eligible_nonabelian_have_twin_quotient_order_7"]
        )
        self.assertEqual(
            [(125, 5), (625, 11), (3125, 22), (15625, 42)],
            [
                (record["order"], record["eligible_count"])
                for record in certificate["by_order"]
            ],
        )
        verify_saved_document(path, REPOSITORY)


if __name__ == "__main__":
    unittest.main()
