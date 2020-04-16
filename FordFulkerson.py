import copy


def path_search(dg,s,t):
    # can be improved using Edmond's-Karp alg.(bfs, "shortest" p) or scaling algorithm (threshold edge value)
    # then choosing paths is done in more "intelligent" way.
    def util(current):
        visited[current] = 1
        if current == t:
            return path
        else:
            for nei in dg[current]:
                if not visited[nei] and dg.weight((current,nei))>0:
                    path.append((current,nei))
                    z = util(nei)
                    if z:
                        return z
                    visited[nei] = 0
                    path.pop()
    path = []
    visited = dict()
    for nd in g.nodes:
        visited[nd] = 0
    return util(s)


def add_reversed(gr):
    a = copy.deepcopy(gr.edges)
    for e in a:
        gr.add_edge(a=e[1], b=e[0], w=0)


def mincutset(gr,s):

    def util(curr):
        vis.add(curr)
        for nei in gr[curr]:
            if gr.weight((curr,nei)) > 0 and nei not in vis:
                util(nei)

    edges = []
    vis = set()
    util(s)
    for nd in vis:
        for nei in gr[nd]:
            if nei not in vis and not gr.weight((nd,nei)):
                edges.append((nd,nei))
    return edges

def ff(gr, s, t):

    dg = copy.deepcopy(gr)
    add_reversed(dg)
    while True:
        p = path_search(dg,s,t)
        if not p:
            break
        else:
            m = 1000000
            for e in p:
                if dg.weight(e) < m :
                    m = dg.weight(e)
            for e in p:
                dg.weights[e] -= m
                dg.weights[(e[1],e[0])] += m
    sx = 0
    for nei in dg[t]:
        sx += dg.weight((t,nei))
    print(f"Maximal flow (minimal cut) for given flow network is {sx}.")
    print(f"Lowest weight edges separating {s} and {t} are {mincutset(dg,s)}.")
    return sx










