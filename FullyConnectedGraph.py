import random
import string
from GraphPlotter import GraphPlotter
import itertools
from Solution import *

class FullyConnectedGraph:

    # Realized a major issue.
    # A graph where each node is roughly the same distance from every other node is not a difficult problem to solve.
    # Any random path is about as good as any other path.
    # So, 

    # TODO: Build real world datasource!
    def __init__(self, nodes=[(0,0), (10, 10), (5,5), (5, 0), (10, 0)]):
        self.nodes = nodes
        self.num_nodes = len(self.nodes)

    def plot(self, title = ''):
        plotter = GraphPlotter(self.G)
        plotter.plot(title)

    def nodes(self):
        return self.G.nodes

    def dist_between(self, index_1, index_2):
        return ((self.nodes[index_1][0] - self.nodes[index_2][0])**2 + (self.nodes[index_1][1] - self.nodes[index_2][1])**2)**.5

    def measure_solution_fitness(self, solution):
        total_dist = 0
        for i in range(0, len(solution)):
            dist = self.dist_between(solution.get(i), solution.get((i+1) % len(solution)))
            total_dist += dist
        return total_dist

    def find_brute_force_solution(self):
        best_solution = None
        best_solution_value = float("inf")
        for sol_list in list(itertools.permutations(range(self.num_nodes))):
            solution = Solution(sol_list)
            fitness_value = self.measure_solution_fitness(solution)
            if fitness_value < best_solution_value:
                best_solution = solution
                best_solution_value = fitness_value
        return best_solution

    def __repr__(self):
        return "Nodes: " + str(self.nodes()) + "\r\nEdges: " + str(self.edges())