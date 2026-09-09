# Exact computations

## Solver (`scripts/copwin2.c`, `scripts/cr_common.h`)

Decides whether $k$ cops win on a graph given in graph6 ($n\le62$). Cop configurations are
multisets ranked in the combinatorial number system ($\binom{n+k-1}{k}$ of them). States
$\mathrm{CT}(C,r)$ (cops to move) and $\mathrm{RT}(C,r)$ (robber to move) are solved by retrograde
analysis in rounds with counters on robber states; predecessors of a newly winning robber state are
marked one cop at a time through intermediate (unmoved multiset, moved multiset, robber) states, in
the spirit of Petr–Portier–Versteegen, which replaces the factor $(\Delta+1)^k$ by about
$k(\Delta+1)$ per intermediate state. The round at which some placement $C$ has all
$\mathrm{CT}(C,r)$ winning is the capture time; `-e` stops there. Both conventions (cops or robber
moving first after placement) are reported and agreed in every case.

Build and use:
```
gcc -O3 -march=native -fopenmp -o copwin2 copwin2.c
./copwin2 k -e < graphs.g6          # do k cops win?  (one graph6 per line)
./copwin2 -c K -e < graphs.g6       # cop number, trying k = 1..K
```

**Validation.** $C_4=2$, $C_5=2$, $P_5=1$, $K_5=1$, Petersen 3, Heawood 3, dodecahedron 3,
$4\times4$ grid 2; Robertson graph: 3 cops lose, 4 win. Over all connected graphs on
$5,\dots,9$ vertices the numbers of cop-win graphs are $16,68,403,3791,65561$ (the known values),
and no graph on $\le9$ vertices has cop number 3 (Baird et al. 2014). The two-move winning
placements below were re-verified by an independent brute-force script.

## Results

| graph | $n$ | $\delta$ | girth | $c(G)$ | $c/\sqrt n$ |
|---|---:|---:|---:|---:|---:|
| $C_4$ | 4 | 2 | 4 | 2 | 1.000 |
| Petersen, (3,5)-cage | 10 | 3 | 5 | 3 | 0.949 |
| Robertson, (4,5)-cage (`data/robertson.g6`) | 19 | 4 | 5 | 4 | 0.918 |
| all 4-regular girth-5 graphs on 20, 21, 22, 23, 24 vertices (2, 8, 131, 3917, 123 859 graphs) | 20–24 | 4 | 5 | 4 | ≤ 0.894 |
| all girth-5 graphs with minimum degree ≥ 4 on 20 and 21 vertices (2 and 11 graphs) | 20–21 | 4 | 5 | 4 | ≤ 0.894 |
| the four (5,5)-cages: Robertson–Wegner, Foster, Meringer, Wong (`data/cages55_all.g6`) | 30 | 5 | 5 | 5 | 0.913 |
| Wells graph (`data/wells.g6`) | 32 | 5 | 5 | 5 | 0.884 |
| Hoffman–Singleton minus $N[u]\cup N[v]$, $u\sim v$ (`data/hs_minus_edge_nbhd.g6`) | 36 | 5 | 5 | 5 | 0.833 |
| (6,5)-cage, O'Keefe–Wong (`data/cages65_HS.g6`) | 40 | 6 | 5 | 6 | 0.949 |
| Hoffman–Singleton minus $N[v]$ (`data/hs_minus_nv.g6`) | 42 | 6 | 5 | 6 | 0.926 |
| Hoffman–Singleton, (7,5)-cage (`data/hs.g6`) | 50 | 7 | 5 | 7 | 0.990 |
| Heawood = incidence graph of PG(2,2) | 14 | 3 | 6 | 3 | 0.802 |
| incidence graph of PG(2,4) (`data/pg24.g6`) | 42 | 5 | 6 | 5 | 0.772 |
| Clebsch | 16 | 5 | 4 | 3 | 0.750 |
| polarity graphs $ER_3, ER_4, ER_5$ | 13, 21, 31 | $q$ | 3 | 3, 3, 3 | ≤ 0.832 |
| Kneser $K(7,3)$ | 35 | 4 | 6 | 4 | 0.676 |
| Möbius–Kantor, Pappus, Desargues, Nauru, F26A, Dyck | 16–32 | 3 | 6 | 3 | ≤ 0.750 |
| McGee (3,7)-cage, Coxeter, Tutte–Coxeter (3,8)-cage, Gray (`data/cubic_named.g6`) | 24–54 | 3 | 7–8 | 3 | ≤ 0.612 |

For Hoffman–Singleton the value follows from $\delta\le c\le\gamma\le|N(v)|=7$ (in a Moore graph of
diameter 2 the neighbourhood of any vertex is dominating); every other value was computed.
In every girth-5 row $c=\delta$. Domination numbers: Robertson 5, Robertson–Wegner 7, (6,5)-cage 8.

## Fan-out placements (two-move wins)

Vertex labels refer to the graph6 files in `data/`. Robertson $\{0,0,0,1\}$; Meringer
$\{0,0,0,2,2\}$; Foster $\{0,0,1,2,2\}$; Robertson–Wegner $\{0,1,1,2,2\}$; Wells $\{0,0,0,0,2\}$;
(6,5)-cage $\{0,0,0,0,0,1\}$. From each placement every robber start is captured within two cop
moves: the stacked cops spread so that the robber's closed neighbourhood becomes dominated. The Wong
graph and Hoffman–Singleton minus $N[v]$ have perfect dominating sets of size $\delta$ (one-move wins).

## Reproducing the enumerations (not committed)

```
geng -q -d4 -D4 -t -f 20      # 4-regular, triangle-free, C4-free  => 4-regular girth >= 5
geng -q -d4 -D4 -t -f 23 r/48 # split over 48 parts; n=24 took ~2 h on 32 cores (123 859 graphs)
geng -q -d4 -t -f 21 r/8      # minimum degree 4, no maximum-degree bound (slow: ~1.3 h for n=20)
./copwin2 4 -e < graphs.g6 | awk '{print $3,$4}' | sort | uniq -c
```
Tallies are in `results/`. The four (5,5)-cages were taken from Meringer's data file
`30_5_5.asc` and identified by automorphism group order (20, 30, 96, 120). The Wells graph was built
as an antipodal double cover of the Clebsch graph with a GF(2) edge signing in which every 4-cycle has
odd sign sum (`scripts/wells.py`; verified intersection array $\{5,4,1,1;1,1,4,5\}$, $|\mathrm{Aut}|=1920$).
Hoffman–Singleton is built from Robertson's pentagon/pentagram description (`scripts/hs_cages.py`);
its 525 induced Petersen subgraphs come from VF2 search (`scripts/find_petersens.py`).
