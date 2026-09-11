"""Construct the Wells graph as an antipodal double cover of the Clebsch graph:
find a GF(2) signing of Clebsch's edges such that every 4-cycle has odd sign sum (so it lifts to an 8-cycle),
build the cover, and check it is 5-regular, girth 5, distance-regular with array {5,4,1,1;1,1,4,5}."""
import networkx as nx, itertools
from networkx.algorithms import isomorphism
C=nx.Graph()
for a in range(16):
    for b in range(16):
        d=bin(a^b).count('1')
        if d in (1,4): C.add_edge(a,b)
edges=list(C.edges()); eidx={frozenset(e):i for i,e in enumerate(edges)}
# 4-cycles: for each pair at distance 2 with common nbrs x,y: cycle u-x-w-y-u
cycles=set()
for u,w in itertools.combinations(C.nodes(),2):
    if C.has_edge(u,w): continue
    cn=list(set(C[u])&set(C[w]))
    if len(cn)==2:
        x,y=cn; cycles.add(frozenset([eidx[frozenset((u,x))],eidx[frozenset((x,w))],eidx[frozenset((w,y))],eidx[frozenset((y,u))]]))
cycles=list(cycles); print("edges",len(edges),"4-cycles",len(cycles))
# solve linear system over GF(2): for each cycle, sum of edge vars = 1
m=len(cycles); nvar=len(edges)
rows=[]
for cyc in cycles:
    r=0
    for e in cyc: r|=1<<e
    rows.append((r,1))
# gaussian elimination
pivots={}
for r,b in rows:
    for col in range(nvar):
        if not (r>>col&1): continue
        if col in pivots:
            pr,pb=pivots[col]; r^=pr; b^=pb
        else:
            pivots[col]=(r,b); break
    else:
        if b==1: print("INCONSISTENT"); raise SystemExit
print("rank",len(pivots),"free vars",nvar-len(pivots))
# back-substitute for one particular solution (free vars = 0)
sol=[0]*nvar
for col in sorted(pivots,reverse=True):
    r,b=pivots[col]; val=b
    for c2 in range(col+1,nvar):
        if r>>c2&1: val^=sol[c2]
    sol[col]=val
# build cover
W=nx.Graph()
for (u,v),s in zip(edges,sol):
    for eps in (0,1):
        W.add_edge((u,eps),(v,eps^s))
W=nx.convert_node_labels_to_integers(W)
print("cover: n=",W.number_of_nodes(),"deg=",set(d for _,d in W.degree()),"girth=",nx.girth(W),"diam=",nx.diameter(W),"connected=",nx.is_connected(W))
# distance-regular check
def intersection_array(G):
    d=nx.diameter(G); arr=None
    for v in G:
        dist=nx.single_source_shortest_path_length(G,v)
        bs=[];cs=[]
        for i in range(d+1):
            layer=[u for u in G if dist[u]==i]
            b=set(); c=set()
            for u in layer:
                b.add(sum(1 for w in G[u] if dist[w]==i+1)); c.add(sum(1 for w in G[u] if dist[w]==i-1))
            if len(b)>1 or len(c)>1: return None
            bs.append(b.pop()); cs.append(c.pop())
        a=(bs[:-1],cs[1:])
        if arr is None: arr=a
        elif arr!=a: return None
    return arr
print("intersection array:",intersection_array(W))
GM=isomorphism.GraphMatcher(W,W); aut=sum(1 for _ in GM.isomorphisms_iter()); print("|Aut|=",aut)
open('wells.g6','w').write(nx.to_graph6_bytes(W,header=False).decode().strip()+'\n')
