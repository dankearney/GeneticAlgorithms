import networkx as nx
import random
import string
from GraphPlotter import GraphPlotter

N = 5
G=nx.Graph(labelDict={})
for i in range(N):
    G.add_node(i)
    G.graph['labelDict'][i] = string.ascii_letters[i]
for i in range(N):
    for j in range(N):
        if i==j: continue
        G.add_edge(i, j, distance=random.randrange(100, 200))

plotter = GraphPlotter(G)
plotter.plot()