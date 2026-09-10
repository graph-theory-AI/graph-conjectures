#!/usr/bin/env python3
"""
scraper/bm_review.py — status review of Bondy–Murty Appendix A items via `claude -p`.

For one bm_id (a record in data/bondy_murty_conjectures.json):
  1. Pull the record (statement, attribution, book context, related corpus records).
  2. Compose a user prompt and shell out to `claude -p` with the system prompt at
     scraper/bm_review_system_prompt.md, --allowed-tools "WebSearch WebFetch Read Write",
     wrapped in scripts/timeout_claude.py for a hard timeout.
  3. Claude saves the review JSON to data/bondy_murty_reviews/<bm_id>.json.

Same review schema as the arXiv pipeline (scraper/arxiv_review.py), so
scraper/build.py attaches the result with the same code path.

Usage
-----
    PER_REVIEW_TIMEOUT=900 python scraper/bm_review.py --bm-id bm-041
    python scraper/bm_review.py --all --jobs 6          # every unreviewed record, 6 at a time
    python scraper/bm_review.py --bm-id bm-041 --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

PROJECT            = Path(__file__).resolve().parent.parent
SYSTEM_PROMPT_PATH = Path(__file__).parent / "bm_review_system_prompt.md"
TIMEOUT_SCRIPT     = PROJECT / "scripts" / "timeout_claude.py"
PER_REVIEW_TIMEOUT = int(os.environ.get("PER_REVIEW_TIMEOUT", 900))

log = logging.getLogger(__name__)


def _load_records(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def _build_user_prompt(rec: dict, out_path: Path) -> str:
    src = rec.get("source", {})
    lines = [
        "Review the following graph-theory conjecture and determine its current status as of today.",
        "",
        "============================================================",
        "  SOURCE",
        "============================================================",
        f"Book       : {src.get('title', '')}",
        f"Item       : Appendix A, item {rec.get('appendix_number')} "
        f"(section: {rec.get('section', '')}; book p. {src.get('book_page')}, PDF p. {src.get('pdf_page')})",
        f"URL        : {src.get('url', '')}",
        f"English ed.: {src.get('english_edition', '')}",
        "",
        "============================================================",
        f"  CONJECTURE   ({rec.get('kind', 'Conjecture')})",
        "============================================================",
        f"Name / title       : {rec.get('title', '')}",
        f"Attributed to      : {rec.get('attributed_to', '')}"
        + (f" ({rec.get('attributed_year')})" if rec.get("attributed_year") else ""),
        f"Book cross-refs    : {', '.join(rec.get('book_refs') or []) or '(none)'}",
        "",
        "Statement (do not paraphrase in the summary):",
        "------------------------------------------------------------",
        rec.get("statement_text", ""),
        "",
        "Context / definitions from the book:",
        "------------------------------------------------------------",
        rec.get("context_text", "") or "(none)",
    ]
    if rec.get("notes"):
        lines += ["", "Editorial notes:", "------------------------------------------------------------", rec["notes"]]

    related = rec.get("related") or []
    if related:
        lines += [
            "",
            "============================================================",
            f"  RELATED RECORDS ALREADY IN OUR CORPUS ({len(related)})",
            "============================================================",
            "Context only — they tell you which nearby statements we already track.",
            "",
        ]
        for r in related:
            if r.get("corpus") == "opg":
                lines.append(f"  - OPG: {r.get('slug')}  ({r.get('note', '')})  "
                             f"http://www.openproblemgarden.org/op/{r.get('slug')}")
            else:
                lines.append(f"  - {r.get('corpus')}: {r.get('id') or r.get('slug')}  ({r.get('note', '')})")

    lines += [
        "",
        "============================================================",
        "  OUTPUT INSTRUCTIONS",
        "============================================================",
        "Issue your WebSearch / WebFetch calls in parallel where possible "
        "(multiple tool calls per assistant turn). Cap total web calls at 8. "
        "Verify every URL with WebFetch before citing.",
        "",
        "Save the review as a JSON object (raw, no <tags>, no code fences) to "
        "this EXACT path using the Write tool:",
        "",
        f"  {out_path}",
        "",
        "Include these extra fields in the JSON object on top of the schema in your instructions:",
        f"  - \"review_id\":        \"{rec.get('bm_id')}\"",
        f"  - \"bm_id\":            \"{rec.get('bm_id')}\"",
        f"  - \"appendix_number\":  {rec.get('appendix_number')}",
        f"  - \"conjecture_title\": \"{(rec.get('title') or '').replace(chr(34), chr(39))}\"",
        "  - \"reviewed_at\":      today's date in YYYY-MM-DD form",
        "  - \"model\":            the model name you are running as",
        "  - \"search_enabled\":   true",
        "",
        f"After writing, output one line: "
        f"done: {rec.get('bm_id')} -> <status> (<confidence>, <N> cites)",
    ]
    return "\n".join(lines)


def review_one(rec: dict, out_dir: Path, model: str, dry_run: bool = False) -> int:
    out_path = out_dir / f"{rec['bm_id']}.json"
    if out_path.exists():
        log.info("  skip (already reviewed): %s", rec["bm_id"])
        return 0
    user_prompt = _build_user_prompt(rec, out_path.resolve())
    if dry_run:
        print(user_prompt)
        return 0
    if not SYSTEM_PROMPT_PATH.exists():
        log.error("system prompt not found: %s", SYSTEM_PROMPT_PATH)
        return 1
    system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
    cmd = [
        sys.executable, str(TIMEOUT_SCRIPT), str(PER_REVIEW_TIMEOUT),
        "claude", "-p", user_prompt,
        "--append-system-prompt", system_prompt,
        "--allowed-tools", "WebSearch WebFetch Read Write",
        "--output-format", "text",
        "--model", model,
        "--no-session-persistence",
    ]
    log.info("  running claude (timeout=%ds) for %s …", PER_REVIEW_TIMEOUT, rec["bm_id"])
    try:
        result = subprocess.run(cmd, timeout=PER_REVIEW_TIMEOUT + 30,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    except subprocess.TimeoutExpired:
        log.error("  claude timed out for %s", rec["bm_id"])
        return 1
    tail = (result.stdout or "").strip().splitlines()[-1:] or [""]
    if not out_path.exists():
        log.error("  FAILED %s (exit=%d, no JSON written): %s", rec["bm_id"], result.returncode, tail[0][:200])
        return 1
    log.info("  saved %s  |  %s", out_path.name, tail[0][:160])
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--bm-id", help="Record id, e.g. bm-041")
    g.add_argument("--all", action="store_true", help="Review every record without a review JSON")
    ap.add_argument("--records", type=Path, default=PROJECT / "data" / "bondy_murty_conjectures.json")
    ap.add_argument("--out-dir", type=Path, default=PROJECT / "data" / "bondy_murty_reviews")
    ap.add_argument("--model",   default="claude-sonnet-4-6")
    ap.add_argument("--jobs",    type=int, default=1, help="parallel claude processes for --all")
    ap.add_argument("--dry-run", action="store_true", help="Print the composed prompt; do not call claude.")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s  %(levelname)-7s  %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )
    args.out_dir.mkdir(parents=True, exist_ok=True)
    records = _load_records(args.records)

    if args.bm_id:
        rec = next((r for r in records if r.get("bm_id") == args.bm_id), None)
        if rec is None:
            log.error("bm_id %s not found in %s", args.bm_id, args.records)
            return 1
        return review_one(rec, args.out_dir, args.model, args.dry_run)

    todo = [r for r in records if not (args.out_dir / f"{r['bm_id']}.json").exists()]
    log.info("%d record(s) to review (%d already done), jobs=%d", len(todo), len(records) - len(todo), args.jobs)
    failures = 0
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futs = {pool.submit(review_one, r, args.out_dir, args.model, args.dry_run): r["bm_id"] for r in todo}
        for f in as_completed(futs):
            try:
                failures += 1 if f.result() else 0
            except Exception as e:  # noqa: BLE001
                failures += 1
                log.error("  %s raised: %s", futs[f], e)
    log.info("done: %d failure(s)", failures)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
