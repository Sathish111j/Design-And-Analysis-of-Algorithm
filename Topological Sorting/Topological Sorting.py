class DirectedAdjacencyListWithWeights:
    def __init__(self, num_nodes):
        self.graph = {i: [] for i in range(num_nodes)}

    def add_edge(self, node1, node2, weight):
        self.graph[node1].append((node2, weight))

    def remove_edge(self, node1, node2):
        self.graph[node1] = [(v, w) for v, w in self.graph[node1] if v != node2]

    def print_adjacency_list(self):
        for node, neighbors in self.graph.items():
            print(f"Node {node} -> {neighbors}")

    def topological_sort(self):
        # Helper function for DFS-based topological sorting
        def dfs(node, visited, stack):
            visited[node] = True
            for neighbor, _ in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack)
            stack.append(node)

        num_nodes = len(self.graph)
        visited = [False] * num_nodes
        stack = []

        for node in range(num_nodes):
            if not visited[node]:
                dfs(node, visited, stack)

        # The stack now contains the topological sorting in reverse order
        return stack[::-1]



# Example usage:
num_nodes = 6
graph = DirectedAdjacencyListWithWeights(num_nodes)
graph.add_edge(5, 2, 1)
graph.add_edge(5, 0, 3)
graph.add_edge(4, 0, 2)
graph.add_edge(4, 1, 5)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 1, 8)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 10)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 2, 4)
graph.add_edge(0, 1,4)
graph.add_edge(1, 2,5)
graph.add_edge(2, 3,2)
graph.add_edge(3, 4,1)


topological_order = graph.topological_sort()
print("Topological Sorting Order:", topological_order)
