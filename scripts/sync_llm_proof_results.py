#!/usr/bin/env python3
"""Import publishable LLM-proof attack metadata into the site repository.

Only verdicts that describe the supplied catalog statement as ill-posed are
currently exported. The full writeups stay in Graph-Theory-LLM-Proofs; this
creates a small, stable data artifact for the static-site build.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPOSITORY_URL = "https://github.com/graph-theory-AI/Graph-Theory-LLM-Proofs"


def collect_ill_posed(source_dir: Path) -> dict:
    attacks_dir = source_dir / "attacks"
    if not attacks_dir.is_dir():
        raise FileNotFoundError(f"attack directory not found: {attacks_dir}")

    results = []
    for verdict_path in sorted(attacks_dir.glob("*/verdict.json")):
        verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
        if verdict.get("verdict") != "ill_posed":
            continue

        review_id = verdict.get("id") or verdict_path.parent.name
        if review_id != verdict_path.parent.name:
            raise ValueError(
                f"verdict id {review_id!r} does not match {verdict_path.parent.name!r}"
            )
        results.append({
            "id": review_id,
            "verdict": "ill_posed",
            "confidence": verdict.get("confidence", "unknown"),
            "one_line": verdict.get("one_line", ""),
            "caveats": verdict.get("caveats", ""),
            "would_publish": bool(verdict.get("would_publish", False)),
            "model": verdict.get("model", ""),
            "assessed_at": verdict.get("when", ""),
            "artifact_url": f"{REPOSITORY_URL}/tree/main/attacks/{review_id}",
        })

    return {
        "schema_version": 1,
        "source_repository": REPOSITORY_URL,
        "methodology_url": f"{REPOSITORY_URL}#readme",
        "disclaimer": (
            "Attack verdicts are unrefereed model self-reports. An ill-posed "
            "label is a diagnostic of the catalog statement supplied to the "
            "model, not a literature-review status or a peer-reviewed result."
        ),
        "results": results,
    }


def main() -> int:
    project = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=project.parent / "Graph-Theory-LLM-Proofs",
        help="checkout containing attacks/*/verdict.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=project / "data" / "llm_proof_results.json",
    )
    args = parser.parse_args()

    payload = collect_ill_posed(args.source_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(payload['results'])} ill-posed result(s) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
