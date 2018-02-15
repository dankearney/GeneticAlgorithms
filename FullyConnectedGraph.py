import networkx as nx
import random
import string
from GraphPlotter import GraphPlotter
import itertools
from Solution import *

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

    def plot(self, title = ''):
        plotter = GraphPlotter(self.G)
        plotter.plot(title)

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
        for i in range(0, len(solution)):
            dist = self.dist_between(solution.get(i), solution.get((i+1) % len(solution)))
            total_dist += dist
        return total_dist

    def set_highlighted(self, node_index_a, node_index_b):
        self.G[node_index_a][node_index_b]['highlighted'] = True

    def highlight_solution(self, solution):
        for i in range(0, len(solution)):
            a = solution.get(i)
            b = solution.get((i+1)%len(solution))
            self.set_highlighted(a, b)

    def find_brute_force_solution(self):
        best_solution = None
        best_solution_value = float("inf")
        for sol_list in list(itertools.permutations(range(self.num_nodes))):
            solution = Solution(sol_list)
            fitness_value = self.measure_solution_fitness(solution)
            if fitness_value < best_solution_value:
                best_solution = solution
                best_solution_value = fitness_value
        return best_solution, best_solution_value

    def __repr__(self):
        return "Nodes: " + str(self.nodes()) + "\r\nEdges: " + str(self.edges())