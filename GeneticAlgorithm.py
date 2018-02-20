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
		print 'Beginning generation: ', self.current_generation
		self.select_next_generation()
		print 'Parents ', self.next_generation
		self.cross_over()
		print 'Crossed over ', self.next_generation
		self.mutate()
		print 'Mutated ', self.next_generation
		self.current_generation = self.next_generation
	
	def cross_over(self):
		for i in range(0, len(self.next_generation), 2):

			mom, dad = self.next_generation[i].arr, self.next_generation[i+1].arr

			# First pick the elements from mom to cross over
			crossover_points = sorted([random.randrange(0, self.graph.num_nodes) for j in range(2)])
			mom_crossover = mom[crossover_points[0]:crossover_points[1]]
			
			# Now push the crossover into dad's array
			newdad = [None] * self.graph.num_nodes
			newdad[crossover_points[0]:crossover_points[1]] = mom_crossover

 			# Fill in the rest of dad's array maintaining order
 			k = 0
 			# j is the index to place the element
 			# k is the element from the old array
 			for i in range(self.graph.num_nodes):
 				item = dad[i]
 				if item in newdad:
 					k += 1
 					continue
 				else:
 					newdad[i-k] = item

			# # Now pick dad's elements to cross over
			# crossover_points = sorted([random.randrange(0, self.graph.num_nodes) for j in range(2)])
			# dad_crossover = dad[crossover_points[0]:crossover_points[1]]
			
			# # Now push the crossover into mom's array
			# newmom = [None] * self.graph.num_nodes
			# newmom[crossover_points[0]:crossover_points[1]] = dad_crossover

 		# 	# Fill in the rest of mom's array maintaining order
 		# 	for j in range(self.graph.num_nodes):
 		# 		if mom[j] not in dad_crossover:
 		# 			newmom[j] = mom[j]

 			print 'newdad: ', newdad

			self.next_generation[i] = Solution(newdad, self.graph)
			self.next_generation[i+1] = Solution(newdad, self.graph)

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
		self.next_generation = self.current_generation
		return
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


