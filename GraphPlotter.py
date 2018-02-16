import networkx as nx
import random
import matplotlib.pyplot as plt

class GraphPlotter:

    def __init__(self, G):
        self.G = G

    def plot(self, title):
        try:
            pos = nx.kamada_kawai_layout(self.G, weight='distance')
            nx.draw_networkx_nodes(self.G, pos, node_color='cornflowerblue')
            nx.draw_networkx_labels(self.G, pos, self.G.graph['labelDict'])
            nx.draw_networkx_edges(self.G, pos, edge_color=[d['color'] if d['color'] != '' else 'aliceblue' for u,v,d in self.G.edges(data=True)])
            edge_labels = nx.get_edge_attributes(self.G,'distance')
            nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, rotate=False)
            plt.title(title)
            plt.show()
        except:
            print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
            raise
