from collections import deque


class DirectedAdjacencyList:
    def __init__(self, num_nodes):
        # Initialize an empty adjacency list for each node
        self.graph = {i: [] for i in range(num_nodes)}

    def add_edge(self, source, target):
        # Add a directed edge from source to target
        self.graph[source].append(target)

    def print_adjacency_list(self):
        # Print the adjacency list representation of the graph
        for node, neighbors in self.graph.items():
            print(f"Node {node} -> {neighbors}")

    def dfs(self, start):
        # Set to keep track of visited nodes
        visited = set()
        # Start DFS from the given node
        self._dfs_helper(start, visited)
        return visited

    def _dfs_helper(self, node, visited):
        # If the node hasn't been visited yet
        if node not in visited:
            # Print the current node and mark it as visited
            print(node, end=" ")
            visited.add(node)
            # Visit all the neighbors of the current node
            for neighbor in self.graph[node]:
                self._dfs_helper(neighbor, visited)

    def bfs(self, start):
        # Set to keep track of visited nodes
        visited = set()
        # Use a queue to keep track of nodes to be visited in BFS
        queue = deque([start])

        while queue:
            # Dequeue a node from the front of the queue
            node = queue.popleft()
            if node not in visited:
                # Print the current node and mark it as visited
                print(node, end=" ")
                visited.add(node)
                # Enqueue all unvisited neighbors of the current node
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)


print("DFS for DirectedAdjacencyList:")
directed_adjacency_list = DirectedAdjacencyList(5)
directed_adjacency_list.add_edge(0, 1)
directed_adjacency_list.add_edge(1, 2)
directed_adjacency_list.add_edge(2, 3)
directed_adjacency_list.add_edge(3, 4)
print("Starting DFS from node 0:")
directed_adjacency_list.dfs(0)
print()


print("BFS for DirectedAdjacencyList:")
directed_adjacency_list = DirectedAdjacencyList(5)
directed_adjacency_list.add_edge(0, 1)
directed_adjacency_list.add_edge(1, 2)
directed_adjacency_list.add_edge(2, 3)
directed_adjacency_list.add_edge(3, 4)
print("Starting BFS from node 0:")
directed_adjacency_list.bfs(0)
