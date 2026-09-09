# Meyniel's conjecture on the cop number

Self-contained workstream on Meyniel's conjecture, the central open problem of the
Cops and Robbers game, approached from the *disproof* side: what would a counterexample
have to look like, and does any graph at all have cop number above $\sqrt{n}$?

> **Meyniel's conjecture (1985).** There is an absolute constant $C$ such that every
> connected graph $G$ on $n$ vertices has cop number $c(G) \le C\sqrt{n}$.

**Definitions.** In Cops and Robbers, $k$ cops choose vertices, then the robber chooses a
vertex, then the two sides alternate, cops first; each piece moves to a vertex at distance
at most one (staying put is allowed). The cops win if a cop occupies the robber's vertex.
The **cop number** $c(G)$ is the least $k$ for which the cops have a winning strategy;
$c(n)$ is its maximum over connected graphs of order $n$. The conjecture is $c(n)=O(\sqrt n)$.
$M_k$ denotes the minimum order of a connected graph with cop number $k$; the conjecture is
equivalent to $M_k=\Omega(k^2)$ (Baird et al. 2014). A **$(d,g)$-cage** is a $d$-regular
graph of girth $g$ of minimum order; a **Moore graph of girth 5** is a $d$-regular graph
of girth 5 on $d^2+1$ vertices (Petersen, Hoffman–Singleton, $C_5$, possibly one on 3250
vertices). The **domination number** $\gamma(G)$ is the size of a smallest set $D$ with
every vertex in or adjacent to $D$; trivially $c(G)\le\gamma(G)$.

## Goal

Two complementary targets, sharing one exact solver:

- **Disproof target.** Exhibit a family with $c(G)/\sqrt n\to\infty$, or as a first step a
  single graph with $c(G)>\sqrt n$ (none is known; equality $c(G)^2=n$ holds for $C_4$ only).
- **Barrier target.** Make precise why the standard lower-bound arguments cannot do this,
  and test the dense girth-5 graphs where an excess of $c$ over the local bound would be
  easiest to detect.

## Status

- **OPEN.** Meyniel's conjecture, and even the soft form $c(n)=O(n^{1-\varepsilon})$. Best
  general upper bound: $c(n)\le n\,2^{-(1-o(1))\sqrt{\log_2 n}}$ (Lu–Peng 2012; Scott–Sudakov
  2011; Frieze–Krivelevich–Loh 2012). Best lower bound: $c(n)\ge\sqrt{n/2}-n^{0.2625}$ (Prałat,
  via incidence graphs of projective planes; see Baird–Bonato 2012).
- **PROVED (literature).** The conjecture holds for graphs of diameter 2 and bipartite graphs
  of diameter 3 ($c\le 2\sqrt n-1$, Lu–Peng 2012); for $G(n,p)$ and random regular graphs
  (Prałat–Wormald 2016); for abelian Cayley graphs (Bradshaw 2020); for bounded genus. Diameter 3
  gives $c\le n^{4/7+o(1)}$ and diameter 4 gives $c\le n^{3/5+o(1)}$ (Hosseini–Knox–Mohar 2019);
  vertex cover number $k$ gives $c\le k/2^{(1-o(1))\sqrt{\log k}}$ (Bose–Esperet–Hodor–Joret–Micek–Rambaud
  2026). Proving the conjecture for subcubic graphs would give $c(n)=O(n^{3/4+\varepsilon})$, and
  there are subcubic graphs with $c\ge n^{1/2-o(1)}$ (Hosseini–Mohar–González Hermosillo de la Maza).
  $M_3=10$ (Petersen), $M_4=19$ (Robertson graph; Turcotte–Yvon 2021), $M_5\le 30$.
