#!/usr/bin/env python3
"""Run redundant exact certificates for scalar symplectic groups."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from scalar_symplectic import analyze_scalar_symplectic


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = args.config.read_bytes()
    configuration = json.loads(raw)
    records = [
        analyze_scalar_symplectic(int(entry["prime"]), int(entry["rank"]))
        for entry in configuration["groups"]
    ]
    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "configuration": str(args.config),
        "configuration_sha256": hashlib.sha256(raw).hexdigest(),
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for record in records:
        exclusion = record["projective_clique_exclusion"]
        print(
            "%s: |G|=%d |Z|=%d compressed=%d nu=%d a=%d; no %d-clique on %d projective points (%d nodes)"
            % (
                record["group_id"],
                record["group_order"],
                record["center_order"],
                record["compressed_vertex_count"],
                record["nu"],
                record["a"],
                exclusion["excluded_clique_size"],
                exclusion["projective_vertex_count"],
                exclusion["search_nodes"],
            )
        )
    print("wrote %d certified records to %s" % (len(records), args.output))


if __name__ == "__main__":
    main()
