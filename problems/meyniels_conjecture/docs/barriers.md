# Why the standard lower bounds cannot disprove Meyniel's conjecture

Notation: $N(v)$ open and $N[v]=N(v)\cup\{v\}$ closed neighbourhood; $N[C]=\bigcup_{c\in C}N[c]$;
$\delta$ minimum degree, $\gamma$ domination number, $n$ order. Graphs are finite, simple, connected.

**Definition (local blocking number).** For a graph with at least one edge,
$b(G)=\max\{\,|N[u]\cap N(v)| : u\ne v\,\}$.
A cop at $u\ne v$ threatens exactly the vertices of $N[u]\cap N(v)$ among the robber's options
$N(v)$, so $b(G)$ is the largest number of a robber's neighbours one cop can threaten at once.
$b\ge1$ always; $b=1$ iff the graph is triangle-free and $C_4$-free, i.e. has girth $\ge5$. For a
strongly regular graph with parameters $(n,k,\lambda,\mu)$, $b=\max\{\lambda+1,\mu\}$.

## Proposition A (escape counting)

*If $k<\gamma(G)$ and $k\,b(G)<\delta(G)$, then $k$ cops have no winning strategy. Consequently
$c(G)\ge\min\{\gamma(G),\lceil\delta/b\rceil\}$; since $c(G)\le\gamma(G)$ always, either
$c(G)=\gamma(G)$ or $c(G)\ge\lceil\delta/b\rceil$.*

**Proof.** Let the cops place themselves on a multiset $C$ of $k<\gamma$ vertices. $C$ is not
dominating, so some $r\notin N[C]$ exists; the robber starts there. We maintain the invariant

> (I) at the beginning of the cops' turn the robber is at a vertex $r\notin N[C]$.

Suppose (I) holds and the cops move from $C$ to $C'$, each within its closed neighbourhood. A cop at
$c$ reaches $r$ only if $r\in N[c]$, excluded by (I); so $r\notin C'$ and the robber is not captured
during the cops' move. Call $w$ *threatened* if $w\in N[C']$. The threatened neighbours of $r$ are
$\bigcup_{u\in C'}(N[u]\cap N(r))$; each $u\in C'$ differs from $r$, so each set has at most $b$
elements and the union at most $kb<\delta\le|N(r)|$. Hence some $w\in N(r)$ is unthreatened; the
robber moves to $w\notin N[C']$, which is (I) for $C'$. By induction (I) holds forever, and a capture
would need a cop to move onto the robber (excluded by (I)) or the robber to move onto a cop (excluded,
since the robber only moves outside $N[C']\supseteq C'$).

For the consequence let $m=\min\{\gamma,\lceil\delta/b\rceil\}$ and $k<m$. Then $k<\gamma$ and
$k\le\lceil\delta/b\rceil-1<\delta/b$, i.e. $kb<\delta$; so $k$ cops lose and $c(G)\ge m$. Cops on a
dominating set capture in one move, so $c\le\gamma$, and if $c<\gamma$ then $c\ge\lceil\delta/b\rceil$. ∎

For $b=1$ this is the Aigner–Fromme theorem (girth $\ge5$ implies $c\ge\delta$). For the polarity
graphs $ER_q$ ($\delta=q$, $b=2$) it gives $c\ge q/2\approx\sqrt n/2$, matching Bonato–Burgess.

## Proposition B (the cap)

*For every graph with at least one edge, $n\ge 1+\delta^2/b$, hence
$\delta/b\le\sqrt{(n-1)/b}\le\sqrt{n-1}$. Equality $\delta/b=\sqrt{n-1}$ holds iff $b=1$ and
$n=\delta^2+1$, i.e. $G$ is a Moore graph of girth 5.*

**Proof.** If $\delta\le b$ the claims are trivial ($\delta/b\le1\le\sqrt{n-1}$ and
$\delta^2/b\le\delta\le n-1$). Assume $\delta>b$. Fix a vertex $v$ of degree $m\ge\delta$ and let
$L_2$ be the set of vertices at distance exactly 2 from $v$; then $n\ge1+m+|L_2|$.

Each $u\in N(v)$ has at least $\delta$ neighbours: $v$, at most $b-1$ inside $N(v)$ (because
$N[u]\cap N(v)=\{u\}\cup(N(u)\cap N(v))$ has at most $b$ elements), and the rest in $L_2$. So $u$ sends
at least $\delta-b$ edges to $L_2$, and the number $e$ of edges between $N(v)$ and $L_2$ satisfies
$e\ge m(\delta-b)$. Each $w\in L_2$ receives at most $|N[w]\cap N(v)|\le b$ of them, so $e\le b|L_2|$.
Therefore $|L_2|\ge m(\delta-b)/b$ and
$n\ge 1+m+m(\delta-b)/b=1+m\delta/b\ge1+\delta^2/b$.
Rearranging gives $\delta/b\le\sqrt{(n-1)/b}\le\sqrt{n-1}$.

Equality forces $b=1$ and $n=\delta^2+1$; with $b=1$ the graph has girth $\ge5$ and $n=\delta^2+1$
forces regularity and diameter 2, i.e. a Moore graph of girth 5; conversely such graphs have $b=1$,
$n=\delta^2+1$. ∎

**Corollary.** The lower bound of Proposition A never exceeds $\sqrt{n-1}$. No one-step
escape-counting argument can produce a graph with $c(G)>\sqrt n$.

## The high-girth bounds are capped the same way

Frankl (1987): girth $\ge8t-3$ implies $c>(\delta-1)^t$. Bradshaw–Hosseini–Mohar–Stacho (2023):
girth $g$ implies $c\ge\frac1g(\delta-1)^{\lfloor(g-1)/4\rfloor}$. The Moore bound gives
$n\ge(\delta-1)^{(g-1)/2}$ for odd $g$ and $n\ge2(\delta-1)^{g/2-1}$ for even $g$. In both cases
$(\delta-1)^{\lfloor(g-1)/4\rfloor}\le\sqrt n$ (for even $g$ use $\lfloor(g-1)/4\rfloor\le(g-2)/4$), so the
Bradshaw et al. bound is at most $\sqrt n/g$, and Frankl's bound is at most $n^{t/(4t-2)}\le\sqrt n$.

Heuristically the reason is uniform: a robber exploiting a tree-like ball of radius $r$ has about
$\delta^r$ escape targets, the cops need about $\sqrt{\delta^r}$ pieces to cover them, and the ball
alone has $\delta^r\le n$ vertices. Any argument that only looks at balls around the robber yields
at most $\sqrt n$. Products cannot amplify either: $c(G\,\square\,H)\le c(G)+c(H)$ while orders
multiply, and retracts (pendant or dominated vertices, blow-ups) never increase $c$. A counterexample
therefore has to be an irreducible family whose cop number exceeds every local bound by an unbounded
factor.
