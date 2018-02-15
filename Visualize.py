import networkx as nx
import matplotlib.pyplot as plt

# WARNING! You need a window manager like Ximg
import subprocess
subprocess.call("export DISPLAY=:0", shell=True)

G=nx.Graph()
G.add_nodes_from([2,3])
G.add_edge(2, 3, weight=107)
nx.draw(G)
plt.show()
