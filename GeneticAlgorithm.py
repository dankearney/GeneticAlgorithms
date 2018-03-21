from Solution import *
import random

class GeneticAlgorithm:

	# Runs a genetic algorithm on the given graph.
	# Terminates after depth iterations.
	# Plots the solution at each step.
	def __init__(self, graph, depth=100, num_chromosomes=100, mutation_rate = 0, crossover_rate = 0):
		self.graph = graph
		self.mutation_rate = mutation_rate
		self.crossover_rate = crossover_rate
		self.num_chromosomes = num_chromosomes	
		self.depth = depth
		self.generation = 0
		self.current_generation = []
		self.next_generation = []

	# The main entry point to run the algorithm.
	def run(self):
		self.generate_random_chromosomes()	# Chromosomes are created at random.
		for self.generation in range(self.depth):	
			self.select_next_generation()	# Next generation is selected from the fittest of the current gen.
			self.cross_over()				# Pairs of the next generation are crossed over.
			self.mutate()					# Individuals in the next generation are mutated.
			self.current_generation = self.next_generation
		return self.determine_winner()

	# Create random solutions to seed the algorithm.
	def generate_random_chromosomes(self):
		for i in range(self.num_chromosomes):
			arr = range(self.graph.num_nodes)	# Begin with the solution 0, 1, 2 .. N-1
			random.shuffle(arr)					# Shake it up to make a random solution
			self.current_generation.append(Solution(arr, self.graph))
	
	# Use ordered crossover to mix parent pairs, at the crossover_rate rate
	def cross_over(self):
		for i in range(0, self.num_chromosomes, 2):		# Iterate in pairs
			if random.random() < self.crossover_rate:	# Ensure that the crossover_rate is honored4

				# First, make a copy of the two parents, 'mom' and 'dad'
				mom, dad = self.next_generation[i].arr[:], self.next_generation[i+1].arr[:]			

				# Now, merge some of mom's solution into dad's solution, and vice versa
				mom_crossed_over = self.cross_merge_arr(mom, dad)
				dad_crossed_over = self.cross_merge_arr(dad, mom)

				# Replace the old chromosomes with the crossed ones
				self.next_generation[i]   = Solution(mom_crossed_over, self.graph)
				self.next_generation[i+1] = Solution(dad_crossed_over, self.graph)	

	# Uses ordered crossover to cross two arrays.
	def cross_merge_arr(self, parent1, parent2):

		# First choose two random indices in parent1 to select the crossover section.
		crossover_points = sorted(random.sample(parent1, 2))
		
		# Extract that section of parent1 and store it in a hashset for quick lookups
		crossover = parent1[crossover_points[0]:crossover_points[1]]
		crossover_set = set(crossover) 								
		
		# Now push the crossover into an empty output array at the same indices
		out_arr = [None] * self.graph.num_nodes
		out_arr[crossover_points[0]:crossover_points[1]] = crossover

		# Fill in the rest of output array from parent2, maintaining parent2's order.
		# Iterate over parent2's nodes.
		# Attempt to insert each node into the output array. 
		# If the slot is empty, AND the node isn't in the crossover set, insert into output array.
		# Otherwise, try to place it in the next slot.
		placement_index = 0
		for item in parent2:
			while placement_index < self.graph.num_nodes and out_arr[placement_index] != None:
				placement_index += 1
			if item not in crossover_set:
				out_arr[placement_index] = item
				placement_index += 1
		return out_arr

	# Mutate chromosomes by two swapping random elements at the mutation rate.
	# Swapping maintains the solution integrity (ensuring no node is visited twice or not visited).
	def mutate(self):
		for solution in self.next_generation:
			if random.random() < self.mutation_rate: # Each chromosome has a chance of mutation. Value tuned manually
				index_a = random.randrange(0, self.graph.num_nodes)
				index_b = random.randrange(0, self.graph.num_nodes)
				solution.swap(index_a, index_b)

	# Computes all of the fitnesses.
	def compute_all_current_gen_fitnesses(self):
		for solution in self.current_generation:
			solution.compute_fitness()

	# Use a "tournament select" to choose winning parents.
	# For our cases, we want to weight our next gen towards the best performers, but not too aggressively,
	# Because we need to maintain diversity. 
	# So we pick 4 random elements and put the best one into the next generation.
	def select_next_generation(self):
		self.next_generation = []

		# Compute all of the fitnesses so we can run tournaments.
		self.compute_all_current_gen_fitnesses()
		fittest = self.fittest_sol_current_gen()
		self.graph.plot(fittest, self.mutation_rate, self.crossover_rate, self.generation, self.num_chromosomes)
		while len(self.next_generation) < len(self.current_generation):
			sample = random.sample(self.current_generation, 4)	# Choose four random solutions.
			fittest = min(sample, key=lambda x: x.fitness)		# Shortest path is fittest solution
			self.next_generation.append(fittest)			

	# Finds fittest solution in current generation.
	# Assumes fitnesses were pre-computed
	def fittest_sol_current_gen(self):
		return min(self.current_generation, key=lambda x: x.fitness)

	# Determines fittest solution by computing all fitnesses.
	def determine_winner(self):
		self.compute_all_current_gen_fitnesses()
		return self.fittest_sol_current_gen()


