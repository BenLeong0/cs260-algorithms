import matplotlib.pyplot as plt
import networkx as nx
from math import inf

edgelist = [
    (0,2), (0,4), (1,2), (1,3), (1,5), (1,6), (2,4),
    (2,5), (3,4), (3,5), (3,6), (4,6), (5,6),
]

G = nx.Graph(edgelist)


def Euler(G, x):
    W = [x]
    while G.edges(x):
        e = list(G.edges(x))[0]
        G.remove_edge(*e)
        print('Adding edge', e)
        print('Edges covered:', len(edgelist)-len(list(G.edges)),'/',len(edgelist))
        W += [e, e[1]]
        x = e[1]
    V = []
    for i in range(int((len(W)-1)/2)):
        V += Euler(G,W[2*i])
        V.append(W[2*i + 1])
    V.append(W[-1])
    return V


walk = Euler(G,0)
print(walk)
