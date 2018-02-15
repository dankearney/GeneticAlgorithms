import networkx as nx
import random
import string
from GraphPlotter import GraphPlotter

class FullyConnectedGraph:

    def __init__(self, num_nodes=5, min_distance=100, max_distance=1000):
        self.num_nodes = num_nodes
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.G=nx.Graph(labelDict={})
        for i in range(self.num_nodes):
            self.G.add_node(i)
            self.G.graph['labelDict'][i] = string.ascii_letters[i]
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if i==j: continue
                self.G.add_edge(i, j, distance=random.randrange(self.min_distance, self.max_distance))

    def plot(self):
        plotter = GraphPlotter(self.G)
        plotter.plot()

G = FullyConnectedGraph(num_nodes=10)
G.plot()