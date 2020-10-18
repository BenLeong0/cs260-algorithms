import matplotlib.pyplot as plt
import networkx as nx

edgelist = [(0,1),(0,2),(2,3),(3,4),(0,4)]
G = nx.Graph(edgelist)


def DFS_Explore(G, v, counter):
    if G.nodes[v]['visited'] == False:
        previsit(v, counter)
        counter += 1
        G.nodes[v]['visited'] = True
        for w in list(G.adj[v]):
            counter = DFS_Explore(G, w, counter)
        postvisit(v, counter)
        counter += 1
    return counter


def Counter_DFS(G):
    nodes = list(G.nodes)
    counter = 0
    for v in nodes:
        G.nodes[v]['visited'] = False
    for v in nodes:
        counter = DFS_Explore(G, v, counter)


def previsit(v, counter):
    G.nodes[v]['pre'] = counter


def postvisit(v, counter):
    G.nodes[v]['post'] = counter


Counter_DFS(G)

for v in list(G.nodes):
    print('Attributes of node', v, ':', G.nodes[v])

nx.draw(G, with_labels=True, font_weight="bold")
plt.show()
