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
		self.select_next_generation()
		self.cross_over()
		self.mutate()
		self.current_generation = self.next_generation
	
	def cross_over(self):
		for i in range(0, len(self.next_generation), 2):
			if random.random() > 1: continue
			mom = self.next_generation[i]
			dad = self.next_generation[i+1]
			newmom = Solution([-1 for i in range(self.graph.num_nodes)], self.graph)
			newdad = Solution([-1 for i in range(self.graph.num_nodes)], self.graph)
			crossover_point_start = random.randrange(0, self.graph.num_nodes)
			crossover_point_end = random.randrange(crossover_point_start, self.graph.num_nodes)
			for j in range(crossover_point_start, crossover_point_end):
				newmom.set(j, mom.get(j))
				newdad.set(j, dad.get(j))

			momslice = set(newmom.arr[crossover_point_start:crossover_point_end])
			dadslice = set(newdad.arr[crossover_point_start:crossover_point_end])

			for k in range(self.graph.num_nodes):
				if mom.get(k) not in momslice:
					newmom.set(k, mom.get(k))
				if dad.get(k) not in dadslice:
					newdad.set(k, dad.get(k))
			self.next_generation[i] = newmom
			self.next_generation[i+1] = newdad

	def mutate(self):
		for solution in self.next_generation:
			if random.random() < .02: # Mutate 10% of the time
				index_a = random.randrange(0, self.graph.num_nodes)
				index_b = random.randrange(0, self.graph.num_nodes)
				val_a = solution.get(index_a)
				val_b = solution.get(index_b)
				solution.set(index_a, val_b)
				solution.set(index_b, val_a)


	def select_next_generation(self):
		self.next_generation = [self.determine_winner()]
		print self.next_generation[0].fitness
		while len(self.next_generation) < len(self.current_generation):
			sample = [random.choice(self.current_generation) for i in range(10)]
			sample.sort(key = lambda x: x.compute_fitness())
			self.next_generation.append(sample[0])

	def determine_winner(self):
		[solution.compute_fitness() for solution in self.current_generation]
		self.current_generation.sort(key = lambda x: x.fitness)
		return self.current_generation[0]


