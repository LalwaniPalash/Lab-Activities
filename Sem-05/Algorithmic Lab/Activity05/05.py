from collections import deque

class Graph:
    def __init__(self, directed=False):
        """Initialize a graph with directed or undirected edges."""
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if not self.directed:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)

    def bfs(self, start):
        """Perform Breadth-First Search (BFS) starting from the vertex 'start'."""
        visited = set()
        queue = deque([start])
        visited.add(start)
        traversal_order = []

        while queue:
            vertex = queue.popleft()
            traversal_order.append(vertex)

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order


if __name__ == "__main__":
    directed_graph = Graph(directed=True)
    directed_graph.add_edge(0, 1)
    directed_graph.add_edge(0, 2)
    directed_graph.add_edge(1, 3)
    directed_graph.add_edge(2, 3)
    directed_graph.add_edge(3, 4)

    print("Directed Graph BFS Traversal:")
    directed_bfs_order = directed_graph.bfs(0)
    print("BFS Traversal Order:", directed_bfs_order)

    undirected_graph = Graph(directed=False)
    undirected_graph.add_edge(0, 1)
    undirected_graph.add_edge(0, 2)
    undirected_graph.add_edge(1, 3)
    undirected_graph.add_edge(2, 3)
    undirected_graph.add_edge(3, 4)

    print("\nUndirected Graph BFS Traversal:")
    undirected_bfs_order = undirected_graph.bfs(0)
    print("BFS Traversal Order:", undirected_bfs_order)
