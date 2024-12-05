class WeightedGraph:
    def __init__(self):
        """Initialize an empty graph represented as an adjacency list."""
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Add a directed edge from vertex u to vertex v with the specified weight."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))  # Add directed edge u -> v

    def add_undirected_edge(self, u, v, weight):
        """Add an undirected edge between vertex u and vertex v with the specified weight."""
        self.add_edge(u, v, weight)
        self.add_edge(v, u, weight)

    def display_graph(self):
        """Display the adjacency list representation of the graph."""
        for vertex in self.graph:
            print(f"Vertex {vertex}: ", end="")
            for neighbor, weight in self.graph[vertex]:
                print(f"({neighbor}, {weight})", end=" ")
            print()  # New line after each vertex


if __name__ == "__main__":
    g = WeightedGraph()

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 4)

    g.add_undirected_edge(4, 5, 6)

    print("Graph Representation (Adjacency List with Weights):")
    g.display_graph()
