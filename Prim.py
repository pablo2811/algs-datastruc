import queue,GRAPHS


def minspantree(g):
    v = g.anyvertice()
    p = queue.PriorityQueue()
    n = len(g)
    t = GRAPHS.Tree()
    s = 0
    parents = dict()
    for i in range(n-1):
        for nei in g[v]:
            if nei not in t.nodes:
                p.put((g.weight((v,nei)),nei))
                parents[nei] = v
        good = p.get()
        while good[1] in t.nodes:
            good = p.get()
        t.add_edge(parents[good[1]],good[1],good[0])
        s += good[0]
        v = good[1]
    t.set_edge_sum(s)
    return t






