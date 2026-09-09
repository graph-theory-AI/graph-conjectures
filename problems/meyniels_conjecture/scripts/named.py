import networkx as nx, itertools
def g6(G): return nx.to_graph6_bytes(nx.convert_node_labels_to_integers(G),header=False).decode().strip()
out=[]
# Polarity (Erdos-Renyi) graphs ER_q over GF(q), q prime: points of PG(2,q), x~y iff x.y=0, x!=y
def ER(q):
    pts=[]
    for v in itertools.product(range(q),repeat=3):
        if v==(0,0,0): continue
        # normalize: first nonzero coordinate = 1
        i=next(j for j in range(3) if v[j]!=0)
        if v[i]==1: pts.append(v)
    G=nx.Graph(); G.add_nodes_from(range(len(pts)))
    for a,b in itertools.combinations(range(len(pts)),2):
        if sum(x*y for x,y in zip(pts[a],pts[b]))%q==0: G.add_edge(a,b)
    return G
for q in [2,3,5]:
    G=ER(q); out.append((f"ER_{q}",G))
# ER_4 over GF(4)
GF4_mul=[[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]  # elements 0,1,a,a^2 with a^2=a+1: encode 2=a,3=a+1
GF4_add=[[a^b for b in range(4)] for a in range(4)]
def er4():
    pts=[]
    for v in itertools.product(range(4),repeat=3):
        if v==(0,0,0): continue
        i=next(j for j in range(3) if v[j]!=0)
        if v[i]==1: pts.append(v)
    G=nx.Graph(); G.add_nodes_from(range(len(pts)))
    for a,b in itertools.combinations(range(len(pts)),2):
        s=0
        for x,y in zip(pts[a],pts[b]): s=GF4_add[s][GF4_mul[x][y]]
        if s==0: G.add_edge(a,b)
    return G
out.append(("ER_4",er4()))
# Odd graph O_4 = Kneser(7,3)
out.append(("O4_Kneser73", nx.kneser_graph(7,3) if hasattr(nx,'kneser_graph') else None))
# Coxeter graph (28), Tutte-Coxeter (30), Shrikhande (16) via networkx if available
for name in ['coxeter_graph','tutte_coxeter_graph','shrikhande_graph','pappus_graph','mcgee_graph']:
    if hasattr(nx,name): out.append((name,getattr(nx,name)()))
# Hoffman-Singleton derived: HS - N[v], HS - v
HS=nx.from_graph6_bytes(open('hs.g6').read().strip().encode())
v=0
out.append(("HS_minus_Nv", HS.subgraph(set(HS)-set(HS[v])-{v}).copy()))
out.append(("HS_minus_v", HS.subgraph(set(HS)-{v}).copy()))
# Kneser(7,3) manually if missing
if out[4][1] is None:
    S=[frozenset(c) for c in itertools.combinations(range(7),3)]
    G=nx.Graph(); G.add_nodes_from(range(len(S)))
    for a,b in itertools.combinations(range(len(S)),2):
        if not (S[a]&S[b]): G.add_edge(a,b)
    out[4]=("O4_Kneser73",G)
with open('named_small.g6','w') as f, open('named_big.g6','w') as fb:
    for name,G in out:
        n=G.number_of_nodes(); degs=sorted(set(d for _,d in G.degree()))
        print(name,'n=',n,'deg=',degs,'girth=',nx.girth(G),'diam=',nx.diameter(G))
        (fb if n>=40 else f).write(g6(G)+' '+name+'\n')
