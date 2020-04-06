
def BFS(node,gr):
    # EXEMPLARY IMPLEMENTATION OF BFS
    queue = [node]
    distance = dict()
    for nd in gr.nodes:
        distance[nd] = float("Inf")
    visited = dict()
    distance[node] = 0
    while len(queue):
        act = queue.pop()
        # here we can process the node (e.g lookup for some info)
        if act not in visited.keys() and gr.hasneib(act):
            # here we search through adjacent ver.
            for nd in gr[act]:
                queue.append(nd)
                distance[nd] = min(distance[nd],distance[act] + 1)
        visited[act] = 1

