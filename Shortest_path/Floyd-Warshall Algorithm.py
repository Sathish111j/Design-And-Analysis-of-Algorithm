class DirectedAdjacencyMatrixWithWeights:
    def __init__(self, num_nodes):
        # Initialize the adjacency matrix with infinite distances for all pairs
        # and 0 for diagonal (distance from a vertex to itself)
        self.matrix = [[float("inf")] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes):
            self.matrix[i][i] = 0

    def add_edge(self, source, target, weight):
        # Set the weight for the directed edge from source to target
        self.matrix[source][target] = weight

    def print_adjacency_matrix(self):
        # Print the adjacency matrix representation of the graph
        for row in self.matrix:
            print(row)

    def floyd_warshall(self):
        # Initialize the distance matrix with the adjacency matrix values
        distances = [row.copy() for row in self.matrix]

        num_vertices = len(self.matrix)

        # For each intermediate vertex k
        for k in range(num_vertices):
            # For every vertex pair (i, j)
            for i in range(num_vertices):
                for j in range(num_vertices):
                    # If the distance through vertex k is shorter than the direct path from i to j,
                    # then update the distance from i to j with the shorter path
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        # Return the matrix of shortest distances between every pair of vertices
        return distances

# Test the Floyd-Warshall implementation
graph = DirectedAdjacencyMatrixWithWeights(5)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 3, 10)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 1, -2)

# Compute the shortest paths between all pairs of vertices using Floyd-Warshall algorithm
shortest_path_matrix = graph.floyd_warshall()
print(shortest_path_matrix)
