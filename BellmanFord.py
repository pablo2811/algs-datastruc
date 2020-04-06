

def BellmanFord(node, gr):
    dist = dict()
    for nd in gr.nodes:
        dist[nd] = float("Inf")
    dist[node] = 0
    for i in range(len(gr) - 1):
        change = False
        for e in gr.edg():
            if dist[e[1]] > dist[e[0]] + gr.weight(e):
                dist[e[1]] = dist[e[0]] + gr.weight(e)
                change = True
        if not change:
            break  # optimization to BF
    return dist