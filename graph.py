
class DirectedGraph:
    # we assume it's simple (no double-edges)
    def __init__(self):
        self.g = dict()
        self.nodes = set()
        self.weights = dict()
        self.edges = []

    def add_edge(self, a, b, w=1):
        self.edges.append((a,b))
        if b not in self.g.keys():
            self.nodes.add(b)
        if a in self.g.keys():
            self.g[a].append(b)
        else:
            self.g[a] = [b]
            self.nodes.add(a)
        self.weights[(a, b)] = w

    def remove_edge(self,a,b):
        self.g[a].remove(b)
        if len(self.g[a]) == 0:
            del self.g[a]
        self.edges.remove((a,b))
        del self.weights[(a,b)]

    def edgesnumber(self):
        return len(self.edges)

    def deg(self,a):
        return len(self.g[a])

    def edg(self):
        return self.edges

    def weight(self,e):
        return self.weights[e]

    def __getitem__(self, item):
        return self.g[item]

    def __len__(self):
        return len(self.nodes)

    def hasneib(self,a):
        return a in self.g.keys()