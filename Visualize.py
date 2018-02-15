import networkx as nx
import matplotlib.pyplot as plt
import random
import string

N = 5
labelDict = {}

G=nx.Graph()
for i in range(N):
    G.add_node(i)
    labelDict[i] = string.ascii_letters[i]
for i in range(N):
    for j in range(N):
        if i==j: continue
        G.add_edge(i, j, distance=random.randrange(100, 200))

try:
    pos = nx.kamada_kawai_layout(G, weight='distance')

    nx.draw_networkx_nodes(G, pos, node_color='cornflowerblue')
    nx.draw_networkx_labels(G, pos, labelDict)
    
    nx.draw_networkx_edges(G, pos, edge_color='gray')

    edge_labels = nx.get_edge_attributes(G,'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, rotate=False)

    plt.show()
except:
    print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
    raise
