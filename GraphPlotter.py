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

    def add_edges(self, solution):
        for i in range(self.graph.num_nodes):
            start = solution.get(i)
            end = solution.get((i+1)%self.graph.num_nodes)
            self.G.add_edge(start, end)

    def plot(self, solution, title=''):
        try:

            print title
            self.G = nx.Graph() # Little hack to clear the old graph
            self.populate_networkx_graph_nodes()
            self.add_edges(solution)
            plt.clf()
            pos=nx.get_node_attributes(self.G, 'xy')
            nx.draw(self.G, pos=pos, node_size=200, node_color='black', edge_color='orchid')

            plt.ion()
            plt.gca().set_title("Title x")
            plt.show()
            plt.draw()
            plt.pause(0.001)    
            plt.show(block=False)

        except:
            print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
            raise