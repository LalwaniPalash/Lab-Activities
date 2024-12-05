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

    def dfs(self, vertex, visited=None):
        """Perform DFS starting from vertex, and print visited vertices."""
        if visited is None:
            visited = set()  # Initialize visited set if not provided
        
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    
    print("DFS starting from vertex 0:")
    g.dfs(0)
