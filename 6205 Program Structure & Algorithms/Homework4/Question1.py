import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Graph represented as an adjacency list
graph = {
    'A': {'B': 3, 'D': 5},
    'B': {},
    'C': {'B': -3},
    'D': {'C': 2}
}


def dijkstra(graph, start):
    # Distance dictionary, initialized to infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to explore the minimum distance node first
    queue = [(0, start)]  # (distance, node)

    while queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(queue)

        # If the current distance is greater than the already found distance, skip
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Example usage
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest paths from node {start_node}:")
for node, distance in shortest_paths.items():
    print(f"Distance to {node}: {distance}")

# Create a graph object using NetworkX
G = nx.DiGraph()

# Add nodes and edges from the adjacency list
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Set custom positions for nodes to arrange them neatly
pos = {
    'A': (0, 1),
    'B': (1, 1),
    'C': (1, 0),
    'D': (0, 0)
}

plt.figure(figsize=(6, 4))

# Draw the graph with node labels and edge weights
nx.draw(G, pos, with_labels=True, node_color='white', node_size=3000, font_size=15, font_weight='bold', arrows=True,
        edgecolors='black')

# Get edge labels and draw them in red
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_weight='bold', font_color='red')

# Show the plot
plt.title('Graph Representation with Weights', fontsize=18, fontweight='bold')
plt.axis('off')  # Hide axes for better presentation
plt.show()