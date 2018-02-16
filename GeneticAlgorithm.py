from Solution import *
import random
from numpy.random import choice

class GeneticAlgorithm:

	def __init__(self, G, depth=100, num_chromosomes=100):
		self.G = G
		self.num_chromosomes = num_chromosomes
		self.depth = depth
		self.current_generation = []
		self.next_generation = []

	def run(self):
		self.generate_first_solutions()
		for i in range(self.depth):
			self.generate_next_generation()
		return self.determine_winner()

	def generate_first_solutions(self):
		for i in range(self.num_chromosomes):
			arr = range(self.G.num_nodes)
			random.shuffle(arr)
			self.current_generation.append(Solution(arr))

	def generate_next_generation(self):
		self.select_next_generation_parents()
		self.cross_over()
		self.mutate()
		self.clean()
		self.current_generation = self.next_generation
		self.next_generation = []
	
	def cross_over(self):
		pass

	def mutate(self):
		pass

	def clean(self):
		for solution in self.next_generation:
			solution.clean()

	def select_next_generation_parents(self):
		total_fitness_sum = 0
		# First, compute all of the fitnesses.
		for solution in self.current_generation:
			solution.compute_fitness(self.G)
			total_fitness_sum += solution.fitness

		# Now, sort solutions by fitness
		self.current_generation.sort(key = lambda x: x.fitness)

		# Compute the probabilities, favoring front of the list (fitter solutions)
		probabilities_not_normalized = [(self.num_chromosomes - i) for i in range(self.num_chromosomes)]
		probabilities = [float(p)/sum(probabilities_not_normalized) for p in probabilities_not_normalized]

		# Weight the next generation towards the fitter solutions
		self.next_generation = list(choice(self.current_generation, self.num_chromosomes, p=probabilities))


	def determine_winner(self):
		self.current_generation.sort(key = lambda x: x.fitness)
		return self.current_generation[0]


