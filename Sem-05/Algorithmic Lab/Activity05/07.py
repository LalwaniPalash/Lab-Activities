class Graph:
    def __init__(self):
        """Initialize an empty graph represented by an adjacency list."""
        self.graph = {}

    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        """Perform Depth-First Search (DFS) starting from the vertex 'start'."""
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")  # Print the current node (or store it in a list if needed)

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("Depth-First Search (DFS) starting from vertex 0:")
    g.dfs(0)
