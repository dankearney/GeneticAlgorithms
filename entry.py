from  FullyConnectedGraph import *
from Solution import *

N = 10

G = FullyConnectedGraph(num_nodes = N)
base = range(N)
base.append(0)
solution = Solution(base)

print G.measure_solution_fitness(solution)
G.plot()