from  FullyConnectedGraph import *
from GeneticAlgorithm import *
from Solution import *

from random import shuffle
<<<<<<< HEAD
N = 50
=======
N = 150
>>>>>>> 686efbf057bf3b2106fc15946c9e08ad84f1302f

random_nodes = [(random.random(), random.random()) for i in range(N)]

G = FullyConnectedGraph(random_nodes)

ga = GeneticAlgorithm(G, num_chromosomes = 500, depth=10000)
winner = ga.run()
