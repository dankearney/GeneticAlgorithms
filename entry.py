from  FullyConnectedGraph import *
from GeneticAlgorithm import *
from Solution import *

from random import shuffle
N = 50

random_nodes = [(random.random(), random.random()) for i in range(N)]

G = FullyConnectedGraph(random_nodes)

ga = GeneticAlgorithm(G, num_chromosomes = 1000, depth=10)
winner = ga.run()

# G.plot(solution=solution)
# winner = ga.run()
# brute_force_sol = G.find_brute_force_solution()
# print brute_force_sol
G.plot(solution=winner)


# print "Winner", winner, winner.compute_fitness(G)
# print "Brute force solution", brute_force_sol.compute_fitness(G)

# G.plot(title='Brute force: ' + str(brute_force_sol.fitness) + ', Genetic: ' + str(winner.compute_fitness(G)))