- **PROVED (this workstream; elementary).** Let $b(G)=\max_{u\ne v}|N[u]\cap N(v)|$ (the most
  neighbours of a robber's vertex a single cop can threaten; $b=1$ iff girth $\ge5$).
  *Escape counting:* if $k<\gamma(G)$ and $k\,b(G)<\delta(G)$ then $k$ cops lose, so
  $c(G)\ge\min\{\gamma(G),\lceil\delta/b\rceil\}$ (Aigner–Fromme is the case $b=1$).
  *Cap:* $n\ge 1+\delta^2/b$, hence $\delta/b\le\sqrt{(n-1)/b}\le\sqrt{n-1}$, with equality only
  for Moore graphs of girth 5. Consequently no one-step escape-counting argument can certify
  $c(G)>\sqrt{n-1}$; the Moore bound caps the high-girth bounds of Frankl (1987) and of
  Bradshaw–Hosseini–Mohar–Stacho (2023) by $\sqrt n$ in the same way. Proofs: [docs/barriers.md](docs/barriers.md).
- **Computer-checked (exact solver, validated against published cop-win counts on $\le9$
  vertices and against $M_3=10$, $M_4=19$).** In every girth-5 graph tested the cop number
  equals the minimum degree, so it stays below $\sqrt n$: all four $(5,5)$-cages ($c=5$), the
  $(6,5)$-cage ($c=6$), the Wells graph ($c=5$), Hoffman–Singleton minus a closed neighbourhood
  ($n=42$, $c=6$) and minus two adjacent closed neighbourhoods ($n=36$, $c=5$), and **every**
  4-regular girth-5 graph on $20,\dots,24$ vertices ($2+8+131+3917+123\,859$ graphs, all $c=4$),
  as well as every girth-5 graph of minimum degree $\ge4$ on $20$ and $21$ vertices. Cubic cages
  of girth 7 and 8 have $c=3$. Full table: [docs/computations.md](docs/computations.md).
- **Computer-checked (mechanism).** Every $\delta$-cop win above is a two-move *fan-out*: the
  cops start stacked on one to three vertices and spread in one move so that the robber's
  closed neighbourhood is dominated. The domination number is irrelevant (Robertson–Wegner
  has $\gamma=7$, $c=5$).
- **OPEN (question raised here).** Is there $f$ such that every $\delta$-regular graph of girth 5
  on $n\le\delta^2+1+f(\delta)$ vertices has $c=\delta$? All tested cases (excess up to 7) say yes.
- **Structural byproduct (computer-checked).** The Hoffman–Singleton graph has exactly 525 induced
  Petersen subgraphs; every vertex outside one has exactly one neighbour inside it, so deleting
  any Petersen gives the unique $(6,5)$-cage, and deleting any two disjoint ones gives the
  Robertson–Wegner graph.
- **NEGATIVE (search).** Simulated annealing over graphs on 20–22 vertices never found a graph
  on which 4 cops lose; the 4-regular girth-5 graphs are strict local maxima of robber territory
  under single edge flips.

Assessment: no route to a disproof is visible. Every known lower-bound technique is capped at
$\sqrt n$, and where an excess over the local bound would be easiest to see the excess is zero.
The data are consistent with $c(G)^2\le n$ for all connected $G$, which would follow from the
question of Baird et al. whether the minimum $k$-cop-win graphs are the $(k,5)$-cages.

## Layout

```
docs/barriers.md        the two propositions with full proofs; the Moore-bound cap of high-girth bounds
docs/computations.md    solver description, validation, exact cop numbers, fan-out placements
scripts/copwin2.c, cr_common.h   exact k-cop solver (C, OpenMP; graph6 in, n <= 62)
scripts/*.py            constructions: Hoffman-Singleton and its Petersen subgraphs, Wells graph, polarity graphs
data/*.g6               every hand-constructed graph whose cop number was computed (graph6)
results/                raw computational log and tallies of the exhaustive runs
tests/                  smoke test: builds the solver and checks Petersen = 3, Robertson = 4
```

The regenerable `geng` enumerations are not committed; the exact commands are in
[docs/computations.md](docs/computations.md). A LaTeX write-up with a dated progress log lives in
the companion repository `graph-theory-AI/meyniels-conjecture` (private at the time of writing).

## Start here

1. [docs/barriers.md](docs/barriers.md), for why a disproof needs a non-local idea.
2. [docs/computations.md](docs/computations.md), for what was computed and how to reproduce it.
3. `scripts/copwin2.c`, the solver (`gcc -O3 -march=native -fopenmp -o copwin2 copwin2.c`;
   `./copwin2 -c 6 -e < data/cages55_all.g6` prints the cop numbers of the four (5,5)-cages).

## References

- M. Aigner, M. Fromme, *A game of cops and robbers*, Discrete Appl. Math. 8 (1984).
- W. Baird, A. Bonato, *Meyniel's conjecture on the cop number: a survey*, J. Comb. 3 (2012), arXiv:1308.3385.
- W. Baird et al., *On the minimum order of k-cop-win graphs*, Contrib. Discrete Math. 9 (2014), arXiv:1308.2841.
- P. Bose, L. Esperet, J. Hodor, G. Joret, P. Micek, C. Rambaud, *Cops and robber in graphs with bounded vertex cover number*, arXiv:2602.07435 (2026).
- P. Bradshaw, *A proof of the Meyniel conjecture for abelian Cayley graphs*, Discrete Math. 343 (2020).
- P. Bradshaw, S. A. Hosseini, B. Mohar, L. Stacho, *On the cop number of graphs of high girth*, J. Graph Theory 102 (2023), arXiv:2005.10849.
- P. Frankl, *Cops and robbers in graphs with large girth and Cayley graphs*, Discrete Appl. Math. 17 (1987).
- A. Frieze, M. Krivelevich, P. Loh, *Variations on cops and robbers*, J. Graph Theory 69 (2012).
- S. A. Hosseini, F. Knox, B. Mohar, *Cops and Robbers on graphs of bounded diameter*, arXiv:1912.07203 (2019).
- S. A. Hosseini, B. Mohar, S. González Hermosillo de la Maza, *Meyniel's conjecture on graphs of bounded degree*, J. Graph Theory 97 (2021), arXiv:1912.06957.
- L. Lu, X. Peng, *On Meyniel's conjecture of the cop number*, J. Graph Theory 71 (2012).
- M. Meringer, *Fast generation of regular graphs and construction of cages*, J. Graph Theory 30 (1999); data at <http://www.mathe2.uni-bayreuth.de/markus/reggraphs.html>.
- J. Petr, J. Portier, L. Versteegen, *A faster algorithm for Cops and Robbers*, Discrete Appl. Math. 320 (2022), arXiv:2112.07449.
- P. Prałat, N. Wormald, *Meyniel's conjecture holds for random graphs*, Random Structures Algorithms 48 (2016).
- A. Scott, B. Sudakov, *A bound for the cops and robbers problem*, SIAM J. Discrete Math. 25 (2011).
- J. Turcotte, S. Yvon, *4-cop-win graphs have at least 19 vertices*, Discrete Appl. Math. 301 (2021), arXiv:2006.02998.

Not an Open Problem Garden entry: the OPG graph-theory corpus has no Cops and Robbers page, and
the four arXiv-extracted records in this repository that cite the conjecture (1912.06957,
1912.07203, 2307.15512, 2602.07435) were matched against OPG and manually rejected.
