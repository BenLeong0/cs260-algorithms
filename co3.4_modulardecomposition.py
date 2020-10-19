import matplotlib.pyplot as plt
import networkx as nx
from math import inf

edgelist = [
    (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5),
    (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4),
    (3, 5), (3, 6), (4, 5), (4, 6), (5, 7), (5, 8),
    (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10),
    (7, 8), (7, 9), (7, 10), (8, 9), (8, 10),
]

G = nx.Graph(edgelist)


def sub_tree(G, H, x):
    return H


def modular_decomp(G):
    H = nx.Graph()
    nodes = tuple(G.nodes)
    H.add_node(nodes)
    sub_tree(G, H, nodes)
    return H


H = modular_decomp(G)
print(list(H.nodes))
print(list(H.edges))
