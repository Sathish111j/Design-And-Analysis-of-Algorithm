import heapq


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

    def dijkstra(self, source):
        # Initialize distances: set distance to all vertices as INFINITE
        # and distance to the source node as 0
        distances = [float("inf")] * len(self.graph)
        distances[source] = 0

        # Priority queue to select the vertex with the minimum distance value.
        # Initialized with the source vertex and its distance (0).
        priority_queue = [(0, source)]

        while priority_queue:
            # Get the vertex with the minimum distance from the priority queue
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # If the current distance is larger than the stored distance for the vertex, skip this vertex
            # This step ensures that vertices are processed once (the first time they are removed from the queue).
            if current_distance > distances[current_vertex]:
                continue

            # Update distances for all neighbors of the current vertex
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # If we find a shorter path to the neighbor through the current_vertex, update the distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Add the neighbor to the priority queue for further processing
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Return the shortest distances from source to all other vertices
        return distances


# Test Dijkstra's algorithm
graph = DirectedAdjacencyListWithWeights(7)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 2, 4)
graph.add_edge(4, 5, 4)
graph.add_edge(0, 6, 4)
# Compute the shortest distances from vertex 0 to all other vertices using Dijkstra's algorithm
shortest_distances_from_0 = graph.dijkstra(0)
print(shortest_distances_from_0)
