"""Regression test for the binary rank-three order-64 tail."""

from __future__ import annotations

import unittest

from src.verification.verify_rank3_order64_tail import (
    EXPECTED_EXTERIOR_ZERO,
    EXPECTED_GENERIC,
    EXPECTED_ORDINARY_ALL_NONFAITHFUL,
    EXPECTED_ORDINARY_MINIMUM_OMEGA,
    EXPECTED_STRUCTURAL_IDS,
    verify_rank3_order64_tail,
)


class RankThreeOrder64TailTests(unittest.TestCase):
    def test_complete_order64_tail(self):
        result = verify_rank3_order64_tail(rebuild_dependencies=True)
        census = result["structural_census"]
        self.assertEqual(44, census["base_predicate_count"])
        self.assertEqual(39, census["structural_predicate_count"])
        self.assertEqual(list(EXPECTED_STRUCTURAL_IDS), census["structural_predicate_ids"])

        partition = result["partition"]
        ordinary = partition["ordinary_faithful_exact_omega_at_least_12"]
        self.assertEqual(
            {str(key): value for key, value in EXPECTED_ORDINARY_MINIMUM_OMEGA.items()},
            ordinary["minimum_exact_omega_by_id"],
        )
        self.assertEqual(12, ordinary["minimum_exact_omega"])
        self.assertEqual(
            list(EXPECTED_ORDINARY_ALL_NONFAITHFUL), ordinary["all_nonfaithful_ids"]
        )
        self.assertEqual(
            list(EXPECTED_GENERIC), partition["generic_no_faithful_candidate"]["ids"]
        )
        self.assertEqual(
            list(EXPECTED_EXTERIOR_ZERO), partition["exterior_zero"]["ids"]
        )


if __name__ == "__main__":
    unittest.main()
