import matplotlib.pyplot as plt
import networkx as nx
from math import inf

# edgelist = [
#     (0, 1, {"capacity": 4}),
#     (0, 2, {"capacity": 2}),
#     (1, 2, {"capacity": 1}),
#     (1, 3, {"capacity": 2}),
#     (2, 3, {"capacity": 3}),
# ]

edgelist = [
    (0, 1, {"capacity": 16}),
    (0, 2, {"capacity": 13}),
    (1, 2, {"capacity": 10}),
    (1, 3, {"capacity": 12}),
    (2, 1, {"capacity": 4}),
    (2, 4, {"capacity": 14}),
    (3, 2, {"capacity": 9}),
    (3, 5, {"capacity": 20}),
    (4, 3, {"capacity": 7}),
    (4, 5, {"capacity": 4}),
]

G = nx.DiGraph(edgelist)


def exists_path(G,s,t):
    check = dict(zip(
            [node for node in list(G.nodes)],
            [False for node in list(G.nodes)]
    ))
    paths = {s: []}
    Q = [s]
    check[s] = True
    while Q:
        u = Q.pop(0)
        for v in list(G.successors(u)):
            if v == t:
                return paths[u] + [(u,t)]
            if not check[v]:
                check[v] = True
                paths[v] = paths[u] + [(u,v)]
                Q.append(v)
    return False


def min_cap(N, path):
    cap = inf
    for (u,v) in path:
        cap = min(cap, N[u][v]['capacity'])
    return cap


def val(N,f,s):
    value = 0
    for (u,v) in f:
        if u == s:
            value += f[(u,v)]
        elif v == s:
            value -= f[(u,v)]
    return value


def residual_network(G,f):
    N = nx.DiGraph()
    for (u,v) in list(G.edges):
        if f[(u,v)] < G[u][v]['capacity']:
            N.add_edge(u,v)
            N[u][v]['capacity'] = G[u][v]['capacity'] - f[(u,v)]
        if f[(u,v)] > 0:
            N.add_edge(v,u)
            N[v][u]['capacity'] = f[(u,v)]
    print(list(N.edges))
    return N


def ford_fulkerson(G, s=0, t=-1):
    f = dict(zip(
        [(u,v) for (u,v) in list(G.edges)]+[(v,u) for (u,v) in list(G.edges)],
        [0 for edge in list(G.edges)]+[0 for edge in list(G.edges)]
    ))
    N = residual_network(G,f)
    path = exists_path(G,s,t)
    while path:
        aug_val = min_cap(N, path)
        for (u,v) in path:
            f[(u,v)] += aug_val
        N = residual_network(G,f)
        path = exists_path(N,s,t)
    return N, val(N,f,s)

N, value = ford_fulkerson(G,list(G.nodes)[0],list(G.nodes)[-1])
pos = nx.spring_layout(N)
print('Flow value:', value)

edge_labels = {}
for (u,v) in list(N.edges):
    edge_labels[(u,v)] = N[u][v]['capacity']

nx.draw(N,pos,edge_color='black',width=1,linewidths=1,
        node_size=500,node_color='pink',alpha=0.9,
        labels={node:node for node in N.nodes()})

nx.draw_networkx_edge_labels(N, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
