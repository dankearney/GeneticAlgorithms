from Solution import *
import random

class GeneticAlgorithm:

	# Runs a genetic algorithm on the given graph.
	# Uses num_chromosomes solutions.
	# Stops when depth iterations have happened.
	def __init__(self, graph, depth=100, num_chromosomes=100):
		self.graph = graph
		self.num_chromosomes = num_chromosomes	
		if self.num_chromosomes < 50:
			raise ArgumentException, 'Must have at least 50 chromosomes' 
		self.depth = depth
		self.current_generation = []
		self.next_generation = []

	def run(self):
		self.generate_random_solutions()
		for i in range(self.depth):
			self.step()
		return self.determine_winner()

	def generate_random_solutions(self):
		for i in range(self.num_chromosomes):
			arr = range(self.graph.num_nodes)
			random.shuffle(arr)
			self.current_generation.append(Solution(arr, self.graph))

	def step(self):
		self.select_parents()
		self.cross_over()
		self.mutate()
		self.current_generation = self.next_generation
	
	# User ordered crossover to mix parent pairs.
	def cross_over(self):
		for i in range(0, len(self.next_generation), 2):
			if random.random() < .9: 
				mom, dad = self.next_generation[i].arr, self.next_generation[i+1].arr
				self.next_generation[i]   = Solution(self.cross_merge_arr(mom, dad), self.graph)
				self.next_generation[i+1] = Solution(self.cross_merge_arr(dad, mom), self.graph)

	# Uses ordered crossover to cross two solutions.
	# Take a random chunk of the solution 1.
	# Insert that into the solution 2 at the same spot.
	# Fill in the rest of solution 2 with the same order.
	# Being careful not to duplicate entries.
	def cross_merge_arr(self, parent1, parent2):
		# First pick the elements to cross over from parent1
		crossover_point_1 = random.randrange(0, self.graph.num_nodes)
		length = self.graph.num_nodes / 2 # Cap the crossover at half the chromosome
		crossover_point_2 = random.randrange(crossover_point_1, crossover_point_1 + length)
		crossover = parent1[crossover_point_1:crossover_point_2]
		crossover_set = set(crossover) # for faster lookups
		
		# Now push the crossover into output array at the same indices
		out_arr = [None] * self.graph.num_nodes
		out_arr[crossover_point_1:crossover_point_2] = crossover

		# Fill in the rest of output array from parent2, maintaining order
		placement_index = 0
		for item in parent2:
			while placement_index < self.graph.num_nodes and out_arr[placement_index] != None:
				placement_index += 1
			if item not in crossover_set:
				out_arr[placement_index] = item
				placement_index += 1
		return out_arr

	# Mutate solutions by swapping random elements some percentage of the time.
	# Swapping maintains the solution integrity.
	def mutate(self):
		for solution in self.next_generation:
<<<<<<< HEAD
			for j in range(self.graph.num_nodes):
				if random.random() < .015: # Each chromosome has a 1
					index_a = random.randrange(0, self.graph.num_nodes)
					index_b = random.randrange(0, self.graph.num_nodes)
					val_a = solution.get(index_a)
					val_b = solution.get(index_b)
					solution.set(index_a, val_b)
					solution.set(index_b, val_a)
=======
			if random.random() < .3: 
				index_a = random.randrange(0, self.graph.num_nodes)
				index_b = random.randrange(0, self.graph.num_nodes)
				val_a = solution.get(index_a)
				val_b = solution.get(index_b)
				solution.set(index_a, val_b)
				solution.set(index_b, val_a)
>>>>>>> 686efbf057bf3b2106fc15946c9e08ad84f1302f

	# Use a "tournament select" to choose winning parents.
	# For our cases, we want to weight our next gen towards the best performers.
	# So we pick N random elements and put the best one into the next generation.
	# More efficient to pre-compute the fitnesses since we can't really get much around
	# computing N fitnesses.
	def select_parents(self):
		self.next_generation = [ self.determine_winner() ] # * int(( self.graph.num_nodes * .1))
		while len(self.next_generation) < len(self.current_generation):
			sample = random.sample(self.current_generation, self.graph.num_nodes / 10)
			self.next_generation.append(min(sample, key=lambda item: item.fitness))
		random.shuffle(self.next_generation)

	def determine_winner(self):
		for solution in self.current_generation:
			solution.compute_fitness()
		return min(self.current_generation, key=lambda item: item.fitness)


