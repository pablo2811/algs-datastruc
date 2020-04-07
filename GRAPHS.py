from abc import abstractmethod


class Graph:
    @abstractmethod
    def add_edge(self, a, b, w=1):
        pass

    @abstractmethod
    def remove_edge(self, a, b):
        pass

    @abstractmethod
    def deg(self, n):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass


class DirectedGraph(Graph):
    # we assume it's simple (no double-edges) and directed.
    def __init__(self):
        self.g = dict()
        self.nodes = set()
        self.weights = dict()
        self.edges = []

    def add_edge(self, a, b, w=1):
        self.edges.append((a, b))
        if b not in self.g.keys():
            self.nodes.add(b)
        if a in self.g.keys():
            self.g[a].append(b)
        else:
            self.g[a] = [b]
            self.nodes.add(a)
        self.weights[(a, b)] = w

    def remove_edge(self, a, b):
        self.g[a].remove(b)
        if len(self.g[a]) == 0:
            del self.g[a]
        self.edges.remove((a, b))
        del self.weights[(a, b)]

    def edgesnumber(self):
        return len(self.edges)

    def deg(self, a):
        return len(self.g[a])

    def edg(self):
        return self.edges

    def weight(self, e):
        return self.weights[e]

    def __getitem__(self, item):
        return self.g[item]

    def __len__(self):
        return len(self.nodes)

    def hasneib(self, a):
        return a in self.g.keys()


class UndirectedGraph(Graph):

    # we assume it's simple (no double-edges).
    def __init__(self):
        self.g = dict()
        self.nodes = set()
        self.weights = dict()
        self.edges = []

    def add_edge(self, a, b, w=1):

        self.edges.append((a, b))
        self.weights[(a, b)] = w

        def add_edge_util(a, b):
            if a in self.nodes:
                self.g[a].append(b)
            else:
                self.g[a] = [b]
                self.nodes.add(a)

        add_edge_util(a, b)
        add_edge_util(b, a)

    def remove_edge(self, a, b):
        self.g[a].remove(b)
        self.g[b].remove(a)
        if not len(self.g[a]):
            del self.g[a]
        if not len(self.g[b]):
            del self.g[b]
        self.edges.remove((a, b))
        del self.weights[(a, b)]

    def edgesnumber(self):
        return len(self.edges)

    def deg(self, a):
        return len(self.g[a])

    def edg(self):
        return self.edges

    def weight(self, e):
        return self.weights[e]

    def __getitem__(self, item):
        return self.g[item]

    def __len__(self):
        return len(self.nodes)

    def hasneib(self, a):
        return a in self.g.keys()


class Tree(Graph):

    # we assume that tree is undirected. (It's more like forest in g-theory)
    def __init__(self, root=None):
        self.t = dict()
        self.leaves = set()
        self.nodes = set()
        self.root = root

    def add_edge(self, a, b, w=1):
        self.starter = a

        def add_edge_util(a, b):
            if a in self.nodes:
                self.t[a].append(b)
            else:
                self.t[a] = [b]
                self.nodes.add(a)

        if b in self.nodes and a in self.nodes:
            raise Exception("Tree structure can not contain cycles.")
        else:
            add_edge_util(a, b)
            add_edge_util(b, a)
        self.update_leaves()

    def __len__(self):
        return len(self.nodes)

    def remove_edge(self, a, b):
        self.t[a].remove(b)
        self.t[b].remove(a)

    def deg(self, n):
        return len(self.t[n])

    def __getitem__(self, item):
        return self.t[item]

    def update_leaves(self):
        for nd in self.nodes:
            if self.deg(nd) == 1 and nd not in self.leaves:
                self.leaves.add(nd)
                self.special_leave = nd

    def add_vertice(self, a):
        # useful in constructing minimum spinning tree
        self.t[a] = []

    def diameter(self):
        # longest path in tree
        nd = self.special_leave
        count = dict()
        count[nd] = -1

        def search(curr, prev, count):
            count[curr] = count[prev] + 1
            for nei in self.t[curr]:
                if nei != prev:
                    search(nei, curr, count)

        search(nd, nd, count)
        M = -1

        for k in count.keys():
            M = max(M, count[k])
        return M







