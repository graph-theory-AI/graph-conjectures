from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scraper"))

from sync_llm_proof_results import (  # noqa: E402
    ILL_POSED_DISCLAIMER,
    collect_ill_posed,
    collect_known_resolutions,
)
from build import _virtual_problem_from_arxiv  # noqa: E402
from conjecture_names import names_by_id  # noqa: E402


class LlmProofResultTests(unittest.TestCase):
    def test_checked_in_results_are_known_literature_resolutions(self):
        payload = json.loads((ROOT / "data" / "llm_proof_results.json").read_text())
        self.assertEqual(len(payload["results"]), 32)
        self.assertEqual(
            {status: sum(r["site_status"] == status for r in payload["results"])
             for status in ("solved", "disproved")},
            {"solved": 25, "disproved": 7},
        )
        self.assertTrue(all(r["article_title"] and r["article_url"]
                            for r in payload["results"]))
        imported_ids = {r["id"] for r in payload["results"]}
        self.assertTrue({
            "1701.03366__00",
            "2510.11311__04",
            "2603.02786__01",
            "2603.02786__04",
            "finding_k_edge_outerplanar_graph_embeddings",
            "imbalance_conjecture",
            "three_chromatic_0_2_graphs",
        }.issubset(imported_ids))
        self.assertNotIn(
            "2402.10782__01",
            imported_ids,
            "partial prior art must not promote a campaign result",
        )

    def test_checked_in_ai_writeups_are_reviewed_pdf_artifacts(self):
        payload = json.loads((ROOT / "data" / "llm_proof_results.json").read_text())
        writeups = payload["ai_results"]
        self.assertEqual(len(writeups), 23)
        self.assertEqual(
            {status: sum(r["site_status"] == status and r["promote_status"]
                         for r in writeups)
             for status in ("ai-proved", "ai-disproved")},
            {"ai-proved": 11, "ai-disproved": 12},
        )
        self.assertTrue(all(r["promote_status"] for r in writeups))
        self.assertTrue(all(r["pdf_url"].endswith(".pdf") for r in writeups))
        self.assertTrue(all(r["review_verdict"] == "CONFIRMED" for r in writeups))
        self.assertTrue(all("audit_url" not in r and "review_summary" not in r
                            for r in writeups))
        imported_ids = {r["id"] for r in writeups}
        self.assertNotIn("1602.05184__00", imported_ids)
        self.assertNotIn("imbalance_conjecture", imported_ids)

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

            results = collect_ill_posed(source)

        self.assertEqual([result["id"] for result in results], ["a__00"])
        self.assertTrue(results[0]["artifact_url"].endswith("/attacks/a__00"))
        self.assertIn("unrefereed", ILL_POSED_DISCLAIMER)

    def test_checked_in_ill_posed_results_match_catalog_ids(self):
        payload = json.loads((ROOT / "data" / "llm_proof_results.json").read_text())
        self.assertIn("unrefereed", payload["ill_posed_disclaimer"])
        ill_posed = payload["ill_posed_results"]
        self.assertTrue(all(r["verdict"] == "ill_posed" for r in ill_posed))
        result_ids = {result["id"] for result in ill_posed}

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
        # A diagnostic never doubles as a literature or AI status.
        self.assertFalse(result_ids & {r["id"] for r in payload["results"]})
        self.assertFalse(result_ids & {r["id"] for r in payload["ai_results"]})

    def test_checked_in_results_carry_canonical_names(self):
        payload = json.loads((ROOT / "data" / "llm_proof_results.json").read_text())
        names = names_by_id()
        for key in ("results", "ai_results", "ill_posed_results"):
            for result in payload[key]:
                with self.subTest(list=key, id=result["id"]):
                    self.assertEqual(result["name"], names[result["id"]])

    def test_source_import_matches_checked_in_data(self):
        source = ROOT.parent / "Graph-Theory-LLM-Proofs"
        if not source.is_dir():
            self.skipTest("sibling Graph-Theory-LLM-Proofs checkout not available")
        expected = collect_known_resolutions(source)
        checked_in = json.loads((ROOT / "data" / "llm_proof_results.json").read_text())
        self.assertEqual(checked_in, expected)

        readme = (source / "README.md").read_text(encoding="utf-8")
        for result in checked_in["ai_results"]:
            relative_pdf = result["pdf_url"].split("/blob/main/", 1)[1]
            self.assertIn(f"({relative_pdf})", readme)


if __name__ == "__main__":
    unittest.main()
