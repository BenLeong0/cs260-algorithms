import matplotlib.pyplot as plt
import networkx as nx
from math import inf

edgelist = [
    (0, 1, {"weight": 1}),
    (0, 2, {"weight": 5}),
    (1, 2, {"weight": 2}),
    (1, 3, {"weight": 2}),
    (1, 4, {"weight": 1}),
    (2, 4, {"weight": 2}),
    (3, 4, {"weight": 3}),
    (3, 5, {"weight": 1}),
    (4, 5, {"weight": 2}),
]

g_edge_labels = {}
for (a,b,c) in edgelist:
    g_edge_labels[(a,b)] = c['weight']

G = nx.Graph(edgelist)


def BFS_disconnected(G,e):
    u, v = e
    visited = {u}
    Q = [u]
    while Q:
        x = Q.pop(0)
        for y in list(G.adj[x]):
            if y not in visited:
                visited.add(y)
                Q.append(y)
    if v in visited:
        return False
    else:
        return True


def get_weight(e):
    return G[e[0]][e[1]]['weight']


def kruskal(G):
    edges = list(G.edges)
    edges.sort(key=get_weight)
    H = nx.Graph()
    for e in edges:
        H.add_nodes_from(e)
        if BFS_disconnected(H,e):
            H.add_edge(*e)
    return H


H = kruskal(G)
pos = nx.spring_layout(H)

edge_labels = {}
for edge in list(H.edges):
    edge_labels[edge] = g_edge_labels[edge]

nx.draw(H,pos,edge_color='black',width=1,linewidths=1,
        node_size=500,node_color='pink',alpha=0.9,
        labels={node:node for node in G.nodes()})

nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
