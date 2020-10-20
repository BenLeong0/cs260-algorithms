import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

G = Graph()
pos = nx.spring_layout(G)

G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from([
    (4, {"color": "red", "visited": False}),
    (5, {"color": "green"}),
])

G.add_edge(1, 2)
e = (2,3)
G.add_edge(*e)
G.add_edges_from([(1, 4, {"weight": 2}), (4, 5)])
G.add_edge(7,8)

H = nx.path_graph(10)

print('Nodes in G:', list(G.nodes))
print('Edges in G:', list(G.edges))
print('Vertices adjacent to 1:', list(G.adj[1]))

print('Edges incident to 1:', G.edges(1))
print('Edges incident to 2 or 7:', G.edges([2,7]))

print('Attributes of edge (1,4):', G[1][4])
G.nodes[4]['woa'] = 'hi'
print('Attributes of node 4:', G.nodes[4])


edgelist = [(0,1),(0,2),(2,3),(3,4),(0,4)]
H = nx.Graph(edgelist)
J = nx.subgraph(G,(1,2,3,5,7,8))
pos = nx.spring_layout(J)

nx.draw(J,pos,edge_color='black',width=1,linewidths=1,
        node_size=500,node_color='pink',alpha=0.9,
        labels={node:node for node in J.nodes()})

# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
