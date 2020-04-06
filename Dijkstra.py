import queue

def Dijkstra(node,gr):
    q = queue.PriorityQueue()
    distance = dict()
    processed = dict()
    for nd in gr.nodes:
        distance[nd] = float("Inf")
        processed[nd] = False
    distance[node] = 0
    q.put((0,node))
    while not q.empty():
        pair = q.get()
        nd = pair[1]
        dis = pair[0]
        if gr.hasneib(nd):
            for nei in gr[nd]:
                if distance[nei] > dis + gr.weight((nd,nei)) and not processed[nei]:
                    distance[nei] = dis + gr.weight((nd,nei))
                    q.put((distance[nei],nei))
        processed[nd] = True
    return distance
