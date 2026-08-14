#!/usr/bin/env python3
"""Build and verify the canonical bounded cutoff-eight certificate."""

from __future__ import annotations

import argparse
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

from h8_bounded_cutoff import exact_bounded_certificate, sha256


def _display_path(path: Path, root: Path) -> str:
    value = path if path.is_absolute() else root / path
    value = value.resolve()
    try:
        return str(value.relative_to(root.resolve()))
    except ValueError:
        return str(value)


def _record(path: Path, root: Path) -> Dict[str, str]:
    return {"path": _display_path(path, root), "sha256": sha256(path)}


def build_document(args: argparse.Namespace, root: Path) -> Dict[str, object]:
    delegations = {}
    for specification in args.delegation:
        key, raw_path = specification.split("=", 1)
        if key in delegations:
            raise ValueError("duplicate delegation key: " + key)
        delegations[key] = Path(raw_path)
    certificate = exact_bounded_certificate(
        ordinary_batch_documents=args.ordinary_batch,
        generic_exports=args.generic_export,
        sg192_document=args.sg192_document,
        sg261_document=args.sg261_document,
        sg261_export=args.sg261_export,
        delegation_paths=delegations,
        root=root,
    )
    producer = Path(__file__).with_name("h8_bounded_cutoff.py")
    dual_producer = Path(__file__).with_name("h8_order64_dual.py")
    runner = Path(__file__)
    return {
        "schema_version": 1,
        "status": "[COMPUTED] center quotients |Q|<=81 only; no global h(8) upper bound",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "inputs": {
            "ordinary_batches": [_record(path, root) for path in args.ordinary_batch],
            "generic_exports": [_record(path, root) for path in args.generic_export],
            "sg192_document": _record(args.sg192_document, root),
            "sg261_document": _record(args.sg261_document, root),
            "sg261_export": _record(args.sg261_export, root),
            "delegations": {
                key: _record(path, root)
                for key, path in sorted(delegations.items())
            },
        },
        "producer": _display_path(producer, root),
        "producer_sha256": sha256(producer),
        "dual_producer": _display_path(dual_producer, root),
        "dual_producer_sha256": sha256(dual_producer),
        "runner": _display_path(runner, root),
        "runner_sha256": sha256(runner),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
    }


def _checked_path(record: Dict[str, str], root: Path) -> Path:
    path = Path(record["path"])
    if not path.is_absolute():
        path = root / path
    if sha256(path) != record["sha256"]:
        raise AssertionError("bounded cutoff-eight input hash mismatch: " + str(path))
    return path


def verify_saved_document(document_path: Path, root: Path) -> None:
    document = json.loads(document_path.read_text(encoding="utf-8"))
    for field in ("producer", "dual_producer", "runner"):
        path = Path(document[field])
        if not path.is_absolute():
            path = root / path
        if sha256(path) != document[field + "_sha256"]:
            raise AssertionError("bounded cutoff-eight source hash mismatch: " + field)
    inputs = document["inputs"]
    ordinary = [_checked_path(record, root) for record in inputs["ordinary_batches"]]
    generic = [_checked_path(record, root) for record in inputs["generic_exports"]]
    sg192_document = _checked_path(inputs["sg192_document"], root)
    sg261_document = _checked_path(inputs["sg261_document"], root)
    sg261_export = _checked_path(inputs["sg261_export"], root)
    delegations = {
        key: _checked_path(record, root)
        for key, record in inputs["delegations"].items()
    }
    rebuilt = exact_bounded_certificate(
        ordinary_batch_documents=ordinary,
        generic_exports=generic,
        sg192_document=sg192_document,
        sg261_document=sg261_document,
        sg261_export=sg261_export,
        delegation_paths=delegations,
        root=root,
    )
    if document["certificate"] != rebuilt:
        raise AssertionError("saved bounded cutoff-eight certificate changed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ordinary-batch", type=Path, action="append", required=True)
    parser.add_argument("--generic-export", type=Path, action="append", required=True)
    parser.add_argument("--sg192-document", type=Path, required=True)
    parser.add_argument("--sg261-document", type=Path, required=True)
    parser.add_argument("--sg261-export", type=Path, required=True)
    parser.add_argument(
        "--delegation", action="append", required=True,
        help="delegated artifact in KEY=PATH form",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    document = build_document(args, Path.cwd())
    args.output.write_text(
        json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    certificate = document["certificate"]
    ordinary = certificate["ordinary"]
    generic = certificate["generic_order64_dual"]
    lines = [
        document["status"],
        "ordinary_boundary_rows=%d distinct_adjacencies=%d omega8_rows=%d omega_ge9_distinct=%d"
        % (
            ordinary["former_clique_ge_8_row_count"],
            ordinary["distinct_stored_adjacency_count"],
            ordinary["omega_eight_row_count"],
            ordinary["omega_at_least_nine_distinct_adjacency_count"],
        ),
        "generic_quotients=%d retained_no9=%d boundary9=%d faithful=%d"
        % (
            generic["quotient_count"],
            generic["retained_no_nine_subgroup_count"],
            generic["pruned_boundary_subgroup_count"],
            generic["faithful_candidate_count"],
        ),
        "special_minimum_omega=%r bounded_maximum_a=%d examples_a_gt_10=%d"
        % (
            [record["minimum_omega"] for record in certificate["special_order64"]],
            certificate["bounded_maximum_a_at_nu_at_most_eight"],
            certificate["bounded_example_with_a_greater_than_10_count"],
        ),
        "wrote %s" % args.output,
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
