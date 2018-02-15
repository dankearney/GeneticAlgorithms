import networkx as nx
import matplotlib.pyplot as plt
import random
import string

N = 5

G=nx.Graph()
G.add_nodes_from(range(N))
for i in range(N):
    for j in range(N):
        if i==j: continue
        G.add_edge(i, j, distance=random.randrange(100, 200))

try:
    pos = nx.kamada_kawai_layout(G, weight='distance')

    nx.draw_networkx_nodes(G, pos)
    
    nx.draw_networkx_edges(G, pos)

    edge_labels = nx.get_edge_attributes(G,'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, rotate=False)

    plt.show()
except:
    print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
    raise
