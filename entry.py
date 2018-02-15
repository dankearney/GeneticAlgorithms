from  FullyConnectedGraph import *
from Solution import *

from random import shuffle
N = 4

G = FullyConnectedGraph(num_nodes = N)
base = range(1, N)
shuffle(base)
base = [0] + base + [0]
solution = Solution(base)
print solution

fitness = G.measure_solution_fitness(solution)
G.highlight_solution(solution)
G.plot("Solution travels " + str(fitness))