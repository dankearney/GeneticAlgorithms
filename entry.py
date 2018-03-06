from  FullyConnectedGraph import *
from GeneticAlgorithm import *
from Solution import *

N = 50

random_nodes = [(random.random(), random.random()) for i in range(N)]

G = FullyConnectedGraph(random_nodes)

ga = GeneticAlgorithm(G, num_chromosomes = 500, depth=100000, mutation_rate = .2, crossover_rate=.75)
winner = ga.run()
