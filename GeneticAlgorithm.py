from Solution import *
import random

class GeneticAlgorithm:

	def __init__(self, graph, depth=100, num_chromosomes=100):
		self.graph = graph
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
			arr = range(self.graph.num_nodes)
			random.shuffle(arr)
			self.current_generation.append(Solution(arr, self.graph))

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
			solution.compute_fitness()
			total_fitness_sum += solution.fitness

		# Now, sort solutions by fitness
		self.current_generation.sort(key = lambda x: x.fitness)
		self.next_generation = []

		while len(self.next_generation) < len(self.current_generation):
			self.next_generation.append(self.weighted_select(self.current_generation))

	def weighted_select(self, arr):
		favor = .05

		if len(arr) < 1/favor:
			return random.choice(arr)

		front = arr[0:int(len(arr) * favor) ]
		back = arr[int(len(arr)* favor) :]

		# 50/50, it's in the top favor%
		coinflip = random.random()
		if coinflip < .5:
			return random.choice(front)
		
		# Otherwise, 50/50 it's in the top favor% of the bottom 90%
		else:
			return self.weighted_select(back)

	def determine_winner(self):
		self.current_generation.sort(key = lambda x: x.fitness)
		return self.current_generation[0]


