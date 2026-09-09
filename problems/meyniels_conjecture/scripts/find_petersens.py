"""Find all induced Petersen subgraphs of the Hoffman-Singleton graph; build complements of one and
of two disjoint Petersens; output canonical distinct graphs (via labelg later)."""
import networkx as nx, itertools, sys, time
from networkx.algorithms import isomorphism
HS = nx.from_graph6_bytes(open('hs.g6').read().strip().encode())
P = nx.petersen_graph()
t=time.time()
GM = isomorphism.GraphMatcher(HS, P)
pets=set()
for m in GM.subgraph_isomorphisms_iter():   # induced subgraph isomorphisms
    pets.add(frozenset(m.keys()))
print("induced Petersen subgraphs:", len(pets), "time", round(time.time()-t,1), file=sys.stderr)
pets=list(pets)
def g6(H): return nx.to_graph6_bytes(nx.convert_node_labels_to_integers(H), header=False).decode().strip()
out65=set(); bad=0
for S in pets:
    H=HS.subgraph(set(HS)-S)
    if all(d==6 for _,d in H.degree()): out65.add(g6(H))
    else: bad+=1
print("HS - Petersen: 6-regular:", len(out65), "non-regular:", bad, file=sys.stderr)
open('cand65_all.g6','w').write('\n'.join(out65)+'\n')
out55=set(); pairs=0
for A,B in itertools.combinations(pets,2):
    if A & B: continue
    pairs+=1
    H=HS.subgraph(set(HS)-A-B)
    if all(d==5 for _,d in H.degree()): out55.add(g6(H))
print("disjoint pairs:", pairs, "5-regular complements (raw):", len(out55), file=sys.stderr)
open('cand55_all.g6','w').write('\n'.join(out55)+'\n')
