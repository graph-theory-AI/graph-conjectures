from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scraper"))

from sync_llm_proof_results import collect_ill_posed  # noqa: E402
from build import _virtual_problem_from_arxiv  # noqa: E402


class LlmProofResultTests(unittest.TestCase):
    def test_ill_posed_is_a_tag_and_does_not_replace_status(self):
        review = {"status": "open"}
        attack = {"verdict": "ill_posed"}
        row = _virtual_problem_from_arxiv({
            "arxiv_id": "2600.00001",
            "paper_authors": [],
            "_review": review,
            "_llm_attack": attack,
        })
        self.assertEqual(row["_review"]["status"], "open")
        self.assertIs(row["_llm_attack"], attack)
        self.assertNotIn("_display_status", row)

    def test_collects_only_ill_posed_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            for review_id, verdict in (("a__00", "ill_posed"), ("b__00", "partial")):
                attack = source / "attacks" / review_id
                attack.mkdir(parents=True)
                (attack / "verdict.json").write_text(json.dumps({
                    "id": review_id,
                    "verdict": verdict,
                    "confidence": "high",
                    "one_line": "Reason",
                    "caveats": "Caveat",
                    "model": "model",
                    "when": "2026-09-01T00:00:00Z",
                }))

            payload = collect_ill_posed(source)

        self.assertEqual([result["id"] for result in payload["results"]], ["a__00"])
        self.assertTrue(payload["results"][0]["artifact_url"].endswith("/attacks/a__00"))
        self.assertIn("unrefereed", payload["disclaimer"])

    def test_checked_in_results_match_catalog_ids(self):
        payload = json.loads((ROOT / "data" / "llm_proof_results.json").read_text())
        result_ids = {result["id"] for result in payload["results"]}

        counters: dict[str, int] = {}
        catalog_ids = set()
        records = json.loads((ROOT / "data" / "arxiv_conjectures.json").read_text())
        for record in records:
            safe_id = record.get("safe_id") or record["arxiv_id"].replace("/", "_")
            index = counters.get(safe_id, 0)
            counters[safe_id] = index + 1
            catalog_ids.add(f"{safe_id}__{index:02d}")

        self.assertEqual(len(result_ids), 23)
        self.assertTrue(result_ids <= catalog_ids)


if __name__ == "__main__":
    unittest.main()
