import networkx as nx
import random
import matplotlib.pyplot as plt
import time

class GraphPlotter:

    def __init__(self, graph):
        self.graph = graph
        self.G = nx.Graph()

    def populate_networkx_graph_nodes(self):
        for i in range(self.graph.num_nodes):
            self.G.add_node(i, xy=self.graph.get_node_xy(i))

    def add_edges(self, solution, color='black'):
        for i in range(self.graph.num_nodes):
            start = solution.get(i)
            end = solution.get((i+1)%self.graph.num_nodes)
            self.G.add_edge(start, end, color=color, distance = self.graph.dist_between(start, end))

    def plot(self, title='', solution=None):
        try:
            self.G = nx.Graph()
            self.populate_networkx_graph_nodes()
            if solution != None:
                self.add_edges(solution)

            plt.clf()
            pos=nx.get_node_attributes(self.G, 'xy')

            nx.draw(self.G, pos=pos, with_labels=True)
            plt.title(title)
            print title
            plt.ion()
            plt.show()
            plt.draw()
            plt.pause(0.001)    
            plt.show(block=False)

        except:
            print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
            raise