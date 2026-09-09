"""Build the Hoffman-Singleton graph (Robertson's pentagon/pentagram construction),
extract Petersen subgraphs of the form P_h + Q_j, and output complements of one
Petersen (candidate (6,5)-cage) and of two disjoint Petersens (candidate (5,5)-cages)."""
import networkx as nx, itertools, sys
# Robertson construction: pentagons P_h (h=0..4) vertices (0,h,i), pentagrams Q_j vertices (1,j,i)
# P_h: i ~ i+-1 ; Q_j: i ~ i+-2 ; (0,h,i) ~ (1,j,(h*j+i) mod 5)
G = nx.Graph()
for h in range(5):
    for i in range(5):
        G.add_edge((0,h,i),(0,h,(i+1)%5))
        G.add_edge((1,h,i),(1,h,(i+2)%5))
for h in range(5):
    for j in range(5):
        for i in range(5):
            G.add_edge((0,h,i),(1,j,(h*j+i)%5))
assert G.number_of_nodes()==50 and all(d==7 for _,d in G.degree())
assert nx.girth(G)==5
HS = nx.convert_node_labels_to_integers(G, label_attribute='orig')
lab = {HS.nodes[v]['orig']:v for v in HS}
def pet(h,j):
    return set(lab[(0,h,i)] for i in range(5)) | set(lab[(1,j,i)] for i in range(5))
# check P_h+Q_j is Petersen
P = HS.subgraph(pet(0,0)); assert nx.is_isomorphic(P, nx.petersen_graph())
def g6(H):
    return nx.to_graph6_bytes(nx.convert_node_labels_to_integers(H), header=False).decode().strip()
# (6,5) candidates: HS minus one Petersen
c65 = set()
for h in range(5):
    for j in range(5):
        H = HS.subgraph(set(HS)-pet(h,j)).copy()
        assert all(d==6 for _,d in H.degree()) and nx.girth(H)>=5, (h,j)
        c65.add(g6(H))
print("(6,5) candidates (raw g6, pre-canonical):", len(c65))
with open('cand65.g6','w') as f:
    f.write('\n'.join(sorted(c65))+'\n')
# (5,5) candidates: HS minus two disjoint Petersens P_h+Q_j, P_h'+Q_j' with h!=h', j!=j'
c55 = set()
for h,h2 in itertools.combinations(range(5),2):
    for j in range(5):
        for j2 in range(5):
            if j==j2: continue
            rem = pet(h,j)|pet(h2,j2)
            H = HS.subgraph(set(HS)-rem).copy()
            assert all(d==5 for _,d in H.degree()) and nx.girth(H)>=5
            c55.add(g6(H))
print("(5,5) candidates (raw g6, pre-canonical):", len(c55))
with open('cand55.g6','w') as f:
    f.write('\n'.join(sorted(c55))+'\n')
with open('hs.g6','w') as f:
    f.write(g6(HS)+'\n')
