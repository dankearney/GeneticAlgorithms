from  FullyConnectedGraph import *
from Solution import *

from random import shuffle
N = 5

G = FullyConnectedGraph(num_nodes = N)
solution, value = G.find_brute_force_solution()
G.highlight_solution(solution)
G.plot("Solution travels " + str(value))
# base = range(N)
# shuffle(base)
# solution = Solution(base)
# print solution

# fitness = G.measure_solution_fitness(solution)
# G.highlight_solution(solution)
# G.plot("Solution travels " + str(fitness))