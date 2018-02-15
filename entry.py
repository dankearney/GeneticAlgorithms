from  FullyConnectedGraph import *
from Solution import *

from random import shuffle
N = 7

G = FullyConnectedGraph(num_nodes = N)
base = range(N)
shuffle(base)
solution = Solution(base)
print solution

fitness = G.measure_solution_fitness(solution)
G.highlight_solution(solution)
G.plot("Solution travels " + str(fitness))