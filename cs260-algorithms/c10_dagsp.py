import matplotlib.pyplot as plt
import networkx as nx
from math import inf

# edgelist = [(5,0),(5,2),(2,3),(4,0),(4,1),(3,1)]
# edgelist = [(7,5),(7,6),(5,4),(6,4),(5,2),(6,3),(2,1),(3,1),(1,0)]

edgelist = [
    (0, 1, {"weight": 1}),
    (0, 2, {"weight": -5}),
    (1, 2, {"weight": 2}),
    (1, 3, {"weight": 2}),
    (1, 4, {"weight": 1}),
    (2, 4, {"weight": 2}),
    (3, 4, {"weight": 3}),
    (3, 5, {"weight": 1}),
    (4, 5, {"weight": 2}),
]

edge_labels = {}
for (a,b,c) in edgelist:
    edge_labels[(a,b)] = c['weight']

G = nx.DiGraph(edgelist)
pos = nx.spring_layout(G)


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


def DAG_SP(G, s):
    nodes = list(G.nodes)
    G.nodes[s]['d'] = 0
    T = TSort(G)
    T.remove(s)
    for v in T:
        G.nodes[v]['d'] = inf
        for u in list(G.predecessors(v)):
            new = G.nodes[u]['d']+G[u][v]['weight']
            G.nodes[v]['d'] = min(G.nodes[v]['d'], new)
    d = []
    for node in nodes:
        d.append((node, G.nodes[node]['d']))
    return d

print(DAG_SP(G,0))

nx.draw(G,pos,edge_color='black',width=1,linewidths=1,
        node_size=500,node_color='pink',alpha=0.9,
        labels={node:node for node in G.nodes()})

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
