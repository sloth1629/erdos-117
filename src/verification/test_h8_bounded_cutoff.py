"""Independent saved-artifact regressions for bounded cutoff eight."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "python"))

from analyze_h8_literature_candidate_inventory import (  # noqa: E402
    verify_saved_document as verify_candidate_inventory,
)
from analyze_h8_sg108_exterior_scan import (  # noqa: E402
    verify_saved_document as verify_sg108_scan,
)
from run_h8_bounded_cutoff import (  # noqa: E402
    verify_saved_document as verify_bounded_cutoff,
)


class H8BoundedCertificateTests(unittest.TestCase):
    def test_h8_bounded_cutoff_saved_certificate(self):
        path = REPOSITORY / "experiments/logs/h8_bounded_cutoff.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            "[COMPUTED] center quotients |Q|<=81 only; no global h(8) upper bound",
            document["status"],
        )
        certificate = document["certificate"]
        self.assertEqual(4, certificate["ordinary"]["omega_eight_row_count"])
        self.assertEqual(
            0, certificate["generic_order64_dual"]["faithful_candidate_count"]
        )
        self.assertEqual(10, certificate["bounded_maximum_a_at_nu_at_most_eight"])
        verify_bounded_cutoff(path, REPOSITORY)

    def test_h8_post_81_candidate_inventory(self):
        path = REPOSITORY / "experiments/logs/h8_literature_candidate_inventory.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        records = document["certificate"]["records"]
        self.assertEqual(
            [([96, 227], 24), ([108, 41], 84), ([144, 196], 19775)],
            [(record["small_group"], record["normal_kernel_count"]) for record in records],
        )
        self.assertEqual([29, 5, 10], [record["abstract_q_omega"] for record in records])
        self.assertEqual(
            [
                "excluded_by_abstract_quotient_clique",
                "requires_exterior_kernel_scan",
                "excluded_by_abstract_quotient_clique",
            ],
            [record["cutoff8_disposition"] for record in records],
        )
        verify_candidate_inventory(path, REPOSITORY)

    def test_h8_sg108_complete_normal_kernel_scan(self):
        path = REPOSITORY / "experiments/logs/h8_sg108_exterior_scan.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        certificate = document["certificate"]
        self.assertEqual(84, certificate["normal_kernel_count"])
        self.assertEqual(38, certificate["status_distribution"]["nonfaithful_radical"])
        self.assertEqual(46, certificate["status_distribution"]["clique_ge_9"])
        self.assertEqual(20, certificate["minimum_faithful_omega"])
        self.assertEqual(0, certificate["candidate_count"])
        verify_sg108_scan(path, REPOSITORY)


if __name__ == "__main__":
    unittest.main()
