"""Integrity checks for the Bondy–Murty Appendix A corpus.

data/bondy_murty_conjectures.json is hand-transcribed (via
scripts/bm_build_records.py), so we check that every record is complete, that
ids are consistent with the appendix numbering, and that every `related`
pointer resolves to a record scraper/build.py will actually render.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "scripts"))
from bm_build_records import PDF_OFFSET  # noqa: E402  (book page → PDF page offset, single source of truth)

STATUSES = {"open", "partial", "solved", "disproved", "unclear"}


def _arxiv_review_ids() -> set[str]:
    states = json.loads((DATA / "arxiv_conjectures.json").read_text(encoding="utf-8"))
    counters: dict[str, int] = {}
    ids: set[str] = set()
    for s in states:
        sid = s.get("safe_id") or s.get("arxiv_id", "").replace("/", "_")
        idx = counters.get(sid, 0)
        counters[sid] = idx + 1
        ids.add(f"{sid}__{idx:02d}")
    return ids


class BondyMurtyCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads((DATA / "bondy_murty_conjectures.json").read_text(encoding="utf-8"))
        cls.opg_slugs = {p["slug"] for p in json.loads((DATA / "problems.json").read_text(encoding="utf-8"))}
        cls.arxiv_ids = _arxiv_review_ids()

    def test_record_count_and_ids(self):
        self.assertEqual(len(self.records), 38)
        ids = [r["bm_id"] for r in self.records]
        self.assertEqual(len(ids), len(set(ids)))
        numbers = [r["appendix_number"] for r in self.records]
        self.assertEqual(len(numbers), len(set(numbers)))
        for r in self.records:
            self.assertEqual(r["bm_id"], f"bm-{r['appendix_number']:03d}")
            self.assertTrue(1 <= r["appendix_number"] <= 100)

    def test_required_fields(self):
        for r in self.records:
            with self.subTest(bm_id=r["bm_id"]):
                for key in ("title", "statement_text", "attributed_to", "section", "kind"):
                    self.assertTrue(r.get(key), f"{key} missing")
                self.assertIn(r["kind"], {"Conjecture", "Problem"})
                self.assertIn(r["coverage"], {"missing", "weak"})
                src = r["source"]
                self.assertTrue(src["url"].startswith("https://inria.hal.science/"))
                self.assertEqual(src["pdf_page"], src["book_page"] + PDF_OFFSET)
                self.assertTrue(625 <= src["book_page"] <= 634)

    def test_weak_records_point_at_an_existing_record(self):
        for r in self.records:
            if r["coverage"] != "weak":
                continue
            with self.subTest(bm_id=r["bm_id"]):
                self.assertTrue(r["related"], "weak coverage must name the covering record")

    def test_related_pointers_resolve(self):
        for r in self.records:
            for rel in r.get("related", []):
                with self.subTest(bm_id=r["bm_id"], rel=rel):
                    if rel["corpus"] == "opg":
                        self.assertIn(rel["slug"], self.opg_slugs)
                    elif rel["corpus"] == "arxiv":
                        self.assertIn(rel["id"], self.arxiv_ids)
                    elif rel["corpus"] == "erdosproblems":
                        self.assertTrue(rel["id"].isdigit())
                    else:
                        self.fail(f"unknown corpus {rel['corpus']!r}")

    def test_reviews_are_well_formed(self):
        reviews_dir = DATA / "bondy_murty_reviews"
        if not reviews_dir.exists():
            self.skipTest("no reviews yet")
        ids = {r["bm_id"] for r in self.records}
        for f in sorted(reviews_dir.glob("*.json")):
            with self.subTest(review=f.name):
                rev = json.loads(f.read_text(encoding="utf-8"))
                self.assertIn(f.stem, ids)
                self.assertEqual(rev.get("bm_id"), f.stem)
                self.assertIn(rev.get("status"), STATUSES)
                self.assertIn(rev.get("confidence"), {"high", "medium", "low"})
                self.assertTrue(rev.get("summary"))
                if rev["status"] in {"solved", "disproved"}:
                    self.assertTrue(
                        any(ref.get("url") for ref in rev.get("since_posted", [])),
                        "a resolution must cite at least one URL",
                    )


class CuratedCorpusTests(unittest.TestCase):
    """data/curated_conjectures.json: workstream conjectures absent from OPG and arXiv."""

    @classmethod
    def setUpClass(cls):
        cls.records = json.loads((DATA / "curated_conjectures.json").read_text(encoding="utf-8"))
        cls.opg_slugs = {p["slug"] for p in json.loads((DATA / "problems.json").read_text(encoding="utf-8"))}
        cls.arxiv_ids = _arxiv_review_ids()

    def test_ids_and_fields(self):
        ids = [r["id"] for r in self.records]
        self.assertEqual(len(ids), len(set(ids)))
        for r in self.records:
            with self.subTest(id=r["id"]):
                self.assertRegex(r["id"], r"^[a-z0-9][a-z0-9-]*$")
                for key in ("title", "statement_text", "attributed_to", "kind", "source"):
                    self.assertTrue(r.get(key), f"{key} missing")
                self.assertIn(r["kind"], {"Conjecture", "Problem"})
                self.assertTrue(r["source"].get("url"))
                if r.get("workstream"):
                    # The directory may live on another branch until that PR merges, so only
                    # the shape is checked: a relative problems/<name> path, no trailing slash.
                    self.assertRegex(r["workstream"], r"^problems/[A-Za-z0-9_.-]+$")

    def test_related_pointers_resolve(self):
        for r in self.records:
            for rel in r.get("related", []):
                with self.subTest(id=r["id"], rel=rel):
                    if rel["corpus"] == "opg":
                        self.assertIn(rel["slug"], self.opg_slugs)
                    elif rel["corpus"] == "arxiv":
                        self.assertIn(rel["id"], self.arxiv_ids)
                    elif rel["corpus"] == "erdosproblems":
                        self.assertTrue(rel["id"].isdigit())
                    else:
                        self.fail(f"unknown corpus {rel['corpus']!r}")

    def test_reviews_are_well_formed(self):
        reviews_dir = DATA / "curated_reviews"
        if not reviews_dir.exists():
            self.skipTest("no reviews yet")
        ids = {r["id"] for r in self.records}
        for f in sorted(reviews_dir.glob("*.json")):
            with self.subTest(review=f.name):
                rev = json.loads(f.read_text(encoding="utf-8"))
                self.assertIn(f.stem, ids)
                self.assertIn(rev.get("status"), STATUSES)
                self.assertIn(rev.get("confidence"), {"high", "medium", "low"})
                self.assertTrue(rev.get("summary"))
                if rev["status"] in {"solved", "disproved"}:
                    self.assertTrue(any(ref.get("url") for ref in rev.get("since_posted", [])))


if __name__ == "__main__":
    unittest.main()
