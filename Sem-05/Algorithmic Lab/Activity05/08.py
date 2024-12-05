from collections import deque

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
        self.graph[v].append(u)  # For undirected graph, add reverse edge as well

    def bfs(self, start):
        """Perform Breadth-First Search (BFS) starting from vertex 'start'."""
        visited = set()  # Set to track visited vertices
        queue = deque([start])  # Initialize the queue with the start vertex
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("Breadth-First Search (BFS) starting from vertex 0:")
    g.bfs(0)
