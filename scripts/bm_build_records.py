#!/usr/bin/env python3
"""
scripts/bm_build_records.py — write data/bondy_murty_conjectures.json.

The 38 records below are the items of Bondy–Murty *Graph Theory*, Appendix A
("Unsolved Problems", 100 items) that BONDY_MURTY_APPENDIX_A.md found either
missing from the OPG + arXiv corpora (coverage = "missing", 32 items) or only
weakly covered by another record (coverage = "weak", 6 items). Statements are
English renderings of the 2025 French edition (F. Havet) checked against the
2008 English edition where the two differ; see `notes` on individual items.

The source block (book page, PDF page, URLs) is derived from the appendix
number so it cannot drift; arXiv `related` ids are resolved against
data/arxiv_conjectures.json so they match the ids scraper/build.py assigns.

Usage:
    python scripts/bm_build_records.py            # rewrites data/bondy_murty_conjectures.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
OUT = PROJECT / "data" / "bondy_murty_conjectures.json"
ARXIV = PROJECT / "data" / "arxiv_conjectures.json"

HAL_URL = "https://inria.hal.science/hal-05211979v1"
HAL_PDF = "https://inria.hal.science/hal-05211979v1/file/master.pdf"
BOOK_TITLE = ("Théorie des graphes (J.A. Bondy, U.S.R. Murty; French edition by "
              "Frédéric Havet, 2025), Appendix A « Problèmes ouverts »")
ENGLISH_ED = "J.A. Bondy, U.S.R. Murty, Graph Theory, GTM 244, Springer 2008, Appendix A"
PDF_OFFSET = 16  # PDF page = book page + 16

# Book page on which each appendix item is printed (from the PDF text layout).
PAGE_BREAKS = [(6, 626), (18, 627), (25, 628), (37, 629), (51, 630),
               (61, 631), (73, 632), (88, 633), (100, 634)]

SECTIONS = [
    (4,   "Reconstruction"),
    (7,   "Subgraphs"),
    (18,  "Covers, decompositions and packings"),
    (22,  "Complexity"),
    (25,  "Connectivity"),
    (32,  "Embeddings"),
    (36,  "Extremal problems"),
    (40,  "Ramsey numbers"),
    (52,  "Vertex colouring"),
    (54,  "Colouring graphs embedded in surfaces"),
    (55,  "Matchings"),
    (61,  "Edge colouring"),
    (67,  "Paths and cycles in graphs"),
    (77,  "Paths and cycles in digraphs"),
    (91,  "Hamilton paths and cycles"),
    (93,  "Covers and packings in digraphs"),
    (97,  "Integer flows"),
    (100, "Hypergraphs"),
]


def book_page(n: int) -> int:
    for upto, page in PAGE_BREAKS:
        if n <= upto:
            return page
    raise ValueError(n)


def section(n: int) -> str:
    for upto, name in SECTIONS:
        if n <= upto:
            return name
    raise ValueError(n)


def arxiv_review_id(arxiv_id: str, title: str) -> str:
    """<safe_id>__<NN> exactly as scraper/build.py assigns it (paper-local index)."""
    states = json.loads(ARXIV.read_text(encoding="utf-8"))
    idx = 0
    for s in states:
        sid = s.get("safe_id") or s.get("arxiv_id", "").replace("/", "_")
        if sid != arxiv_id.replace("/", "_"):
            continue
        if s.get("title") == title:
            return f"{sid}__{idx:02d}"
        idx += 1
    raise KeyError(f"{arxiv_id} / {title!r} not found in {ARXIV}")


def opg(slug: str, note: str) -> dict:
    return {"corpus": "opg", "slug": slug, "note": note}


def arx(arxiv_id: str, title: str, note: str) -> dict:
    return {"corpus": "arxiv", "id": arxiv_review_id(arxiv_id, title), "arxiv_id": arxiv_id, "note": note}


def ep(number: int, note: str) -> dict:
    return {"corpus": "erdosproblems", "id": str(number), "note": note}


R: list[dict] = []


def add(n: int, title: str, statement: str, attributed_to: str, year: int | None,
        coverage: str, *, kind: str = "Conjecture", context: str = "",
        book_refs: list[str] | None = None, related: list[dict] | None = None,
        notes: str = "") -> None:
    R.append({
        "bm_id":           f"bm-{n:03d}",
        "appendix_number": n,
        "section":         section(n),
        "title":           title,
        "kind":            kind,
        "statement_text":  statement,
        "context_text":    context,
        "attributed_to":   attributed_to,
        "attributed_year": year,
        "book_refs":       book_refs or [],
        "coverage":        coverage,
        "related":         related or [],
        "notes":           notes,
        "source": {
            "title":           BOOK_TITLE,
            "url":             HAL_URL,
            "pdf_url":         HAL_PDF,
            "book_page":       book_page(n),
            "pdf_page":        book_page(n) + PDF_OFFSET,
            "english_edition": ENGLISH_ED,
        },
    })


# ── Reconstruction ─────────────────────────────────────────────────────────────
add(3, "Halin's conjecture on hypomorphic infinite graphs",
    "If two infinite graphs are hypomorphic, then each is isomorphic to a subgraph of the other.",
    "R. Halin", 1970, "missing",
    context=("Two graphs $G$ and $H$ are hypomorphic if there is a bijection $\\varphi\\colon V(G)\\to V(H)$ "
             "with $G - v \\cong H - \\varphi(v)$ for every vertex $v$. For finite graphs the Reconstruction "
             "Conjecture asserts that hypomorphic graphs are isomorphic; this fails for infinite graphs, and "
             "Halin's conjecture is the natural weakening."),
    book_refs=["Exercise 4.2.10"],
    related=[opg("reconstruction_conjecture", "finite analogue")],
    notes=("Bowler, Erde, Heinig, Lehner and Pitz, 'A counterexample to the reconstruction conjecture for "
           "locally finite trees' (Bull. London Math. Soc. 49, 2017), state that their construction also "
           "answers a question of Halin; the status review should check whether it is this one."))

# ── Covers, decompositions and packings ────────────────────────────────────────
add(11, "Barát–Thomassen conjecture",
    "For every tree $T$ there exists a natural number $k := k(T)$ such that every simple $k$-edge-connected "
    "graph whose number of edges is divisible by $e(T)$ admits a decomposition into copies of $T$.",
    "J. Barát and C. Thomassen", 2006, "missing",
    book_refs=["Exercise 2.4.8", "Exercise 17.4.19"],
    related=[arx("1507.08208", "Conjecture 1.2",
                 "Bensmail, Harutyunyan, Le and Thomassé propose a refinement of this conjecture")],
    notes=("Editorial lead, to be confirmed by the status review: Bensmail, Harutyunyan, Le, Merker and "
           "Thomassé, 'A proof of the Barát–Thomassen conjecture', J. Combin. Theory Ser. B 124 (2017)."))

add(13, "Bondy's small cycle double cover conjecture",
    "Every simple graph on $n$ vertices without cut edges has a cycle double cover consisting of at most "
    "$n - 1$ cycles.",
    "J.A. Bondy", 1990, "missing",
    context=("A cycle double cover is a family of cycles covering every edge exactly twice. This "
             "strengthens the Cycle Double Cover Conjecture (Appendix A, item 12)."),
    book_refs=["Conjecture 3.11"],
    related=[opg("cycle_double_cover_conjecture", "implied by this conjecture")])

add(14, "Five cycle double cover conjecture",
    "Every 2-edge-connected graph has a double cover by at most five even subgraphs.",
    "M. Preissmann", 1981, "weak",
    context=("An even subgraph is a spanning subgraph in which every vertex has even degree, i.e. an "
             "edge-disjoint union of cycles; a double cover uses every edge exactly twice. Also "
             "attributed to Celmins (1984)."),
    book_refs=["Exercise 3.5.3"],
    related=[opg("strong_5_cycle_double_cover_conjecture", "stronger form (prescribed cycle in the cover)"),
             opg("cycle_double_cover_conjecture", "weaker: no bound on the number of even subgraphs"),
             opg("petersen_coloring_conjecture", "implies the 5-cycle double cover conjecture"),
             opg("m_n_cycle_covers", "general (m,n)-cycle cover framework")])

add(16, "Linear arboricity conjecture",
    "Every simple $k$-regular graph has linear arboricity $\\lceil (k+1)/2 \\rceil$.",
    "J. Akiyama, G. Exoo and F. Harary (1981); A.J.W. Hilton (1982)", 1981, "missing",
    context=("The linear arboricity $\\mathrm{la}(G)$ is the least number of linear forests (forests whose "
             "components are paths) whose union is $G$. Equivalently: every simple graph of maximum degree "
             "$\\Delta$ satisfies $\\mathrm{la}(G) \\le \\lceil (\\Delta+1)/2 \\rceil$."),
    book_refs=["Theorem 13.19"],
    related=[arx("2302.13312", "Conjecture 2", "refinement for planar graphs")])

# ── Complexity ─────────────────────────────────────────────────────────────────
add(21, "Finding a second Hamilton cycle in a cubic graph",
    "Is the following problem in $\\mathsf{P}$? Given a cubic graph $G$ and a Hamilton cycle in $G$, "
    "find a second Hamilton cycle in $G$.",
    "M. Chrobak and S. Poljak", 1988, "missing", kind="Problem",
    context=("By Smith's theorem every edge of a cubic graph lies in an even number of Hamilton cycles, so "
             "a second Hamilton cycle always exists; the question is whether one can be found in polynomial "
             "time."),
    book_refs=["Exercise 19.4.1"],
    related=[opg("4_connected_graphs_are_not_uniquely_hamiltonian", "existence question for 4-connected graphs"),
             opg("uniquely_hamiltonian_graphs", "existence of a second Hamilton cycle in regular graphs")])

add(22, "Internally disjoint odd paths: is it in co-NP?",
    "Is the following problem in $\\mathsf{co\\text{-}NP}$? Given a graph $G$ and two $k$-subsets $X$ and "
    "$Y$ of $V(G)$, decide whether there exist $k$ internally disjoint $(X,Y)$-paths of odd length in $G$.",
    "C. Thomassen", 1980, "missing", kind="Problem")

# ── Connectivity ───────────────────────────────────────────────────────────────
add(25, "Thomassen's spanning k-connected bipartite subgraph conjecture",
    "Every $2k$-connected graph contains a spanning $k$-connected bipartite subgraph.",
    "C. Thomassen", 1989, "missing",
    context=("Thomassen (1989) asked more generally whether there is a function $f$ such that every "
             "$f(k)$-connected graph has a spanning $k$-connected bipartite subgraph; the book states the "
             "conjecture with $f(k) = 2k$."),
    notes=("Translation caveat: the French edition prints « Tout graphe orienté 2k-connexe contient un "
           "sous-graphe orienté simple k-connexe couvrant » (digraph / oriented subgraph). Thomassen's 1989 "
           "question, as cited in the literature (Delcourt–Ferber 2015), concerns spanning bipartite "
           "subgraphs of undirected graphs; the statement above follows that reading. The status review "
           "should confirm against the English edition."))

# ── Embeddings ─────────────────────────────────────────────────────────────────
add(26, "Orientable five cycle double cover conjecture",
    "Every 2-edge-connected graph has an orientable double cover by five even subgraphs.",
    "D. Archdeacon (1984); F. Jaeger (1988)", 1984, "weak",
    context=("A double cover by even subgraphs is orientable if each even subgraph can be oriented so that "
             "every edge of the graph is traversed once in each direction. Strengthens both the five cycle "
             "double cover conjecture (item 14) and the orientable cycle double cover conjecture."),
    book_refs=["Conjecture 22.14"],
    related=[opg("the_circular_embedding_conjecture", "its discussion lists this as a consequence of the strong form"),
             opg("cycle_double_cover_conjecture", "weaker"),
             opg("grunbaums_conjecture", "compared with the orientable cycle double cover conjecture"),
             opg("three_4_flows_conjecture", "implies the orientable 4-cover conjecture")])

add(29, "Kelmans–Seymour conjecture",
    "Every 5-connected non-planar graph contains a subdivision of $K_5$.",
    "P.D. Seymour (1974); A.K. Kelmans (1979)", 1974, "missing",
    book_refs=["Exercise 10.5.14"],
    notes=("Editorial lead, to be confirmed by the status review: He, Wang and Yu, 'The Kelmans–Seymour "
           "conjecture I–IV', J. Combin. Theory Ser. B 144 (2020)."))

add(31, "Conway's thrackle conjecture",
    "No graph with more edges than vertices has a thrackle drawing.",
    "J.H. Conway", 1968, "missing",
    context=("A thrackle is a drawing of a graph in the plane in which every pair of edges meets exactly "
             "once, either at a common endpoint or at a proper crossing. French: « plongement en manoque »."),
    book_refs=["Exercise 10.1.11"])

add(32, "Harborth's conjecture (integral straight-line drawings)",
    "Every simple planar graph admits a straight-line planar embedding in which every edge has integer length.",
    "A. Kemnitz and H. Harborth", 2001, "missing")

# ── Extremal problems ──────────────────────────────────────────────────────────
add(33, "Erdős–Sós conjecture",
    "If $G$ is a simple graph on $n$ vertices with $m > n(k-1)/2$ edges, then $G$ contains every tree "
    "with $k$ edges.",
    "P. Erdős and V.T. Sós", 1963, "missing",
    book_refs=["Exercise 4.1.9"])

add(34, "Even-cycle Turán number",
    "For every $k \\ge 2$ there is a positive constant $c$ such that $\\mathrm{ex}(n, C_{2k}) \\ge c\\, n^{1+1/k}$.",
    "P. Erdős", 1971, "missing",
    context=("$\\mathrm{ex}(n, C_{2k})$ is the maximum number of edges of a simple graph on $n$ vertices "
             "with no cycle of length $2k$; the Bondy–Simonovits theorem gives the matching upper bound "
             "$O(n^{1+1/k})$. Known for $k = 2, 3, 5$."),
    book_refs=["Exercise 12.2.14"],
    related=[opg("turan_number_of_a_finite_family", "discusses the even-cycle case"),
             ep(572, "same statement")])

# ── Ramsey numbers ─────────────────────────────────────────────────────────────
add(37, "Constructive exponential lower bound for diagonal Ramsey numbers",
    "Give a constructive proof that $r(k,k) \\ge c^k$ for some constant $c > 1$ and all $k \\ge 1$.",
    "P. Erdős", 1969, "missing", kind="Problem",
    context="Erdős's 1947 probabilistic argument gives $r(k,k) \\ge 2^{k/2}$ non-constructively.",
    book_refs=["Theorem 12.12"],
    related=[ep(78, "same problem")])

add(38, "Limit of $r(k,k)^{1/k}$",
    "Does $\\lim_{k\\to\\infty} r(k,k)^{1/k}$ exist? If so, determine its value.",
    "P. Erdős", 1947, "missing", kind="Problem",
    related=[ep(77, "same problem")])

add(39, "Burr–Erdős tree Ramsey conjecture",
    "For every tree $T$ on $n$ vertices, $r(T,T) \\le 2n - 2$.",
    "S.A. Burr and P. Erdős", 1976, "missing",
    related=[ep(547, "same statement")])

# ── Vertex colouring ───────────────────────────────────────────────────────────
add(41, "Hadwiger's conjecture",
    "Every $k$-chromatic graph has a $K_k$-minor.",
    "H. Hadwiger", 1943, "missing",
    context=("Known for $k \\le 6$: the case $k = 5$ is equivalent to the Four Colour Theorem (Wagner 1937) "
             "and $k = 6$ was settled by Robertson, Seymour and Thomas (1993)."),
    book_refs=["Conjecture 16.11"],
    related=[opg("list_hadwiger_conjecture", "list-colouring variant"),
             opg("fractional_hadwiger", "fractional variant"),
             opg("seagull_problem", "an unproved consequence"),
             opg("coloring_and_immersion", "immersion analogue"),
             opg("jorgensens_conjecture", "structure of $K_6$-minor-free graphs")],
    notes="Open Problem Garden itself has no page for this conjecture; only the list and fractional variants.")

add(42, "Hajós conjecture for $k = 5$ and $k = 6$",
    "Does every $k$-chromatic graph contain a subdivision of $K_k$ when $k = 5$ and when $k = 6$?",
    "G. Hajós; P.A. Catlin", 1979, "missing", kind="Problem",
    context=("Hajós conjectured this for all $k$; it holds for $k \\le 4$ (Dirac 1952) and Catlin (1979) "
             "disproved it for every $k \\ge 7$."),
    book_refs=["Exercise 16.4.3"],
    related=[opg("coloring_and_immersion", "immersion analogue of Hajós' conjecture")])

add(45, "Erdős–Lovász Tihany conjecture",
    "Let $G$ be a $k$-chromatic graph containing no $k$-clique, and let $k + 1 = k_1 + k_2$ with "
    "$k_1, k_2 \\ge 2$. Then $G$ has vertex-disjoint subgraphs $G_1$ and $G_2$ such that $G_i$ is "
    "$k_i$-chromatic, $i = 1, 2$.",
    "L. Lovász", 1968, "missing",
    book_refs=["Exercise 17.3.13"],
    related=[opg("double_critical_graph_conjecture", "the special case $k_1 = 2$")])

add(46, "El-Zahar–Erdős conjecture",
    "Does there exist a function $f$ such that every graph of chromatic number at least $f(r,k)$ contains "
    "either an $r$-clique or an induced subgraph which is the disjoint union of two $k$-chromatic graphs?",
    "M. El-Zahar and P. Erdős", 1985, "missing", kind="Problem")

add(50, "Gyárfás's tree conjecture for triangle-free graphs",
    "Every triangle-free graph of infinite chromatic number contains every finite tree as an induced subgraph.",
    "A. Gyárfás", 1975, "weak",
    context=("Follows from the Gyárfás–Sumner conjecture (Appendix A, item 49): if $T$-free graphs are "
             "$\\chi$-bounded, a triangle-free $T$-free graph has bounded chromatic number."),
    related=[opg("graphs_with_a_forbidden_induced_tree_are_chi_bounded", "Gyárfás–Sumner conjecture, which implies this")])

# ── Colouring graphs embedded in surfaces ──────────────────────────────────────
add(53, "Albertson's toroidal colouring conjecture",
    "Every toroidal graph has three vertices whose deletion leaves a 4-colourable graph.",
    "M.O. Albertson", 1981, "missing",
    book_refs=["Section 16.5"])

add(54, "Chromatic number of the plane (Hadwiger–Nelson problem)",
    "Determine the chromatic number of the unit-distance graph of the plane, i.e. the least number of "
    "colours needed to colour the points of $\\mathbb{R}^2$ so that no two points at distance $1$ receive "
    "the same colour.",
    "E. Nelson", 1950, "missing", kind="Problem",
    context="At the time of the book, $4 \\le \\chi(\\mathbb{R}^2) \\le 7$.",
    book_refs=["Exercise 15.1.20"],
    related=[opg("coloring_the_odd_distance_graph", "odd-distance analogue")],
    notes="Editorial lead, to be confirmed by the status review: de Grey (2018) showed the chromatic number is at least 5.")

# ── Edge colouring ─────────────────────────────────────────────────────────────
add(57, "1-factorization conjecture",
    "Every simple $d$-regular graph on $n$ vertices with $n$ even and $d \\ge n/2$ is $d$-edge-colourable.",
    "A.J.W. Hilton", 1989, "missing",
    context=("Equivalently, such graphs have a 1-factorization. Usually stated (Chetwynd and Hilton 1985) "
             "with the sharper threshold $d \\ge 2\\lceil n/4 \\rceil - 1$."),
    related=[opg("goldbergs_conjecture", "overfull parameter and chromatic index")],
    notes=("Editorial lead, to be confirmed by the status review: Csaba, Kühn, Lo, Osthus and Treglown, "
           "'Proof of the 1-factorization and Hamilton decomposition conjectures', Mem. Amer. Math. Soc. "
           "244 (2016), for sufficiently large $n$."))

add(60, "Vizing's interchange conjecture",
    "Given a proper edge colouring of a graph $G$, a proper edge colouring of $G$ with $\\chi'(G)$ colours "
    "can be obtained by a sequence of colour interchanges on alternating paths or cycles (Kempe changes).",
    "V.G. Vizing", 1965, "missing",
    notes=("Editorial lead, to be confirmed by the status review: Narboni, 'Vizing's edge-recoloring "
           "conjecture holds' (arXiv:2302.12914, 2023); triangle-free case by Bonamy, Defrain, Klimošová, "
           "Lagoutte and Narboni (J. Combin. Theory Ser. B, 2023)."))

# ── Paths and cycles in graphs ─────────────────────────────────────────────────
add(62, "Kotzig's unique $k$-path conjecture",
    "For $k \\ge 3$ there is no graph in which every pair of vertices is connected by a unique path of length $k$.",
    "A. Kotzig", 1979, "missing",
    context="The case $k = 2$ is the Friendship Theorem (Theorem 3.1 in the book).",
    book_refs=["Theorem 3.1"])

add(64, "Smith's conjecture on longest cycles",
    "In a $k$-connected graph, $k \\ge 2$, any two longest cycles have at least $k$ vertices in common.",
    "S. Smith", None, "missing",
    context="Attributed to S. Smith; see Grötschel (1984).",
    book_refs=["Exercise 5.1.5"],
    related=[opg("chords_of_longest_cycles", "longest cycles in 3-connected graphs"),
             opg("do_any_three_longest_paths_in_a_connected_graph_have_a_vertex_in_common", "analogous question for longest paths")])

add(65, "Bondy's linear-length cycle conjecture for cyclically 4-edge-connected cubic graphs",
    "There is a positive constant $c$ such that every 3-connected, cyclically 4-edge-connected cubic graph "
    "on $n$ vertices contains a cycle of length at least $cn$.",
    "J.A. Bondy", None, "missing",
    context="Attributed to J.A. Bondy; see Fleischner and Jackson (1989).")

add(66, "Birmelé's conjecture on long cycles",
    "If any two cycles of length at least $k$ in a graph intersect, then the graph has a set of $k$ vertices "
    "meeting every cycle of length at least $k$.",
    "E. Birmelé", 2003, "missing",
    related=[opg("erdos_posa_property_for_long_directed_cycles", "Erdős–Pósa property for long cycles (directed version)")])

# ── Paths and cycles in digraphs ───────────────────────────────────────────────
add(70, "Weighted Caccetta–Häggkvist conjecture",
    "Let $D$ be a strongly connected digraph with a positive weight function $w$ on its arcs such that "
    "$w^-(v) \\ge 1$ and $w^+(v) \\ge 1$ for every vertex $v$. Then $D$ contains a directed cycle of weight "
    "at least $1$.",
    "B. Bollobás and A.D. Scott", 1996, "weak",
    context=("$w^-(v)$ and $w^+(v)$ denote the total weight of the arcs entering and leaving $v$. Bollobás "
             "and Scott proved the analogous statement for directed paths."),
    book_refs=["Exercise 2.5.9"],
    related=[opg("caccetta_haggkvist_conjecture", "the unweighted case; this statement appears in its discussion")])

# ── Hamilton paths and cycles ──────────────────────────────────────────────────
add(79, "Matthews–Sumner conjecture",
    "Every 4-connected claw-free graph is Hamiltonian.",
    "M.M. Matthews and D.P. Sumner", 1984, "weak",
    context=("Equivalent, via Ryjáček's closure, to Thomassen's conjecture that every 4-connected line graph "
             "is Hamiltonian."),
    book_refs=["Exercise 19.3.16"],
    related=[opg("hamiltonian_cycles_in_line_graphs", "equivalent (Ryjáček 1997)")])

add(80, "Barnette's conjecture on 4-regular 4-polytopes",
    "The graph of every 4-regular 4-polytope (every simple 4-dimensional convex polytope) is Hamiltonian.",
    "D.W. Barnette", None, "missing",
    context="Attributed to D.W. Barnette; see Grünbaum (1970), p. 1145.",
    related=[opg("barnettes_conjecture", "Barnette's better-known conjecture on cubic bipartite planar graphs")])

add(85, "Cantoni's conjecture",
    "Every planar cubic graph with exactly three Hamilton cycles contains a triangle.",
    "R. Cantoni", 1950, "missing",
    context="See also Ninčák (1974) and Tutte (1976).")

add(88, "Thomassen's conjecture on Hamiltonian vertex-transitive graphs",
    "All but finitely many connected vertex-transitive graphs are Hamiltonian.",
    "C. Thomassen", 1976, "weak",
    context=("Only five connected vertex-transitive graphs without a Hamilton cycle are known: $K_2$, the "
             "Petersen graph, the Coxeter graph, and the truncations of the last two."),
    book_refs=["Exercise 19.1.12"],
    related=[opg("hamiltonian_paths_and_cycles_in_vertex_transitive_graphs", "Lovász's Hamilton-path problem; discusses the known exceptions"),
             opg("hamiltonicity_of_cayley_graphs", "special case: Cayley graphs")])

add(89, "Chvátal's toughness conjecture",
    "There exists a positive integer $k$ such that every $k$-tough graph is Hamiltonian.",
    "V. Chvátal", 1973, "missing",
    context=("A graph $G$ is $t$-tough if $|S| \\ge t \\cdot c(G - S)$ for every vertex cut $S$, where "
             "$c(\\cdot)$ counts components. French: « k-endurant »."),
    book_refs=["Exercise 19.1.22"])

add(90, "Hypohamiltonian graphs of minimum degree at least 4",
    "Is there a hypohamiltonian graph of minimum degree at least $4$?",
    "C. Thomassen", 1978, "missing", kind="Problem",
    context="A graph is hypohamiltonian if it is not Hamiltonian but every vertex-deleted subgraph is.",
    book_refs=["Exercise 19.1.16"])

add(91, "Grötschel's conjecture on bipartite hypotraceable graphs",
    "There is no bipartite hypotraceable graph.",
    "M. Grötschel", 1978, "missing",
    context="A graph is hypotraceable if it has no Hamilton path but every vertex-deleted subgraph has one.",
    book_refs=["Exercise 19.1.17"])


def main() -> int:
    R.sort(key=lambda r: r["appendix_number"])
    ids = [r["bm_id"] for r in R]
    assert len(ids) == len(set(ids)) == 38, len(ids)
    OUT.write_text(json.dumps(R, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(R)} records to {OUT.relative_to(PROJECT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
