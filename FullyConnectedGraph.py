from GraphPlotter import GraphPlotter
from Solution import *
import math

# A class that describes a fully connected graph.
# Nodes cannot be added or deleted.
# There is no need for explicit edges because they are implied.
class FullyConnectedGraph:

    # Nodes must be a list of (x,y) coordinate tuples.
    def __init__(self, nodes):
        self.nodes = nodes
        self.num_nodes = len(self.nodes)
        self.plotter = GraphPlotter(self)

    # Plot the solution using NetworkX
    def plot(self, solution, mutation_rate, crossover_rate, generation, chromosomes):
        self.plotter.plot(solution, mutation_rate, crossover_rate, generation, self.num_nodes, chromosomes)

    # Get the x,y coordinates of a node
    def get_node_xy(self, i):
        return self.nodes[i]

    # Computed the Euclidean distance between ndoes
    def dist_between(self, index_1, index_2):
        p1 = self.nodes[index_1]
        p2 = self.nodes[index_2]
        dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
        return dist

    def __repr__(self):
        return "Nodes: " + str(self.nodes)  