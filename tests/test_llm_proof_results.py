from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from sync_llm_proof_results import collect_known_resolutions  # noqa: E402


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
