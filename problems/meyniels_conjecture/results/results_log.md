# Attempt to disprove Meyniel's conjecture: computational log

All cop numbers below were computed exactly with `copwin2` (retrograde analysis over multiset cop
configurations with staged one-cop-at-a-time propagation; standard rules, cops move first after
placement; results identical under robber-moves-first). Sources: `cr_common.h`, `copwin2.c`, `climb2.c`.
Validation: C4=2, C5=2, P5=1, K5=1, Petersen=3, Heawood=3, dodecahedron=3, 4x4 grid=2, Robertson=4
(3 cops lose, 4 win), all matching the literature.

Question attacked: does any graph have c(G) > sqrt(n)?  (Meyniel: c(G) = O(sqrt n); every known
extremal family has c <= sqrt(n); a graph with c > sqrt(n) would be the first step of any disproof.)
For girth >= 5 graphs c >= delta (Aigner-Fromme) but the Moore bound gives delta <= sqrt(n-1), so the
only way to exceed sqrt(n) is c > delta.  In EVERY case below c = delta (girth-5 cases) or c = known value.

| graph | n | delta | girth | c(G) | c/sqrt(n) | note |
|---|---|---|---|---|---|---|
| C4 | 4 | 2 | 4 | 2 | 1.000 | only known equality case |
| Petersen (3,5)-cage | 10 | 3 | 5 | 3 | 0.949 | Moore graph |
| Robertson (4,5)-cage | 19 | 4 | 5 | 4 | 0.918 | gamma = 5, c = 4 |
| all 4-regular girth-5 graphs, n=20 (2), 21 (8), 22 (131), 23 (3917), 24 (123859) | 20-24 | 4 | 5 | 4 (all) | <= 0.894 | exhaustive via geng; every one is a 2-move cop win |
| all girth-5 graphs with min degree >= 4 on 20 and 21 vertices (2 and 11 graphs) | 20-21 | 4 | 5 | 4 (all) | <= 0.894 | on 21 vertices: 8 regular + 3 with a degree-5 vertex |
| Robertson-Wegner (5,5)-cage | 30 | 5 | 5 | 5 | 0.913 | gamma = 7; = HS minus two disjoint Petersens |
| Foster cage (5,5) | 30 | 5 | 5 | 5 | 0.913 | |
| Meringer graph (5,5) | 30 | 5 | 5 | 5 | 0.913 | |
| Wong graph (5,5) | 30 | 5 | 5 | 5 | 0.913 | has a perfect dominating 5-set |
| Wells graph (5-reg, girth 5, DRG {5,4,1,1;1,1,4,5}) | 32 | 5 | 5 | 5 | 0.884 | |
| HS minus N[u] u N[v], u~v | 36 | 5 | 5 | 5 | 0.833 | |
| (6,5)-cage (O'Keefe-Wong) = HS minus a Petersen | 40 | 6 | 5 | 6 | 0.949 | gamma = 8, c = 6 |
| HS minus N[v] | 42 | 6 | 5 | 6 | 0.926 | perfect dominating 6-set |
| Hoffman-Singleton (7,5)-cage | 50 | 7 | 5 | 7 | 0.990 | c<=gamma<=|N(v)|=7 (Moore graph) |
| Heawood = PG(2,2) incidence | 14 | 3 | 6 | 3 | 0.802 | |
| PG(2,4) incidence | 42 | 5 | 6 | 5 | 0.772 | |
| Clebsch | 16 | 5 | 4 | 3 | 0.750 | |
| polarity graphs ER_3, ER_4, ER_5 | 13,21,31 | q | 3 | 3,3,3 | <=0.83 | diameter 2 |
| Kneser K(7,3) = odd graph O_4 | 35 | 4 | 6 | 4 | 0.676 | |
| McGee (3,7)-cage, Coxeter, Tutte-Coxeter (3,8)-cage, Gray, Nauru, Dyck, F26A, Moebius-Kantor, Pappus, Desargues, dodecahedron | 16-54 | 3 | 5-8 | 3 (all) | <=0.75 | c never exceeds delta=3 |

Structural facts found on the way:
* Hoffman-Singleton has exactly 525 induced Petersen subgraphs; every vertex outside a Petersen P has
  exactly one neighbour in P, so HS - P is always the (6,5)-cage (|Aut| = 480) and HS - (P u P') for
  disjoint P, P' is always the Robertson-Wegner graph (|Aut| = 20; 12600 pairs, one isomorphism type).
  No Petersen subgraph avoids a closed neighbourhood N[v].
* Simulated annealing over graphs on 20-22 vertices (objective: robber territory against 3 cops, then
  capture time / number of winning placements against 4 cops) never left the 4-cop-win regime; the
  4-regular girth-5 graphs are strict local maxima under single edge flips.

## Solver validation (independent statistics)
* connected cop-win graphs on n=5..9 vertices: 16, 68, 403, 3791, 65561 (matches the known sequence);
  no connected graph on <= 9 vertices has cop number 3 (Baird et al. Theorem 2.1); all 261080 connected
  9-vertex graphs checked.
* The two-move winning placements reported by the solver were re-verified by a separate brute-force
  Python check (`place_test.g6`): e.g. Robertson graph, cops {0,0,0,1}: every robber start is captured
  within two cop moves.  Same for Meringer {0,0,0,2,2}, Foster {0,0,1,2,2}, Robertson-Wegner {0,1,1,2,2},
  Wells {0,0,0,0,2}.  Mechanism: cops stacked on one or two vertices "fan out" so that after one move the
  closed neighbourhood of the robber is dominated -- this is why c = delta on every near-Moore girth-5 graph.

## Files
* cr_common.h, copwin2.c (exact k-cop solver, OpenMP; graph6 in, n<=62), climb2.c (annealing search)
* hs.g6 (Hoffman-Singleton), cages55_all.g6 (four (5,5)-cages, named), cages65_HS.g6 ((6,5)-cage),
  wells.g6, hs_minus_nv.g6, hs_minus_edge_nbhd.g6, pg24.g6, g19_45.g6..g23_45.g6 (all 4-regular
  girth-5 graphs on 19..23 vertices), 30_5_5.asc (Meringer's data), find_petersens.py, hs_cages.py, wells.py
