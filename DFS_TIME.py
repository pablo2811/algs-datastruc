

def dfs_time(gr, node=0):

    # returns dict of times when node-processing was finished
    visited = dict()
    counter = dict()
    counter[-1] = 0
    for nd in gr.nodes:
        visited[nd] = 0

    def DFSutil(current):
        counter[-1] += 1
        visited[current] = 1
        if gr.hasneib(current):
            for nei in gr[current]:
                if not visited[nei]:
                    DFSutil(nei)
        counter[-1] += 1
        counter[current] = counter[-1]

    if not node:
        node = gr.anyvertice()
    DFSutil(node)
    for key in visited.keys():
        if not visited[key]:
            DFSutil(key)
    del counter[-1]
    return counter


