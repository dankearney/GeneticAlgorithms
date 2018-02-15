import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_nodes_from([2,3])
G.add_edge(2, 3, weight=107)
try:
    nx.draw(G)
    plt.show()
except:
    print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
    raise
