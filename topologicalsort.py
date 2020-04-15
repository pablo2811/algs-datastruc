

def con_topological(dag):
    # dag stands for DirectedAcyclicGraph
    def util_top(st,curr):
        st[curr] = 1
        if dag.hasneib(curr):
            for nd in dag[curr]:
                if st[nd] == 0:
                    util_top(st,nd)
                elif st[nd] == 1:
                    raise Exception("Topological sort cannot be created due to cycle in DAG.")
        st[curr] = 2
        top.append(curr)
    state = dict()
    top = []
    for nd in dag.nodes:
        state[nd] = 0  # 0 not processed 1 under processing 2 processed
    for key in state:
        if not state[key]:
            util_top(state,key)
    return top[::-1]

