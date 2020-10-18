import matplotlib.pyplot as plt
import networkx as nx
from math import inf

# edgelist = [
#     (0, 1, {"weight": 1}),
#     (0, 2, {"weight": 5}),
#     (1, 2, {"weight": 2}),
#     (1, 3, {"weight": 2}),
#     (1, 4, {"weight": 1}),
#     (2, 4, {"weight": 2}),
#     (3, 4, {"weight": 3}),
#     (3, 5, {"weight": 1}),
#     (4, 5, {"weight": 2}),
# ]

edgelist = [
    (0, 1, {"weight": 2}),
    (0, 2, {"weight": 5}),
    (0, 3, {"weight": 4}),
    (3, 1, {"weight": -9}),
]


edge_labels = {}
for (a,b,c) in edgelist:
    edge_labels[(a,b)] = c['weight']

G = nx.DiGraph(edgelist)
pos = nx.spring_layout(G)


def relax(u,v):
    G.nodes[v]['d'] = min(G.nodes[v]['d'], G.nodes[u]['d'] + G[u][v]['weight'])


def get_distance(v):
    return G.nodes[v]['d']


def Bellman_Ford(G, s):
    nodes = list(G.nodes)
    for v in nodes:
        G.nodes[v]['d'] = inf
    G.nodes[s]['d'] = 0
    for _ in range(len(list(G.edges))-1):
        for e in list(G.edges):
            relax(*e)
    d = []
    for node in nodes:
        d.append((node, G.nodes[node]['d']))
    return d


print(Bellman_Ford(G,0))


nx.draw(G,pos,edge_color='black',width=1,linewidths=1,
        node_size=500,node_color='pink',alpha=0.9,
        labels={node:node for node in G.nodes()})

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
