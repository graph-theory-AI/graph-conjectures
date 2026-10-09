#!/usr/bin/env python3
"""
scripts/sync_openai_math_results.py — write data/openai_math_results.json.

On 6 October 2026 OpenAI released github.com/openai/math: 722 manuscripts in
372 result families, produced by an unreleased internal model and not peer
reviewed. MATCHES below is the hand-checked list of catalogue entries that one
of those manuscripts proves, disproves, or advances. Each match was checked
against the manuscript's TeX source, not only against the catalogue blurb.

This script resolves every listed manuscript against a local checkout of that
repository and adds what can be derived mechanically: the family title, the
PDF link (pinned to the checked commit), and whether OpenAI's Lean scope page
for the family (lean/docs/<family>.md) covers the manuscript.

Model-generated claims stay apart from the literature: scraper/build.py
promotes a matched entry to ai-proved / ai-disproved, never to solved /
disproved, and only when the literature has not already settled it.

Usage:
    git clone https://github.com/openai/math ../openai-math
    python scripts/sync_openai_math_results.py --source-dir ../openai-math
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

from conjecture_names import with_name

PROJECT = Path(__file__).resolve().parent.parent
OUT = PROJECT / "data" / "openai_math_results.json"

REPOSITORY_URL = "https://github.com/openai/math"
RELEASED = "2026-10-06"
CHECKED_AT = "2026-10-07"
MATCHED_BY = "claude-opus-5-5 (manual match against the OpenAI catalogue; TeX sources read)"
DISCLAIMER = (
    "Claims from OpenAI's collection of model-generated manuscripts. They have not "
    "been peer reviewed; Lean formalizations, where listed, are OpenAI's own and "
    "were neither run nor reviewed by this project."
)

# relation: "resolves" — the manuscript proves or disproves this statement;
#           "implies"  — it settles it through the short argument in `derivation`;
#           "partial"  — progress only; the site status is left unchanged.
HADWIGER = "A-counterexample-to-Hadwigers-conjecture-September-23-2026"
LIST_HADWIGER = "A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026"
SIDORENKO = "A-counterexample-to-Sidorenkos-conjecture-September-23-2026"
RYSER = [
    "A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026",
    "Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026",
]
CROSSING_KN = "The-crossing-number-of-complete-graphs-September-23-2026"
CROSSING_KMN = "The-crossing-number-of-complete-bipartite-graphs-September-23-2026"
SECOND_NEIGHBOURHOOD = "A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026"
NOT_IN_LEAN_157 = ("This manuscript lies outside the family's Lean formalization, which "
                   "covers only the companion list-colouring bound.")

MATCHES: list[dict] = [
    # ── Family 157: clique minors ──────────────────────────────────────────────
    {
        "id": "bm-041",
        "family": "157",
        "manuscripts": [HADWIGER],
        "relation": "resolves",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript constructs arbitrarily large graphs on $m$ vertices with "
            "independence number at most 2 and $h(G) < 26m/75 + 2/3 < m/2 \\le \\chi_f(G) "
            "\\le \\chi(G)$, where $h(G)$ is the largest order of a clique minor: each is "
            "$k$-chromatic for some $k$ (necessarily $k \\ge 7$) without a $K_k$ minor."
        ),
        "caveats": NOT_IN_LEAN_157,
    },
    {
        "id": "seagull_problem",
        "family": "157",
        "manuscripts": [HADWIGER],
        "relation": "resolves",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's counterexample to Hadwiger's conjecture consists of $m$-vertex graphs "
            "with no independent set of size 3 whose largest clique minor has fewer than "
            "$26m/75 + 2/3 < m/2$ vertices. The manuscript notes that this is the "
            "Plummer–Stiebitz–Toft form of Hadwiger's conjecture for independence number 2."
        ),
        "caveats": NOT_IN_LEAN_157,
    },
    {
        "id": "1907.12999__00",
        "family": "157",
        "manuscripts": [HADWIGER],
        "relation": "implies",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "Disproved by the graphs of OpenAI's counterexample to Hadwiger's conjecture, "
            "which have independence number at most 2 and no clique minor on half of "
            "their vertices."
        ),
        "derivation": (
            "The manuscript's graphs have $n$ vertices, $\\alpha(G) \\le 2$ and largest "
            "clique minor $h(G) < 26n/75 + 2/3 < n/2$. With $t = h(G)$ the graph has no "
            "$K_{t+1}$ minor, yet the statement would require $\\alpha(G) \\ge n/t > 2$."
        ),
        "caveats": NOT_IN_LEAN_157,
    },
    {
        "id": "fractional_hadwiger",
        "family": "157",
        "manuscripts": [HADWIGER],
        "relation": "partial",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's counterexample to Hadwiger's conjecture disproves part (a): its graphs "
            "satisfy $\\text{had}(G) < m/2 \\le \\chi_f(G)$, and the manuscript says so "
            "explicitly. Parts (b) and (c), which use the fractional Hadwiger number "
            "$\\text{had}_f$, are not addressed."
        ),
        "caveats": NOT_IN_LEAN_157,
    },
    {
        "id": "list_hadwiger_conjecture",
        "family": "157",
        "manuscripts": [LIST_HADWIGER],
        "relation": "resolves",
        "site_status": "ai-proved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves $\\chi_\\ell(G) \\le C\\,h(G)$ for an absolute "
            "constant $C$, where $h(G)$ is the largest order of a clique minor, so every "
            "$K_t$-minor-free graph is $Ct$-list-colourable. The constant is not optimised; "
            "Steiner's examples force $C \\ge 2$."
        ),
    },
    {
        "id": "2110.09403__00",
        "family": "157",
        "manuscripts": [LIST_HADWIGER],
        "relation": "partial",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves the linear bound $\\chi_\\ell(G) \\le C\\,h(G)$, so "
            "$K_t$-minor-free graphs have list chromatic number $O(t)$. Its constant is not "
            "optimised, so the bound $2t$ remains open."
        ),
    },
    {
        "id": "2201.09115__01",
        "family": "157",
        "manuscripts": [LIST_HADWIGER],
        "relation": "partial",
        "match_confidence": "medium",
        "one_line": (
            "OpenAI's linear bound $\\chi_\\ell(G) \\le C\\,h(G)$ gives $\\chi_\\ell(G) \\le "
            "C(s+t-1)$ for $K_{s,t}$-minor-free graphs, linear in $s+t$ even when $s$ and "
            "$t$ are comparable. The constant is not optimised, so the bound $2s+t$ remains "
            "open."
        ),
        "derivation": (
            "$K_{s,t}$ is a subgraph of $K_{s+t}$, so a $K_{s,t}$-minor-free graph has no "
            "$K_{s+t}$ minor, i.e. $h(G) \\le s+t-1$."
        ),
    },
    {
        "id": "2206.13635__00",
        "family": "157",
        "manuscripts": [LIST_HADWIGER],
        "relation": "partial",
        "match_confidence": "medium",
        "one_line": (
            "Combined with the source paper's bound $h(t) \\le 2g(t)$, OpenAI's linear bound "
            "for graphs gives $h(t) = O(t)$; the conjectured value "
            "$\\lceil\\frac32(t-1)\\rceil$ remains open."
        ),
        "derivation": (
            "The source paper proves $h(t) \\le 2g(t)$, where $g(t)$ is the largest "
            "chromatic number of a $K_t$-minor-free graph, and the manuscript's corollary "
            "$\\chi(G) \\le C\\,h(G)$ gives $g(t) \\le C(t-1)$."
        ),
    },
    # ── Family 161: Sidorenko and forcing ──────────────────────────────────────
    {
        "id": "sidorenkos_conjecture",
        "family": "161",
        "manuscripts": [SIDORENKO],
        "relation": "resolves",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript exhibits a connected bipartite graph $H$ with 35 vertices "
            "and 66 edges (the incidence graph of 22 triples on 13 points) and a finite "
            "simple graph $G$ with $t(H,G) < t(K_2,G)^{66}$."
        ),
    },
    {
        "id": "2210.16971__00",
        "family": "161",
        "manuscripts": [SIDORENKO],
        "relation": "implies",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "Disproved via OpenAI's counterexample to Sidorenko's conjecture: the 35-vertex "
            "bipartite graph, oriented from one side to the other, lacks the directed "
            "Sidorenko property."
        ),
        "derivation": (
            "Orient every edge of the manuscript's graph $H$ from its 13 point vertices to "
            "its 22 triple vertices; the result $B$ maps to $\\vec K_2$. By Theorem 1.5 of "
            "the source paper, $B$ has the directed Sidorenko property only if $H$ has the "
            "asymmetric Sidorenko property, which implies the ordinary one, as that paper "
            "notes. $H$ fails the ordinary property."
        ),
    },
    {
        "id": "2210.16971__01",
        "family": "161",
        "manuscripts": [SIDORENKO],
        "relation": "implies",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "Disproved via OpenAI's counterexample to the forcing conjecture: the same "
            "35-vertex bipartite graph, oriented from one side to the other, has a cycle "
            "and a homomorphism to an edge but lacks the directed forcing property."
        ),
        "derivation": (
            "The manuscript's forcing corollary gives $p \\in (0,1)$ and a nonconstant "
            "symmetric graphon $W$ with $t(K_2,W) = p$ and $t(H,W) = p^{66}$. Read as a "
            "bipartite graphon, $W$ shows that $H$, with its point/triple bipartition, lacks "
            "the asymmetric forcing property. By Theorem 1.8 of the source paper, $H$ "
            "oriented from points to triples then lacks the directed forcing property."
        ),
        "caveats": ("The forcing corollary lies outside the family's Lean formalization, "
                    "which covers only the Sidorenko counterexample."),
    },
    # ── Family 162: Ryser ──────────────────────────────────────────────────────
    {
        "id": "rysers_conjecture",
        "family": "162",
        "manuscripts": RYSER,
        "relation": "resolves",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscripts construct, for every sufficiently large prime $q$, "
            "intersecting ($\\nu = 1$) $r$-partite $r$-uniform hypergraphs with $r = q+1$ "
            "and covering number $\\tau = r > (r-1)\\nu$; further ranks $r = p^n + 1$ are "
            "also covered."
        ),
    },
    {
        "id": "2505.05339__02",
        "family": "162",
        "manuscripts": RYSER,
        "relation": "implies",
        "site_status": "ai-disproved",
        "match_confidence": "high",
        "one_line": (
            "Disproved by OpenAI's counterexamples to Ryser's conjecture, which this "
            "statement implies."
        ),
        "derivation": (
            "The manuscripts' hypergraphs are intersecting ($\\nu = 1$), $r$-partite and "
            "$r$-uniform with covering number $r$. With $\\nu = 1$ the statement forces "
            "$k = 1$: $r-1$ vertices whose deletion leaves no edge, i.e. a vertex cover of "
            "size $r-1$, which does not exist."
        ),
    },
    # ── Family 165: crossing numbers ───────────────────────────────────────────
    {
        "id": "the_crossing_number_of_the_complete_graph",
        "family": "165",
        "manuscripts": [CROSSING_KN],
        "relation": "resolves",
        "site_status": "ai-proved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves the Harary–Hill formula $\\mathrm{cr}(K_n) = "
            "\\frac14\\lfloor\\frac n2\\rfloor\\lfloor\\frac{n-1}2\\rfloor\\lfloor\\frac{n-2}2"
            "\\rfloor\\lfloor\\frac{n-3}2\\rfloor$ for every $n$: the classical drawings are "
            "optimal."
        ),
    },
    {
        "id": "the_crossing_number_of_the_complete_bipartite_graph",
        "family": "165",
        "manuscripts": [CROSSING_KMN],
        "relation": "resolves",
        "site_status": "ai-proved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves Zarankiewicz's formula $\\mathrm{cr}(K_{m,n}) = "
            "\\lfloor\\frac m2\\rfloor\\lfloor\\frac{m-1}2\\rfloor\\lfloor\\frac n2\\rfloor"
            "\\lfloor\\frac{n-1}2\\rfloor$ for all positive $m, n$, settling Turán's brick "
            "factory problem."
        ),
    },
    {
        "id": "2009.03418__00",
        "family": "165",
        "manuscripts": [CROSSING_KN],
        "relation": "partial",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves the $t = 0$ case, Hill's formula "
            "$\\mathrm{cr}(K_n) = H(n)$; complete graphs minus a matching are not treated."
        ),
    },
    # ── Family 173: second neighbourhood ───────────────────────────────────────
    {
        "id": "seymours_second_neighbourhood_conjecture",
        "family": "173",
        "manuscripts": [SECOND_NEIGHBOURHOOD],
        "relation": "resolves",
        "site_status": "ai-proved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves that every nonempty finite oriented graph has a "
            "vertex $v$ with $|N^+(v)| \\le |N^{++}(v)|$, where $N^{++}(v)$ is the set of "
            "vertices at directed distance exactly two from $v$."
        ),
    },
    {
        "id": "caccetta_haggkvist_conjecture",
        "family": "173",
        "manuscripts": [SECOND_NEIGHBOURHOOD],
        "relation": "partial",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's proof of Seymour's second-neighbourhood conjecture yields a statement "
            "this page lists as open: every $n$-vertex digraph with minimum outdegree and "
            "minimum indegree at least $n/3$ has a cycle of length at most 3. It also gives "
            "the girth-four case of the Behzad–Chartrand–Wall conjecture: an $r$-regular "
            "digraph with no cycle of length at most 3 has at least $3r+1$ vertices. The case "
            "$r = n/3$ of the conjecture itself, which bounds only the outdegree, remains open."
        ),
        "derivation": (
            "The manuscript derives both statements for oriented graphs in its closing "
            "corollary on directed cycles; a digraph containing a 2-cycle already has a "
            "cycle of length at most 3."
        ),
    },
    # ── Family 158: chromatic number of the plane ──────────────────────────────
    {
        "id": "bm-054",
        "family": "158",
        "manuscripts": ["The-Euclidean-plane-is-not-five-colorable-September-23-2026"],
        "relation": "partial",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves that every 5-colouring of the plane, with no "
            "measurability assumption, has a monochromatic pair of points at distance 1, so "
            "the chromatic number of the plane is 6 or 7."
        ),
    },
    # ── Family 180: Barnette ───────────────────────────────────────────────────
    {
        "id": "barnettes_conjecture",
        "family": "180",
        "manuscripts": ["Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026"],
        "relation": "resolves",
        "site_status": "ai-proved",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves that every finite simple cubic bipartite planar "
            "3-connected graph has a Hamiltonian cycle."
        ),
    },
    # ── Family 181: Erdős–Gallai cycle decomposition ───────────────────────────
    {
        "id": "decomposing_an_eulerian_graph_into_cycles",
        "family": "181",
        "manuscripts": ["A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026"],
        "relation": "partial",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript proves the Erdős–Gallai conjecture that every $n$-vertex "
            "graph splits into $O(n)$ cycles and edges, and deduces that every Eulerian "
            "graph splits into at most $Cn$ cycles. Hajós's bound $\\frac12(n-1)$ is not "
            "reached: $C$ is not determined."
        ),
    },
    # ── Family 190: ordered matrix removal ─────────────────────────────────────
    {
        "id": "1704.02367__01",
        "family": "190",
        "manuscripts": ["Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026"],
        "relation": "partial",
        "match_confidence": "high",
        "one_line": (
            "OpenAI's manuscript, citing this question, constructs a fixed $66\\times66$ "
            "binary matrix for which ordered removal has no polynomial bound, ruling out the "
            "ideal polynomial dependence. It only forces $\\delta^{-1} \\ge "
            "\\exp(\\Omega(\\varepsilon^{-1/2}))$, so exponential dependence remains open."
        ),
    },
]


def _family_index(source_dir: Path) -> dict[str, dict]:
    """Family number -> {title, papers: {preprint dir: {title, path}}} from CONTENTS.md."""
    text = (source_dir / "CONTENTS.md").read_text(encoding="utf-8")
    families: dict[str, dict] = {}
    current = None
    for cell in re.findall(r"<td>\n\n(.*?)\n\n</td>", text, re.S):
        head = re.match(r"\*\*(\d+)\. (.*?)\*\*", cell, re.S)
        if head:
            current = {"title": head.group(2).rstrip("."), "papers": {}}
            families[head.group(1)] = current
            continue
        link = re.match(r"&emsp;\[(.*?)\]\((preprints/([^/]+)/[^)]+\.pdf)\)", cell, re.S)
        if link and current is not None:
            current["papers"][link.group(3)] = {"title": link.group(1).strip(),
                                                "path": link.group(2)}
    return families


def _lean_index(source_dir: Path) -> dict[str, str]:
    """Repo-relative PDF path -> family whose Lean scope page lists it."""
    covered: dict[str, str] = {}
    for doc in sorted((source_dir / "lean" / "docs").glob("*.md")):
        head = doc.read_text(encoding="utf-8").split("## Scope")[0]
        for path in re.findall(r"\]\(\.\./\.\./(preprints/[^)]+\.pdf)\)", head):
            covered[path] = doc.stem
    return covered


def collect(source_dir: Path) -> dict:
    families = _family_index(source_dir)
    lean = _lean_index(source_dir)
    commit = subprocess.run(
        ["git", "-C", str(source_dir), "rev-parse", "HEAD"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()

    results = []
    for match in MATCHES:
        family = families[match["family"]]
        manuscripts = []
        for preprint in match["manuscripts"]:
            paper = family["papers"][preprint]
            manuscripts.append({
                "title": paper["title"],
                "pdf_url": f"{REPOSITORY_URL}/blob/{commit}/{paper['path']}",
                "lean": paper["path"] in lean,
            })
        result = {
            "id": match["id"],
            "relation": match["relation"],
            "site_status": match.get("site_status"),
            "match_confidence": match["match_confidence"],
            "one_line": match["one_line"],
            "family": match["family"],
            "family_title": family["title"],
            "manuscripts": manuscripts,
        }
        if any(m["lean"] for m in manuscripts):
            result["lean_scope_url"] = (
                f"{REPOSITORY_URL}/blob/{commit}/lean/docs/{match['family']}.md"
            )
        for key in ("derivation", "caveats"):
            if match.get(key):
                result[key] = match[key]
        results.append(with_name(result))

    ids = [r["id"] for r in results]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate catalogue ids in MATCHES")
    return {
        "schema_version": 1,
        "source_repository": REPOSITORY_URL,
        "source_commit": commit,
        "released": RELEASED,
        "checked_at": CHECKED_AT,
        "matched_by": MATCHED_BY,
        "disclaimer": DISCLAIMER,
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source-dir", type=Path, default=PROJECT.parent / "openai-math")
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    payload = collect(args.source_dir)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(f"wrote {len(payload['results'])} OpenAI manuscript match(es) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
