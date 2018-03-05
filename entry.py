from  FullyConnectedGraph import *
from GeneticAlgorithm import *
from Solution import *

N = 100

random_nodes = [(random.random(), random.random()) for i in range(N)]

G = FullyConnectedGraph(random_nodes)

ga = GeneticAlgorithm(G, num_chromosomes = 500, depth=10000)
winner = ga.run()
