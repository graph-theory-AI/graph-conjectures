# Dataset quality assessment — recommended modifications

Assessment date: 2026-08-12. Method: full structural audit of `data/problems.json`,
`data/reviews/*.json`, `data/intersection.json`, plus web spot-verification of 20
citations (all 32 solved/disproved "strong claims" enumerated; 8 of them verified
in depth against the live web, plus 12 partial/open citations — 19/20 fully check
out, zero hallucinated papers found).

## Status (2026-09-23)

| # | Item | Outcome |
|---|------|---------|
| 1 | PTAS label | **Done.** Status stays `solved`. The review now has `solved_before_posting: true` and a `pre_posting_resolution` citation (Kenyon-Mathieu–Schudy, STOC 2007). The problem page shows it, and the README explains it under the status table. |
| 2 | README stats | **Obsolete.** The README no longer quotes citation or confidence totals. Its OPG status table matches the built site. |
| 3 | Empty `statements[]` | **Done.** `parse.py` now falls back to the whole problem block when there is no `envtheorem`. Because `cache/op/` is empty, the 2 records were patched in `data/problems.json` to match what the fallback produces. |
| 4 | `intersection.json` | **Done.** Each row has a `confirmed` flag: 2 true, 13 false. `build.py` reads the flag instead of a hard-coded list, `intersect.py` keeps the flag across re-runs, and the README wording is corrected. |
| 5 | Citation year/venue | **Done (conservative).** The audit's example was wrong: arXiv gives Steffen's paper as *Combinatorica* 35 (2015), so the entry was already correct. I checked all 408 arXiv-backed citations against arXiv metadata and fixed 13: 6 journal years taken from `journal_ref`, 4 "arXiv preprint" venues replaced by the published venue (journal_ref, DOI or Surveys in Combinatorics), and 3 preprint years set to arXiv v1. 91 citations name a journal whose year is later than arXiv v1 and have no `journal_ref`. They look like journal years but are unverified and were left unchanged. |
| 6 | Author-less problems | **Verified.** I fetched all 15 OPG pages again: their "Author(s):" field is empty upstream, so this isn't a selector bug. |

## Recommended fixes, in priority order

### 1. Relabel `ptas_for_feedback_arc_set_in_tournaments` (real labeling issue)

- File: `data/reviews/ptas_for_feedback_arc_set_in_tournaments.json`
- Currently `status: "solved"`, but the PTAS is due to Kenyon-Mathieu & Schudy
  (STOC **2007**), *before* the OPG posting — which contradicts the README's
  definition of `solved` ("proved since posting"). The review summary is
  transparent about this; only the label is off.
- The single citation (Baweja–Jia–Woodruff 2022, arXiv:2107.07141) is a
  *semi-streaming* PTAS — a resource-model refinement, not the resolution.
- Fix: either introduce a distinct status (e.g. `solved_pre_posting`) or keep
  `solved` and add an explicit note field; if a new status is added, update the
  site templates and README status table accordingly.

### 2. Regenerate README statistics (count drift)

- File: `README.md`
- Actual data: **461** citations (README says 459); confidence split
  **151 high / 69 medium / 7 low** (README says 151/68/8).
- Fix: regenerate the stats block from `data/reviews/` rather than hand-editing,
  ideally via a small script so the numbers can't drift again.

### 3. Patch two statement-parsing failures

- File: `data/problems.json` (via `scraper/parse.py`)
- `obstacle_number_of_planar_graphs` and
  `what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian`
  have empty `statements[]` although `statement_html` is present (these two pages
  phrase the problem outside the `envtheorem` div — 225/227 problems have it).
- Consequence: the site renders fine (it uses `statement_html`), but any consumer
  of the plain-text `statements[].text` field (search indexing included) misses
  these two problems.
- Fix: add a fallback in `parse.py` that extracts text from `statement_html`
  when no `envtheorem` statement is found, then re-run parse.

### 4. Clean up or clearly mark `intersection.json` as advisory

- Files: `data/intersection.json`, `README.md`
- At least 6 of the 15 fuzzy matches are wrong pairings, verified against the
  local `data/erdos_graph.json` statements:
  - `chromatic_number_of_common_graphs` → erdős #761 (about *cochromatic* number)
  - `behzads_conjecture` (total colouring) → #631 (list chromatic number)
  - `monochromatoc_reachability_in_arc_colored_digraphs` → #638 (monochromatic-triangle Ramsey family)
  - `erdos_posa_property_for_long_directed_cycles` → #580 (trees in dense graphs)
  - `unfriendly_partitions` → #583 (Gallai path partition)
  - `odd_cycle_transversal_in_triangle_free_graphs` → #24 (counting C₅'s in triangle-free graphs)
- This is well-contained: `scraper/build.py` only surfaces the 2 manually
  confirmed entries (`erdos_faber_lovasz_conjecture` → #19,
  `the_erdos_hajnal_conjecture` → #61 — both correct).
- Fix: either prune the wrong rows, or add a `"confirmed": true/false` field per
  row; and soften the README wording — it currently calls the file "manually
  curated", which only holds for the confirmed subset.

### 5. Cosmetic citation metadata (year/venue conflation)

- Example: in `data/reviews/5_flow_conjecture.json`, Steffen's
  "Intersecting 1-factors and nowhere-zero 5-flows" is listed as
  "2015, Combinatorica" — the arXiv preprint is 2013 (arXiv:1306.5645) and the
  journal publication is 2017. Claims/titles were accurate everywhere checked.
- Fix (low priority): a sweep normalizing `year`/`venue` to either the arXiv
  date or the journal publication consistently; could be scripted against the
  arXiv API for entries with an `arxiv_id`.

### 6. Verify the 15 author-less problems (probably fine)

- 15 entries in `data/problems.json` have empty `authors`. Likely faithful to
  the upstream OPG pages, but worth a one-time check against `cache/op/*.html`
  to confirm it's not a selector miss.

## What was checked and found sound (no action needed)

- 227 problems ↔ 227 reviews, 1:1, unique slugs, no orphans.
- All 461 citations carry URLs, and every cited URL appears in that review's
  `verified_urls`.
- Status↔evidence coherence is perfect: all 19 `solved` have a `proof` citation,
  all 13 `disproved` have a `counterexample`, all 136 `partial` have citations.
- No citation predates its problem's posting; no impossible arXiv IDs.
- The 41 zero-citation reviews (40 `open`, 1 `unclear`) document search effort
  (4–10 queries each).
- Spot-verified as real and correctly interpreted: Goldberg–Seymour
  (Chen–Jing–Zang, JCO 2025), common graphs of arbitrary chromatic number
  (Kráľ–Volec–Wei, Compositio 2025), Ádám's conjecture counterexample
  (Thomassen, JCTB 2023), odd-distance graph χ=∞ (Davies, GAFA 2024, arXiv:2209.15598),
  strong matchings/covers counterexamples (Hollom–Shaw, E-JC v33i2p11),
  Welsh's flow-roots disproof (Jacobsen–Salas), fractional-powers counterexample
  (Hartke–Liu–Petříčková), plus 10 partial/open citations (CDC, Caccetta–Häggkvist,
  5-flow, three-longest-paths, Gyárfás–Sumner, Barnette) — all 10/10 OK.
