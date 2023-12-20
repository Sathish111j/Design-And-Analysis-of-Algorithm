class DirectedAdjacencyListWithWeights:
    def __init__(self, num_nodes):
        # Initialize an empty adjacency list for each node
        self.graph = {i: [] for i in range(num_nodes)}

    def add_edge(self, source, target, weight):
        # Add a directed edge from source to target with given weight
        self.graph[source].append((target, weight))

    def print_adjacency_list(self):
        # Print the adjacency list representation of the graph
        for node, neighbors in self.graph.items():
            print(f"Node {node} -> {neighbors}")

    def bellman_ford(self, source):
        # Initialize distances: set distance to all vertices as INFINITE
        # and distance to the source node as 0
        distances = [float("inf")] * len(self.graph)
        distances[source] = 0

        # Relax all edges |V| - 1 times (where |V| is the number of vertices)
        for _ in range(len(self.graph) - 1):
            for node in self.graph:
                for neighbor, weight in self.graph[node]:
                    # If the distance to the neighbor can be minimized by passing through the node
                    # then update the distance
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight

        # Check for negative-weight cycles in the graph
        # If we can still update the distance to a neighbor even after |V| - 1 iterations,
        # it means the graph contains a negative cycle
        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    print("Graph contains a negative-weight cycle")
                    return None

        # Return the shortest distances from source to all other vertices
        return distances

# Test the Bellman-Ford implementation
graph = DirectedAdjacencyListWithWeights(5)
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(3, 2, 5)
graph.add_edge(3, 1, 1)
graph.add_edge(4, 3, -3)

# Compute the shortest distances from vertex 0 to all other vertices
shortest_distances = graph.bellman_ford(0)

print(shortest_distances)
