class GraphPlotter

    def __init__(self, G):
        self.G = G

    def plot(self):
        try:
            pos = nx.kamada_kawai_layout(G, weight='distance')
            nx.draw_networkx_nodes(G, pos, node_color='cornflowerblue')
            nx.draw_networkx_labels(G, pos, labelDict)
            nx.draw_networkx_edges(G, pos, edge_color='gray')
            edge_labels = nx.get_edge_attributes(G,'distance')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, rotate=False)
            plt.show()
        except:
            print "Warning! Plotting failed. You will need a window manager like Ximg if running on Windows Ubuntu."
            raise
