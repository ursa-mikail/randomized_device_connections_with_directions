import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a directed graph
G = nx.DiGraph()

# Add devices
devices = ["Device01", "Device02", "Device03", "Device04", "Cloud"]
G.add_nodes_from(devices)

# Define connection modes
connection_modes = ["uni", "bi", "none"]

# Randomly generate connections
connections = []
for i in range(len(devices)):
    for j in range(i + 1, len(devices)):
        connection_mode = random.choice(connection_modes)
        connections.append((devices[i], devices[j], connection_mode))

"""
# Define connections (edges) and their direction (uni-directional/ bi-directional)
connections = [("Device01", "Device02", 'bi'),
               ("Device02", "Device03", 'none'),
               ("Device03", "Cloud", 'uni'),
               ("Device01", "Cloud", 'bi')]
"""

for edge in connections:
    if edge[2] == 'uni':
        G.add_edge(edge[0], edge[1], direction='->')
    elif edge[2] == 'bi':
        G.add_edge(edge[0], edge[1], direction='<->')
        G.add_edge(edge[1], edge[0], direction='<->')
    elif edge[2] == 'none':
        G.add_edge(edge[0], edge[1], direction='-')

# Define positions for the nodes (optional, for better visualization)
pos = nx.spring_layout(G)

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue", font_color="black")

# Add edge labels for direction
edge_labels = {(edge[0], edge[1]): f"{G[edge[0]][edge[1]]['direction']}" for edge in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw edges with different arrow styles
for edge in G.edges():
    direction = G[edge[0]][edge[1]]['direction']
    if direction == '->':
        nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='black', arrows=True)
    elif direction == '<->':
        nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='black', arrows=True, connectionstyle="arc3,rad=0.1")
    elif direction == '-':
        nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='black', arrows=False)

plt.show()


# ref: 
# https://stackoverflow.com/questions/60067022/multidigraph-edges-from-networkx-draw-with-connectionstyle
# https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html
