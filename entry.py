from  FullyConnectedGraph import *
from GeneticAlgorithm import *
from Solution import *

from random import shuffle
N = 50

random_nodes = [(random.random(), random.random()) for i in range(N)]

G = FullyConnectedGraph(random_nodes)

ga = GeneticAlgorithm(G, num_chromosomes = 100, depth=10000)
winner = ga.run()
