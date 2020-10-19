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

G = nx.Graph(edgelist)


def get_weight(G,e):
    u, v = e
    return G[u][v]['weight']


def prim(G):
    edges = list(G.edges)
    edges.sort(key=lambda e: get_weight(G,e))
    H = nx.Graph()
    H.add_node(0)
    while set(H.nodes) != set(G.nodes):
        for (u,v) in edges:
            if u in list(H.nodes) or v in list(H.nodes):
                new_edge = (u,v)
                break
        H.add_edge(*new_edge)
        for (u,v) in edges:
            if u in list(H.nodes) and v in list(H.nodes):
                edges.remove((u,v))
    return list(H.edges)


print(prim(G))
