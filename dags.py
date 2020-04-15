import topologicalsort,GRAPHS

# this module presents ways of using dp & topological sort to answer quieries in dag (directedacyclic).
# 1. how many diffrent paths (from a to b)
# 2. shortest /  longest
# 3. which nodes are ALWAYS in the path.

def diff_paths(st,end,dag):

    tp = topologicalsort.con_topological(dag)
    for k in range(len(tp)):
        if tp[k] == end:
            return 0
        if tp[k] == st:
            i = k
            break
    ways = dict()
    ways[st] = 1
    w = i + 1
    while True:
        for j in range(i,w):
            if tp[w] in dag[tp[j]]:
                if tp[w] in ways.keys():
                    ways[tp[w]] += ways[tp[j]]
                else:
                    ways[tp[w]] = ways[tp[j]]
        if tp[w] == end:
            break
        w += 1
    return ways[end]


def listofpaths(st,end,dag):

    tp = topologicalsort.con_topological(dag)
    for k in range(len(tp)):
        if tp[k] == end:
            return 0
        if tp[k] == st:
            i = k
            break
    ways = dict()
    ways[st] = [[st]]
    w = i + 1
    while True:
        for j in range(i,w):
            if tp[w] in dag[tp[j]]:
                if tp[w] not in ways.keys():
                    ways[tp[w]] = []
                for s in ways[tp[j]]:
                    a  = s.copy()
                    a.append(tp[w])
                    ways[tp[w]].append(a)

        if tp[w] == end:
            break
        w += 1
    return ways[end]


def shortest(st,end,dag):

    tp = topologicalsort.con_topological(dag)
    for k in range(len(tp)):
        if tp[k] == end:
            return None
        if tp[k] == st:
            i = k
            break
    sh = dict()
    sh[st] = 0
    w = i + 1
    while True:
        for j in range(i,w):
            if tp[w] in dag[tp[j]]:
                if tp[j] in sh.keys() and tp[w] in sh.keys():
                    sh[tp[w]] = min(sh[tp[j]]+1,sh[tp[w]])
                elif tp[j] in sh.keys():
                    sh[tp[w]] = sh[tp[j]] + 1
        if tp[w] == end:
            break
        w += 1
    return sh[end]





