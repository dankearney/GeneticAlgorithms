class Solution:

	def __init__(self, arr, graph):
		self.arr = arr
		self.arr
		self.graph = graph
		self.fitness = None

	def compute_fitness(self):
		self.fitness = self.graph.measure_solution_fitness(self)
		return self.fitness

	# Certain solutions produced at various points of the algorithm are invalid.
	# If a mutation or crossing-over causes a node to be visited twice
	# or a node to not be visited, we need to clean it up
	def clean(self):
		# Identify any missing nodes in current array
		difference = set(range(len(self.arr))) - set(self.arr)
		
		# No differences between the two? Great!
		if len(difference) == 0:
			return

		# If differences.. find duplicates and replace with element from difference
		seen = set([])
		for i in range(len(self.arr)):
			element = self.arr[i]
			if element in seen:
				self.arr[i] =  difference.pop()
			seen.add(element)

	def set(self, i, val):
		self.arr[i] = val

	def get(self, i):
		return self.arr[i]

	def __repr__(self):
		return str(self.arr) + ", fitness: " + str(self.compute_fitness())

	def __len__(self):
		return len(self.arr)

