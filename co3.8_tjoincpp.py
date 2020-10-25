import matplotlib.pyplot as plt
import networkx as nx
import itertools
from math import inf

edgelist = [
    (1, 2, {"weight": 2}),
    (1, 4, {"weight": 10}),
    (2, 3, {"weight": 6}),
    (2, 5, {"weight": 8}),
    (3, 6, {"weight": 2}),
    (4, 5, {"weight": 3}),
    (4, 7, {"weight": 7}),
    (5, 6, {"weight": 5}),
    (5, 8, {"weight": 9}),
    (6, 9, {"weight": 10}),
    (7, 8, {"weight": 5}),
    (8, 9, {"weight": 1}),
]

edgelist = [
    ('a', 'b', {"weight": 50}),
    ('a', 'c', {"weight": 50}),
    ('a', 'd', {"weight": 50}),
    ('b', 'd', {"weight": 50}),
    ('b', 'e', {"weight": 70}),
    ('b', 'f', {"weight": 50}),
    ('c', 'd', {"weight": 70}),
    ('c', 'g', {"weight": 70}),
    ('c', 'h', {"weight": 120}),
    ('d', 'f', {"weight": 60}),
    ('e', 'f', {"weight": 70}),
    ('f', 'h', {"weight": 60}),
    ('g', 'h', {"weight": 70}),
]

edgelist = [
    ('a', 'c', {"weight": 3}),
    ('a', 'd', {"weight": 11}),
    ('a', 'g', {"weight": 1}),
    ('b', 'c', {"weight": 9}),
    ('b', 'e', {"weight": 5}),
    ('b', 'f', {"weight": 8}),
    ('c', 'd', {"weight": 12}),
    ('d', 'f', {"weight": 14}),
    ('d', 'g', {"weight": 4}),
    ('e', 'f', {"weight": 2}),
    ('e', 'g', {"weight": 18}),
]

G = nx.Graph(edgelist)


vertices = [2,4,6,8]


def relax(G,u,v,distances,prev_nodes):
    if distances[u] + G[u][v]['weight'] < distances[v]:
        prev_nodes[v] = u
        distances[v] = distances[u] + G[u][v]['weight']


def Dijkstra_x_to_y(G, x, y):
    distances = {}
    prev_nodes = {}
    for v in list(G.nodes):
        distances[v] = inf
    distances[x] = 0
    P = list(G.nodes)
    P.sort(key=lambda a : distances[a])
    while P:
        u = P.pop(0)
        for v in list(G.adj[u]):
            relax(G,u,v,distances,prev_nodes)
            P.append
            P.sort(key=lambda a : distances[a])
    v, path = y, []
    while v != x:
        path.insert(0, (prev_nodes[v], v))
        v = prev_nodes[v]
    return [distances[y], path]


def find_doubles(vertices):
    list_of_combs = []
    if len(vertices) == 2:
        return [[tuple(vertices)]]
    for i in range(1, len(vertices)):
        for item in find_doubles(vertices[1:i] + vertices[i+1:]):
            pairs = [(vertices[0], vertices[i])]
            list_of_combs.append(pairs + item)
    return list_of_combs


def find_lengths(G, vertices):
    lengths = {}
    for pair in list(itertools.combinations(vertices, 2)):
        lengths[pair] = Dijkstra_x_to_y(G, *pair)
    return lengths


def find_tjoin(G, vertices):
    combinations = find_doubles(vertices)
    lengths = find_lengths(G, vertices)
    min_length = inf
    for comb in combinations:
        total = 0
        new_edges = []
        for pair in comb:
            total += lengths[pair][0]
            new_edges += lengths[pair][1]
        if total < min_length:
            min_length = total
            opt_edges = new_edges
    return opt_edges



def tjoin_cpp(G):
    odd_degree_vertices = []
    for x in list(G.nodes):
        if G.degree[x] % 2 == 1:
            odd_degree_vertices.append(x)
    # return find_tjoin(G, odd_degree_vertices)
    new_edges = find_tjoin(G, odd_degree_vertices)
    total_length = 0
    for (u,v) in list(G.edges):
        total_length += G[u][v]['weight']
    for (u,v) in new_edges:
        total_length += G[u][v]['weight']
    return total_length, new_edges



print(tjoin_cpp(G))
