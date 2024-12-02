import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f', 'g'], type = 'machine')
G.add_nodes_from(['h', 'i', 'j'], type = 'human')
G.add_edges_from([('a', 'c'), ('a', 'b'), ('a', 'd'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'g'), ('c', 'f'), ('c', 'd'), ('d', 'f'), ('d', 'e'), ('d', 'g'), ('e', 'g'), ('f', 'g'), ('f', 'h'), ('g', 'h'), ('h', 'i'), ('i', 'j')])

plt.figure()
pos_nodes = nx.spring_layout(G)
nx.draw(G, pos_nodes, with_labels=True)

pos_attrs = {}
for node, coords in pos_nodes.items():
    pos_attrs[node] = (coords[0], coords[1] + 0.08)

node_attrs = nx.get_node_attributes(G, 'type')
custom_node_attrs = {}
for node, attr in node_attrs.items():
    custom_node_attrs[node] = "{'type': '" + attr + "'}"

nx.draw_networkx_labels(G, pos_attrs, labels=custom_node_attrs)
plt.show()
