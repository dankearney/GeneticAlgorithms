import random
import string
from GraphPlotter import GraphPlotter
import itertools
from Solution import *
import math

class FullyConnectedGraph:

    # TODO: Build real world datasource!
    def __init__(self, nodes=[(0,0), (10, 10), (5,5), (5, 0), (10, 0)]):
        self.nodes = nodes
        self.num_nodes = len(self.nodes)
        self.plotter = GraphPlotter(self)

    def plot(self, solution, title = ''):
        self.plotter.plot(solution, title)

    def get_node_xy(self, i):
        return self.nodes[i]

    def dist_between(self, index_1, index_2):
        p1 = self.nodes[index_1]
        p2 = self.nodes[index_2]
        dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
        return dist

    def find_brute_force_solution(self):
        best_solution = None
        best_solution_value = float("inf")
        for sol_list in list(itertools.permutations(range(self.num_nodes))):
            solution = Solution(sol_list, self)
            fitness_value = self.measure_solution_fitness(solution)
            if fitness_value < best_solution_value:
                best_solution = solution
                best_solution_value = fitness_value
        return best_solution

    def __repr__(self):
        return "Nodes: " + str(self.nodes)  