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


def connected_components(G):
    nodes = list(G.nodes)
    components = []
    while nodes:
        R, Q, T = {nodes[0]}, {nodes[0]}, set()
        while Q:
            v = Q.pop()
            if v in nodes:
                nodes.remove(v)
            if set(G.adj[v]).intersection(set(G.nodes)-R):
                w = set(G.adj[v]).intersection(set(G.nodes)-R).pop()
                R.add(w)
                Q.update([v,w])
                T.add((v,w))
        components.append(tuple(R))
    return components


def is_complete(G, x, nodes):
    for node in nodes:
        if (x, node) not in list(G.edges) and (node, x) not in list(G.edges):
            return False
    return True


def is_anticomplete(G, x, nodes):
    for node in nodes:
        if (x, node) in list(G.edges) or (node, x) in list(G.edges):
            return False
    return True


def is_module(G, nodes):
    rem = [node for node in list(G.nodes) if node not in nodes]
    for node in rem:
        if not is_complete(G, node, nodes) and not is_anticomplete(G, node, nodes):
            return False
    return True


def sub_lists(l):
    base = []
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists += orig
    lists.sort(key=len, reverse=True)
    if len(lists[0]) == 1:
        return lists
    return lists[1:]


def proper_modules(G):
    nodes = list(G.nodes)
    modules = []
    while nodes:
        sublists = sub_lists(nodes)
        for set in sublists:
            if is_module(G, set):
                modules.append(set)
                nodes = [x for x in nodes if x not in set]
                break
    return modules


def sub_tree(G, T, x):
    if len(list(G.nodes)) == 1:
        return
    components = connected_components(G)
    co_components = connected_components(nx.complement(G))
    if len(components) != 1:                # If disconnected
        for component in components:
            T.add_edge(x, tuple(component))
            C = nx.subgraph(G,component)
            sub_tree(C, T, x)
        return
    elif len(co_components) != 1:            # If co-disconnected
        for co_component in co_components:
            v = tuple(co_component)
            T.add_edge(x, v)
            C = nx.subgraph(G,co_component)
            sub_tree(C, T, v)
        return
    else:
        modules = proper_modules(G)
        for module in modules:
            v = tuple(module)
            T.add_edge(x, v)
            C = nx.subgraph(G,module)
            sub_tree(C, T, v)
        return
    return T


def modular_decomp(G):
    T = nx.Graph()
    nodes = tuple(G.nodes)
    T.add_node(nodes)
    sub_tree(G, T, nodes)
    return T

T = modular_decomp(G)
pos = nx.spring_layout(T)

nx.draw(T,pos,edge_color='black',width=1,linewidths=1,
        node_size=500,node_color='pink',alpha=0.9,
        labels={node:node for node in T.nodes()})
plt.axis('off')
plt.show()
