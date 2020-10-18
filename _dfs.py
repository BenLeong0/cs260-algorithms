import matplotlib.pyplot as plt
import networkx as nx

edgelist = [(0,1),(0,2),(2,3),(3,4),(0,4)]
G = nx.Graph(edgelist)


def DFS_Explore(G, v):
    if G.nodes[v]['visited'] == False:
        previsit(v)
        G.nodes[v]['visited'] = True
        for w in list(G.adj[v]):
            DFS_Explore(G, w)
        postvisit(v)


def DFS(G):
    nodes = list(G.nodes)
    for v in nodes:
        G.nodes[v]['visited'] = False
    for v in nodes:
        DFS_Explore(G, v)
    print('Attributes of node 4:', G.nodes[4])


def previsit(v):
    print('previsit', v)


def postvisit(v):
    print('postvisit', v)


DFS(G)

nx.draw(G, with_labels=True, font_weight="bold")
plt.show()
