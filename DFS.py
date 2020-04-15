
def dfs(gr,node,returnset=False,processed=False):
    # EXEMPLARY DFS IMPLEMENTATION
    visited = dict()
    for nd in gr.nodes:
        visited[nd] = 0

    def DFSutil(current):
        # here we can add processing of node
        visited[current] = 1
        if gr.hasneib(current):
            for nei in gr[current]:
                if (not processed or nei not in processed) and not visited[nei]:
                    DFSutil(nei)
    DFSutil(node)
    if returnset:
        res = set()
    else:
        res = []
    for key in visited.keys():
        if visited[key] == 1:
            if returnset:
                res.add(key)
            else:
                res.append(key)
    return res
