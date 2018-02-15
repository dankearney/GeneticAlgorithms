from  FullyConnectedGraph import *
from Solution import *

from random import shuffle
N = 10

G = FullyConnectedGraph(num_nodes = N)
base = range(1, N)
shuffle(base)
base = [0] + base + [0]
solution = Solution(base)
print solution

G.measure_solution_fitness(solution)
G.highlight_solution(solution)
G.plot()