import matplotlib.pyplot as plt
import networkx as nx
from math import inf

edgelist = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 1),
    (2, 4), (3, 2), (3, 5), (4, 3), (4, 5),
]

G = nx.Graph(edgelist)


def graph_scan(G,s):
    R, Q, T = {s}, {s}, set()
    while Q:
        v = Q.pop()
        if set(G.adj[v]).intersection(set(G.nodes)-R):
            w = set(G.adj[v]).intersection(set(G.nodes)-R).pop()
            R.add(w)
            Q.update([v,w])
            T.add((v,w))
    return R, T


print(graph_scan(G,0))
