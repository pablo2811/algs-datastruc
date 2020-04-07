import GRAPHS

def search(st,end,t):

    visited = set()
    def search_util(curr,prev,visited):
        visited.add(curr)
        for nd in t[curr]:
            if nd != prev:
                search_util(nd,curr,visited)

    search_util(st,st,visited)
    return end in visited

def minspantree(g):

    t = GRAPHS.Tree()
    for nd in g.nodes:
        t.add_vertice(nd)
    edges_sorted = sorted(g.edges,key=g.weight)
    n = len(g)
    t.add_edge(edges_sorted[0][0],edges_sorted[0][1],w=g.weight(edges_sorted[0]))
    j = 1
    min_sum = g.weight(edges_sorted[0])
    for i in range(1,n-1):
        while search(edges_sorted[j][0],edges_sorted[j][1],t):
            j += 1
        t.add_edge(edges_sorted[j][0],edges_sorted[j][1])
        min_sum += g.weight(edges_sorted[j])
        j += 1
    print(min_sum)
    return t




minspantree(g)

