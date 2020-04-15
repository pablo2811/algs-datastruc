import DFS_TIME,DFS

def insert(vals,nodes,v,n):

    vals.append(v)
    nodes.append(n)
    if len(vals) == 2:
        if vals[0] > v:
            vals[0], vals[1] = vals[1], vals[0]
            nodes[0], nodes[1] = nodes[1], nodes[0]
    elif len(vals) >= 3 :
        j = len(vals) - 2
        while vals[j] > v:
            vals[j],vals[j+1] = vals[j+1],vals[j]
            nodes[j], nodes[j + 1] = nodes[j + 1], nodes[j]
            j -= 1

def kosaraju(dag):
    # IMPLEMENTATION OF KOSARAJU'S ALGORITHM (CALCULATE SSC FOR DAG)
    times = DFS_TIME.dfs_time(dag)
    vals = []
    nodes = []
    for key in times.keys():
        insert(vals,nodes,times[key],key)
    rev_dag = dag.reverse_edges()
    ssc = []
    processed = set()
    while len(nodes):
        nd = nodes.pop()
        if nd not in processed:
            s = DFS.dfs(rev_dag,nd,True,processed)
            processed = processed.union(s)
            ssc.append(s)
    return ssc

