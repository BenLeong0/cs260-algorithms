import matplotlib.pyplot as plt
import networkx as nx

# edgelist = [(5,0),(5,2),(2,3),(4,0),(4,1),(3,1)]
edgelist = [(7,5),(7,6),(5,4),(6,4),(5,2),(6,3),(2,1),(3,1),(1,0)]
G = nx.DiGraph(edgelist)


def DFS_Explore(G, v, T):
    if G.nodes[v]['visited'] == False:
        G.nodes[v]['visited'] = True
        for w in list(G.adj[v]):
            T = DFS_Explore(G, w, T)
        T.insert(0,v)
    return T


def TSort(G):
    nodes = list(G.nodes)
    T = []
    for v in nodes:
        G.nodes[v]['visited'] = False
    for v in nodes:
        T = DFS_Explore(G, v, T)
    return T


print(TSort(G))

nx.draw(G, with_labels=True, font_weight="bold")
plt.show()
