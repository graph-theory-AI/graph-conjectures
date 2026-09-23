# Relations between conjectures

`data/relations.json` is a directed relation graph over the full conjecture
corpus: the 227 Open Problem Garden problems (`opg:<slug>`), the 762
arXiv-mined conjectures/problems/questions (`arxiv:<safe_id>__NN`), the 38
Bondy–Murty Appendix A items (`bm:bm-NNN`) and the `others` corpus
(`others:<id>`). It records which conjecture **implies** which, which pairs are
**equivalent**, and which entries are **duplicates** of each other across
corpora.

**190 relations** survived adversarial verification, out of 207 candidates;
4 duplicate pairs were merged in September 2026, leaving 186 edges. An
incremental pass over the Bondy–Murty and `others` corpora then added 40
(see [below](#bondymurty-extension-september-2026)), for 226 edges. One
wrong duplicate (e040, see below) was then removed, leaving **225 edges**:

| relation       | confirmed | plausible | meaning                                            |
|----------------|----------:|----------:|----------------------------------------------------|
| implies        |       155 |         4 | truth of `source` forces truth of `target`         |
| equivalent_to  |         7 |         1 | each implies the other                             |
| same_conjecture|        15 |         1 | same statement appearing in two corpora            |
| related_only   |        37 |         5 | documented connection, but no implication          |

Every edge carries the verified direction, a referee argument precise enough
to check by hand, citations when the confirmation is literature-based, and
provenance (how many independent finder agents proposed it, and whether it
survived the re-attack pass).

**"Verified" means checked by adversarial AI referees** against the full
statements and, where applicable, the literature — it does **not** mean
formally verified. None of the arguments have been machine-checked in a proof
assistant such as Rocq or Lean; they are short informal mathematical arguments
that a human (or a formalization effort) can audit.

## Pipeline

The graph was produced by a four-stage multi-agent pipeline
(working files in `data/relations_work/`):

```
phase 0   build_phase0.py       deterministic merge: 989 nodes, identity merges
                                from the 44 manually confirmed arxiv↔OPG matches,
                                seed edges (49 OPG cross-mentions with quotes,
                                12 unverified fuzzy matches, 148 internal-ref hints)
phase A   18 tagging agents     topic cluster + one-line formal gist + canonical
                                invariant names per statement  → tags.json
phase B   17 finder agents      14 per-cluster (2 lenses each on the two biggest
                                clusters), 1 cross-cluster over the gist table,
                                2 over cross-cluster invariant groups
                                → 335 raw candidates → 176 deduped  → candidates.json
phase C   59 verifier agents    52 refute-by-default referees (4 edges each,
                                web search allowed, direction re-derived from the
                                statements) + 7 re-attack skeptics on the 54
                                confirmations resting on an argument alone
                                → verdicts.json → data/relations.json
```

Design choices that mattered:

- **Refute by default.** Verifiers confirm only on a rigorous short argument
  (hypothesis-class containment, parameter monotonicity, standard duality or
  reduction), an explicit statement in the problem's own discussion, or a
  literature citation. Plausible-sounding sketches that could not be justified
  were killed: 17 of 207 candidates were refuted, 3 more downgraded to
  "no relation".
- **Direction discipline.** "A implies B" edges are the ones where getting the
  direction wrong is worst; verifiers re-derive the direction from the
  statements rather than trusting the finder, and one edge was flipped.
- **Second skeptic pass.** Confirmations backed by argument alone (no citation)
  were re-attacked by fresh agents told to find the hole; all 54 held.

## What the refutations caught

- Two fuzzy arXiv↔OPG matches were false, both riding on the generic label
  "Question 1" (`e205`, `e206` in `data/relations_work/verdicts.json`).
- A name collision between two distinct Grünbaum conjectures (`e195`).
- The folklore "5-flow ⇒ cycle double cover" route misattributes Jamshy–Tarsi:
  their theorem starts from the shortest-cycle-cover conjecture, not the 5-flow
  conjecture (`e169`).
- Aharoni's rainbow generalization of Caccetta–Häggkvist is related to, but not
  the same as, Caccetta–Häggkvist (`e204`).

## Status-propagation audit

Confirmed edges let review statuses flow: if A ⇒ B and A is solved, B is
solved; if B is disproved, so is A. **This audit now runs at build time**
(`status_flag()` in `scraper/relations_layout.py`), so it cannot go stale: every
edge is confronted with the review statuses of its two endpoints, and the
verdict is rendered on the relation page, in the per-problem "Related
conjectures" box, and as a count in the relation page header. Three kinds come
out:

- **to verify** (4 implications) — the source is solved or the target is
  disproved, while the reviews leave the other endpoint unresolved. If the
  implication holds, it settles that endpoint too; but the implication is only
  checked by AI referees, so it is flagged as *to be formally verified or peer
  reviewed* rather than used to change a status. Two are "source solved"
  (e026, e166) and two "target disproved" (e105, e111).
- **inconsistent** (1 edge) — an equivalence or duplicate whose endpoints have
  different resolved statuses, so the edge or one of the reviews is wrong.
- **vacuous** (42 edges) — the implication is logically fine but carries no
  information any more, because its target is already a theorem or its source
  is already disproved. Vacuous edges are drawn faintly on the graph. Seven of
  them appeared at once when the cycle double cover conjecture was proved
  (see below), and three more point into it from Bondy–Murty nodes; most of the rest hang off `jaegers_modular_orientation_conjecture`,
  `circular_flow_numbers_of_r_graphs` and `real_roots_of_the_flow_polynomial`,
  all disproved.

The six edges first flagged inconsistent were re-examined in September 2026:

1. `arxiv:2509.07174__00` (coarse Menger, surface-embedded, **partial**) is the
   same conjecture as `arxiv:2509.08762__00` (coarse Menger, bounded genus,
   **solved**) — one of the two reviews is stale. Still flagged
   **inconsistent**.
2. `arxiv:2306.04710__02` (Δ(1,2,2) hero in {K₁+P⃗₂}-free digraphs, **open**)
   ⇒ `arxiv:2202.13306__00` (Δ(1,2,2) hero in oriented complete multipartite
   graphs, **disproved**) — oriented complete multipartite digraphs are
   {K₁+P⃗₂}-free, so the counterexample would disprove the source conjecture
   too. Now flagged **to verify**.
3. `arxiv:1710.11281__01` (cop number bounded by genus, **solved**) ⇒
   `arxiv:1710.11281__04` (cop number finiteness on bounded surfaces,
   **partial**) — medium confidence (the argument uses Gromov's systolic
   inequality). Now flagged **to verify**.
4. `arxiv:1802.03727__01` (clique or dense bipartite subgraph in high-degree
   graphs, **solved** by the import via Kwan–Sudakov–Tran) ⇒
   `arxiv:1802.03727__00` (separation choosability grows with minimum degree,
   **open**). Now flagged **to verify**.
5. `arxiv:1802.04179__01` (the informal conjecture that 11/3 is not tight for
   {C₄,C₅}-free planar graphs, **solved** via Xu–Zhu's 7/2 bound) was marked
   the same conjecture as `arxiv:1802.04179__00` (determine that constant,
   still open: **partial**, infimum in [3, 7/2]). They are not the same
   statement, so the edge (e040) was **removed**; `__01` keeps its corpus page
   but no longer appears in the relation graph.
6. `arxiv:2510.11311__03` (characterize Eulerian-avoidable digraphs, **open**)
   ⇒ `arxiv:2510.11311__04` (every orientation of C₄ is Eulerian-avoidable,
   **disproved** by the import via Lei–Wang–Xu–Yang). Now flagged
   **to verify**.

The "to verify" edges are not used to change any status: the implications are
AI-checked only, and must be formally verified or peer reviewed first.

The fourth August inconsistency, `arxiv:1802.03727__02` ⇒ `arxiv:1802.03727__03`,
was cleared by the same import, which marked `__03` solved.

Each needs a human glance before the review JSONs are edited.

## The cycle double cover conjecture became a theorem (July 2026)

The largest hub in the graph was resolved. OpenAI announced a proof (GPT-5.6
Sol Ultra, 11 July 2026) that every bridgeless graph has a cycle double cover;
Sang-il Oum's exposition is [arXiv:2607.16356](https://arxiv.org/abs/2607.16356).
Every implication edge at that node points *into* it, so nothing propagates
outward — but seven edges lost their content at once:

| source | edge |
|---|---|
| `opg:m_n_cycle_covers` (the (5,2)-cover conjecture) | `e084` |
| `opg:strong_5_cycle_double_cover_conjecture` | `e086` |
| `opg:the_circular_embedding_conjecture` | `e087` |
| `opg:faithful_cycle_covers` | `e088` |
| `opg:petersen_coloring_conjecture` | `e091` |
| `opg:cycle_double_covers_containing_predefined_2_regular_subgraphs` | `e098` |
| `opg:decomposing_eulerian_graphs` | `e187` |

All seven are kept — the arguments are still correct mathematics, and they are
the reason each of those pages was interesting — but they are now flagged
`vacuous: the target is now a theorem`. The live content of each source page is
whatever it says *beyond* CDC, and the reviewer notes on the seven pages now say
what that is.

The Bondy–Murty extension added three more edges into CDC, all vacuous as
well: Bondy's small CDC conjecture (`bm:bm-013`), the 5-cycle double cover
conjecture (`bm:bm-014`, the same statement as `opg:m_n_cycle_covers`) and the
orientable 5-CDC conjecture (`bm:bm-026`, which also implies `bm:bm-014`).

The orientable 5-CDC conjecture also implies the 5-flow conjecture (Oum,
Section 9.3 and Lemma 22: an orientable k-CDC with directed even subgraphs
C_1..C_k gives the nowhere-zero Z_k-flow Σ i·χ_{C_i}). It is now edge `e246`,
`bm:bm-026` ⇒ `opg:5_flow_conjecture`, confirmed by a referee who read the
paper. One relation from the paper is still missing: the 5-CDC conjecture is
equivalent to its graphic-matroid form (Conjecture 28), but the corpus has no
matroid nodes. The `related_only` verdict on
`cycle_double_cover_conjecture` ↔ `the_berge_fulkerson_conjecture` (`e188`) is
confirmed by the proof: Berge–Fulkerson is untouched by it.

## Bondy–Murty extension (September 2026)

The original pipeline predates the Bondy–Murty corpus, so a smaller
incremental pass connected its 38 items and Meyniel's conjecture (the one
`others` entry) to the existing graph. Provenance is in
`data/relations_work/bm/`:

```
seeds      33 pairs from the Bondy–Murty cross-check notes (`related` field of
           data/bondy_murty_conjectures.json; erdosproblems links skipped)
finders    2 agents over the gist table of tags.json → 9 more candidates
verify     6 refute-by-default referees, 7 candidates each; direction
           re-derived from the statements; no re-attack pass
           → 34 confirmed, 5 plausible, 3 no relation → edges e207–e245
follow-up  1 referee on orientable 5-CDC ⇒ 5-flow (Oum, Lemma 22)
           → confirmed → e246
```

The 3 rejections: the 1-factorization conjecture ↔ Goldberg (no implication
between the simple-graph and multigraph statements), Smith's conjecture ↔
chords of longest cycles, and a name collision between Barnette's conjecture on
4-regular 4-polytopes and his better-known conjecture on cubic bipartite planar
graphs. Unlike the original edges, these 40 were not re-attacked by a second
skeptic, and most rest on an argument alone, with no citation. They are
correspondingly less vetted.

## Duplicate edges merged (September 2026)

Phase B's dedup missed four pairs where two finder agents proposed the same
relation with different wordings; each pair rendered twice in the "Related
conjectures" box. They were merged into the first edge of each pair, unioning
citations and summing finder counts, with the merge recorded in the surviving
edge's `provenance.merged_edge_ids` / `provenance.merge_note`:

| kept | dropped | relation |
|---|---|---|
| `e010` | `e037` | `arxiv:1605.07411__00` ≡ `opg:graphs_with_a_forbidden_induced_tree_are_chi_bounded` |
| `e027` | `e122` | `arxiv:2407.18800__00` ≡ `arxiv:2407.18800__01` |
| `e187` | `e190` | `opg:decomposing_eulerian_graphs` ⇒ `opg:cycle_double_cover_conjecture` |
| `e189` | `e202` | `opg:cycle_double_cover_conjecture` — `opg:three_4_flows_conjecture` (`related_only`, found from both pages) |

## Structure of the graph

Biggest hubs by confirmed implication/equivalence degree: the **cycle double
cover conjecture** (10, now solved — see above), the **5-flow conjecture** (6),
**Gyárfás–Sumner** (5), **Petersen coloring** (5), **Caccetta–Häggkvist** (4),
the majority 3-coloring conjecture for digraphs (4), and the Bondy–Murty
**5-cycle double cover conjecture** (4). No implication 2-cycles
appeared, so there are no hidden equivalences beyond the declared ones.

## Reproducibility and limitations

`data/relations_work/` keeps the pipeline provenance: `build_phase0.py`
(deterministic phase 0; regenerates the node table and batches from the
checked-in data), `tags.json` (phase A output), `candidates.json` (phase B
output incl. finder sketches), `verdicts.json` (all 207 referee verdicts,
including the refutations with reasons). Reviews were generated with Claude
(Sonnet for tagging, Fable for finding/verification) in August 2026. The
Bondy–Murty extension keeps its own provenance in `data/relations_work/bm/`.

Caveats:

- The verification is adversarial AI review, not formal verification: no
  argument has been checked in Rocq, Lean, or any other proof assistant.
- Recall is bounded by the finders: an unproposed edge is an unfound edge.
  Within-cluster coverage is double for the two biggest clusters only.
- The 11 `plausible` edges and 42 `related_only` links are kept but labeled —
  they need literature follow-up before being treated as implications.
- Like the literature reviews, the graph is advisory and should be
  spot-checked before being relied on for research decisions.
