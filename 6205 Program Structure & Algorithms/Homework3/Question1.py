import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([(7,6), (6,5), (5,2), (8,4), (5,1), (8,3)])

pos = nx.spring_layout(G, k=1.0, seed=42)

plt.figure(figsize=(10,8))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="black", node_size=2000)
plt.savefig("graph.png")
plt.show()


