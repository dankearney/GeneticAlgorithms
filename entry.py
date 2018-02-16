from  FullyConnectedGraph import *
from GeneticAlgorithm import *

from random import shuffle
N = 9

G = FullyConnectedGraph(num_nodes = N)
ga = GeneticAlgorithm(G, num_chromosomes = 100, depth=5)
winner = ga.run()
brute_force_sol = G.find_brute_force_solution()

print "Winner", winner, winner.compute_fitness(G)
print "Brute force solution", brute_force_sol.compute_fitness(G)
G.highlight_solution(winner, 'red')
G.highlight_solution(brute_force_sol, 'blue')
G.plot(title='Brute force: ' + str(brute_force_sol.fitness) + ', Genetic: ' + str(winner.compute_fitness(G)))