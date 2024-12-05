class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Add an undirected edge between vertices u and v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited):
        """Depth First Search (DFS) to visit all reachable vertices."""
        visited.add(vertex)
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def is_connected(self):
        """Check if the graph is connected using DFS."""
        if not self.graph:
            return True  # If the graph is empty, it is considered trivially connected

        visited = set()
        start_vertex = next(iter(self.graph))  # Get the first vertex
        self.dfs(start_vertex, visited)

        return len(visited) == len(self.graph)

if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    if g.is_connected():
        print("The graph is connected.")
    else:
        print("The graph is not connected.")
    
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(2, 3)

    if g2.is_connected():
        print("The second graph is connected.")
    else:
        print("The second graph is not connected.")
