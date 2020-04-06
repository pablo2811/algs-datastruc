
def FloydWarshall(gr):
    n = len(gr)
    tab = [[float("Inf") for k in range(n)] for i in range(n)]
    mapping = dict()
    i = 0
    for nd in gr.nodes:
        mapping[nd] = i
        i += 1
    for i in range(n):
        tab[i][i] = 0
    for ed in gr.edges:
        tab[mapping[ed[0]]][mapping[ed[1]]] = gr.weight(ed)

    for k in range(n):
        for j in range(n):
            for i in range(n):
                tab[j][i] = min(tab[j][i],tab[j][k] + tab[k][i])
    for k in mapping.keys():
        print(k,mapping[k])
    for r in tab:
        print(r)
    return tab
