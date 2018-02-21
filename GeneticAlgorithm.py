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
			winner = self.determine_winner()
			self.graph.plot(winner, title=str(winner.fitness))
		return self.determine_winner()

	def generate_first_solutions(self):
		for i in range(self.num_chromosomes):
			arr = range(self.graph.num_nodes)
			random.shuffle(arr)
			self.current_generation.append(Solution(arr, self.graph))

	def generate_next_generation(self):
		# print 'Beginning generation: ', self.current_generation
		self.select_next_generation()
		# print 'Parents ', self.next_generation
		self.cross_over()
		# print 'Crossed over ', self.next_generation
		self.mutate()
		# print 'Mutated ', self.next_generation
		self.current_generation = self.next_generation
	
	def cross_over(self):
		for i in range(0, len(self.next_generation), 2):
			mom, dad = self.next_generation[i].arr, self.next_generation[i+1].arr
			self.next_generation[i]   = Solution(self.cross_merge_arr(mom, dad), self.graph)
			self.next_generation[i+1] = Solution(self.cross_merge_arr(dad, mom), self.graph)

	def cross_merge_arr(self, parent1, parent2):
		# First pick the elements to cross over from parent1
		crossover_points = sorted([random.randrange(0, self.graph.num_nodes) for j in range(2)])
		crossover = parent1[crossover_points[0]:crossover_points[1]]
		
		# Now push the crossover into output array at the same indices
		out_arr = [None] * self.graph.num_nodes
		out_arr[crossover_points[0]:crossover_points[1]] = crossover

		# Fill in the rest of output array from parent2, maintaining order
		placement_index = 0
		for item in parent2:
			while placement_index < self.graph.num_nodes and out_arr[placement_index] != None:
				placement_index += 1
			if item not in crossover:
				out_arr[placement_index] = item
				placement_index += 1
		return out_arr


	def mutate(self):
		for solution in self.next_generation:
			if random.random() < .10: # Mutate 10% of the time
				index_a = random.randrange(0, self.graph.num_nodes)
				index_b = random.randrange(0, self.graph.num_nodes)
				val_a = solution.get(index_a)
				val_b = solution.get(index_b)
				solution.set(index_a, val_b)
				solution.set(index_b, val_a)

	def select_next_generation(self):
		self.next_generation = [self.determine_winner()]
		while len(self.next_generation) < len(self.current_generation):
			sample = [random.choice(self.current_generation) for i in range(10)]
			sample.sort(key = lambda x: x.compute_fitness())
			self.next_generation.append(sample[0])

	def determine_winner(self):
		[solution.compute_fitness() for solution in self.current_generation]
		self.current_generation.sort(key = lambda x: x.fitness)
		return self.current_generation[0]


