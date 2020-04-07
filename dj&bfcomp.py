import matplotlib.pyplot as plt,random,GRAPHS,Dijkstra,BellmanFord


def comparisionDJBF():
    g = GRAPHS.DirectedGraph()
    t_bf = []
    t_dik = []
    for n in range(10,5000,80):
        for k in range(n):
            a = random.randint(1,n)
            b = random.randint(1,n)
            w = random.randint(1,n)
            g.add_edge(a,b,w)
            g.add_edge(b,a,w)
        t_bf.append(BellmanFord.BellmanFord(a,g))
        t_dik.append(Dijkstra.Dijkstra(a,g))

    x = [i for i in range(10,5000,80)]
    plt.plot(x,t_bf,color="red",label='Bellman-Ford')
    plt.plot(x,t_dik,color="blue",label='Dijkstra')
    plt.xlabel("Number of edges")
    plt.ylabel("Time of execution")
    plt.title("Bellman-Ford & Dijkstra comparision")
    plt.legend()
    plt.savefig("BF-Dijkstra comparision.png")

