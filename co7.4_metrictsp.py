import matplotlib.pyplot as plt
import networkx as nx
from math import inf

edgelist = [
    (0, 1, {"weight": 15}),
    (0, 2, {"weight": 10}),
    (0, 3, {"weight": 20}),
    (1, 2, {"weight": 5}),
    (1, 3, {"weight": 20}),
    (2, 3, {"weight": 15}),
]

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

def kruskal(G):
    edges = list(G.edges)
    edges.sort(key=lambda e : G[e[0]][e[1]]['weight'])
    H = nx.Graph()
    for e in edges:
        H.add_nodes_from(e)
        if BFS_disconnected(H,e):
            H.add_edge(*e)
    return H


def Euler(vertices, edges, s):
    W, x = [s], s
    while [edge for edge in edges if x in edge]:
        y = [edge for edge in edges if x in edge][0]
        edges.remove(y)
        y = list(y)
        y.remove(x)
        y = y[0]
        W += [(x,y), y]
        x = y
    V = []
    for k in range(int((len(W)-1)/2)):
        V += Euler(vertices, edges, W[2*k]) + [W[2*k+1]]
    V.append(s)
    return V


def tour_filter(walk):
    node_order = []
    for k in range(int((len(walk))/2)):
        node_order.append(walk[2*k])
    node_order.append(walk[-1])
    node_order = list(dict.fromkeys(node_order))
    newwalk = []
    for i in range(len(node_order)-1):
        newwalk += [node_order[i], (node_order[i], node_order[i+1])]
    newwalk += [node_order[-1], (node_order[0], node_order[-1]), node_order[0]]
    return newwalk


def double_tree(G):
    H = kruskal(G)
    mst_edges = list(H.edges)*2
    mst_vertices = list(H.nodes)
    return tour_filter(Euler(mst_vertices, mst_edges, 0))

print(double_tree(G))
