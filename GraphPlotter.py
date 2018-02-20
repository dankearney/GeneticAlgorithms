import networkx as nx
import random
import matplotlib.pyplot as plt

class GraphPlotter:

    def __init__(self, graph):
        self.graph = graph
        self.G = nx.Graph()
        self.populate_networkx_graph_nodes()

    def populate_networkx_graph_nodes(self):
        for i in range(self.graph.num_nodes):
            self.G.add_node(i, xy=self.graph.get_node_xy(i))

    def add_edges(self, solution, color='black'):
        for i in range(self.graph.num_nodes):
            start = solution.get(i)
            end = solution.get((i+1)%self.graph.num_nodes)
            self.G.add_edge(start, end, color=color, distance = self.graph.dist_between(start, end))

    def plot(self, title=''):
        try:
            pos=nx.get_node_attributes(self.G, 'xy')
            nx.draw_networkx_nodes(self.G, pos, node_color='cornflowerblue')
            labelDict = {}
            for i in range(self.graph.num_nodes):
                labelDict[i] = i
            nx.draw_networkx_labels(self.G, pos, labelDict)
            nx.draw_networkx_edges(self.G, pos)
            # edge_labels = nx.get_edge_attributes(self.G, 'distance')
            # nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, rotate=False)
            plt.title(title)
            plt.show()
        except:
            print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
            raise