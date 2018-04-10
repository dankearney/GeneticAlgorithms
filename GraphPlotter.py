import networkx as nx
import random
import matplotlib.pyplot as plt
import time
import string

class GraphPlotter:

    def __init__(self, graph):
        self.graph = graph
        self.G = nx.Graph()
        self.fitnesses = []
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(122)
        self.ax2 = self.fig.add_subplot(121)
        self.filename = self.random_filename()

    def random_filename(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) + '.pdf'

    def populate_networkx_graph_nodes(self):
        for i in range(self.graph.num_nodes):
            self.G.add_node(i, xy=self.graph.get_node_xy(i))

    def add_edges(self, solution):
        for i in range(self.graph.num_nodes):
            start = solution.get(i)
            end = solution.get((i+1)%self.graph.num_nodes)
            self.G.add_edge(start, end)

    def plot(self, solution, mutation_rate, crossover_rate, generation, num_nodes, chromosomes):
        try:

            self.fitnesses.append(solution.fitness)
            line1, = self.ax.plot(range(len(self.fitnesses)), self.fitnesses, 'r-') # Returns a tuple of line objects, thus the comma
            self.ax.set_title('Fitness: %.2f Generation: %d\n Nodes: %d  Mutation rate: %.3f\n  Crossover rate: %.3f  Chromosomes: %d'
                %(solution.fitness, generation, num_nodes, mutation_rate, crossover_rate, chromosomes))
            self.ax.set_xlabel('Iterations')
            self.ax.set_ylabel('Best Fitness')
            self.G = nx.Graph() # Little hack to clear the old graph
            self.populate_networkx_graph_nodes()
            self.add_edges(solution)
            self.ax2.clear()
            pos=nx.get_node_attributes(self.G, 'xy')
            nx.draw(self.G, pos=pos, ax=self.ax2, node_size=100, node_color='black', edge_color='orchid')
            plt.draw()
            plt.pause(0.001)

            mng = plt.get_current_fig_manager()
            mng.resize(*mng.window.maxsize())
            # mng.full_screen_toggle()
            # mng.window.showMaximized()
            plt.show(block=False)

            # Save just the portion _inside_ the second axis's boundaries
            extent = self.ax2.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())

            self.fig.savefig('figures/vis_' + str(len(self.fitnesses)) + '.pdf', bbox_inches=extent)

            # Save just the portion _inside_ the second axis's boundaries
            extent = self.ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())

            self.fig.savefig('figures/graph_' + str(len(self.fitnesses)) + '.pdf', bbox_inches='tight')

        except:
            print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
            raise