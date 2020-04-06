
def DFS(gr,node):
    # EXEMPLARY DFS IMPLEMENTATION
    visited = dict()
    for nd in gr.nodes:
        visited[nd] = 0

    def DFSutil(current):
        if visited[current]:
            visited[current] = 1
            return
        else:
            # here we can add processing of node
            visited[current] = 1
            if gr.hasneib(current):
                for nei in gr[current]:
                   DFSutil(nei)
    DFSutil(node)
    res = []
    for key in visited.keys():
        if visited[key] == 1:
            res.append(key)
    return res
