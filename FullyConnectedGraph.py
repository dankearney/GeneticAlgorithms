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
                self.G.add_edge(i, j, distance=random.randrange(self.min_distance, self.max_distance), highlighted= False)

    def plot(self):
        plotter = GraphPlotter(self.G)
        plotter.plot()

    def nodes(self):
        return self.G.nodes

    def edges(self):
        return self.G.edges

    def connected_edges(self, node_index):
        return self.G.edges(node_index, data=False)

    def dist_between(self, node_index_a, node_index_b):
        return self.G[node_index_a][node_index_b]['distance']

    def measure_solution_fitness(self, solution):
        total_dist = 0
        for i in range(1, len(solution)):
            dist = self.dist_between(solution.get(i-1), solution.get(i))
            total_dist += dist
        return total_dist

    def set_highlighted(self, node_index_a, node_index_b):
        self.G[node_index_a][node_index_b]['highlighted'] = True

    def highlight_solution(self, solution):
        for i in range(1, len(solution)):
            a = solution.get(i)
            b = solution.get(i-1)
            self.set_highlighted(a, b)


    def __repr__(self):
        return "Nodes: " + str(self.nodes()) + "\r\nEdges: " + str(self.edges())