from Solution import *
import random

class GeneticAlgorithm:

	# Runs a genetic algorithm on the given graph.
	# Uses num_chromosomes solutions.
	# Stops when depth iterations have happened.
	def __init__(self, graph, depth=100, num_chromosomes=100):
		self.graph = graph
		self.num_chromosomes = num_chromosomes	
		self.depth = depth
		self.current_generation = []
		self.next_generation = []

	def run(self):
		self.generate_random_solutions()
		for i in range(self.depth):
			self.step()
		return self.determine_winner()

	def generate_random_solutions(self):
		for i in range(self.num_chromosomes):
			arr = range(self.graph.num_nodes)
			random.shuffle(arr)
			self.current_generation.append(Solution(arr, self.graph))

	def step(self):
		self.select_parents()
		self.cross_over()
		self.mutate()
		self.current_generation = self.next_generation
	
	# User ordered crossover to mix parent pairs.
	def cross_over(self):
		for i in range(0, len(self.next_generation), 2):
			if random.random() < .9:
				mom, dad = self.next_generation[i].arr, self.next_generation[i+1].arr
				self.next_generation[i]   = Solution(self.cross_merge_arr(mom, dad), self.graph)
				self.next_generation[i+1] = Solution(self.cross_merge_arr(dad, mom), self.graph)

	# Uses ordered crossover to cross two solutions.
	# Take a random chunk of the solution 1.
	# Insert that into the solution 2 at the same spot.
	# Fill in the rest of solution 2 with the same order.
	# Being careful not to duplicate entries.
	def cross_merge_arr(self, parent1, parent2):
		# First pick the elements to cross over from parent1
		crossover_points = sorted([random.randrange(0, self.graph.num_nodes) for j in range(2)])
		crossover = parent1[crossover_points[0]:crossover_points[1]]
		crossover_set = set(crossover) # for faster lookups
		
		# Now push the crossover into output array at the same indices
		out_arr = [None] * self.graph.num_nodes
		out_arr[crossover_points[0]:crossover_points[1]] = crossover

		# Fill in the rest of output array from parent2, maintaining order
		placement_index = 0
		for item in parent2:
			while placement_index < self.graph.num_nodes and out_arr[placement_index] != None:
				placement_index += 1
			if item not in crossover_set:
				out_arr[placement_index] = item
				placement_index += 1
		return out_arr

	# Mutate solutions by swapping random elements some percentage of the time.
	# Swapping maintains the solution integrity.
	def mutate(self):
		for solution in self.next_generation:
			for j in range(self.graph.num_nodes):
				if random.random() < .02: # Each gene has a chance of mutation. Value tuned by
					index_a = random.randrange(0, self.graph.num_nodes)
					index_b = random.randrange(0, self.graph.num_nodes)
					solution.swap(index_a, index_b)

	def compute_all_current_gen_fitnesses(self):
		for solution in self.current_generation:
			solution.compute_fitness()

	# Use a "tournament select" to choose winning parents.
	# For our cases, we want to weight our next gen towards the best performers.
	# So we pick N random elements and put the best one into the next generation.
	# More efficient to pre-compute the fitnesses since we can't really get much around
	# computing N fitnesses.
	def select_parents(self):
		self.next_generation = [] # self.determine_winner
		self.compute_all_current_gen_fitnesses()
		fittest = self.fittest_sol_current_gen()
		self.graph.plot(fittest, title=fittest.fitness)
		while len(self.next_generation) < len(self.current_generation):
			sample = random.sample(self.current_generation, 10)
			fittest = min(sample, key=lambda x: x.fitness)
			self.next_generation.append(fittest)

	def fittest_sol_current_gen(self):
		return min(self.current_generation, key=lambda x: x.fitness)


	def determine_winner(self):
		self.compute_all_current_gen_fitnesses()
		return self.fittest_sol_current_gen()


