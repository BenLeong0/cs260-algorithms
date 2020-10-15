import matplotlib.pyplot as plt
import networkx as nx


def BFS(G):
    nodes = list(G.nodes)
    for v in nodes:
        G.nodes[v]['visited'] = False
    Q = [nodes[0]]
    level = 0
    G.nodes[nodes[0]]['level'] = level
    while Q:
        u = Q.pop(0)
        if G.nodes[u]['visited'] == False:
            G.nodes[u]['visited'] = True
            for w in list(G.adj[u]):
                Q.append(w)
                if 'level' not in G.nodes[w]:
                    G.nodes[w]['level'] = G.nodes[u]['level']+1
    for u in nodes:
        print('Vertex', u, 'level:', G.nodes[u]['level'])


def odd_cycle_existance(G):
    BFS(G)
    for (u,v) in G.edges:
        if G.nodes[u]['level'] == G.nodes[v]['level']:
            return True
    return False



edgelist = [(0,1),(0,2),(2,3),(3,4),(0,4)]
G = nx.Graph(edgelist)



print(odd_cycle_existance(G))

nx.draw(G, with_labels=True, font_weight="bold")
plt.show()
