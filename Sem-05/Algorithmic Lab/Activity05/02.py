class DirectedGraph:
    def __init__(self, vertices):
        """Initialize the graph with a given number of vertices."""
        self.vertices = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]  # Create an adjacency matrix

    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v."""
        if u >= self.vertices or v >= self.vertices:
            print("Invalid vertices!")
            return
        self.matrix[u][v] = 1  # Set the edge from u to v

    def display_graph(self):
        """Display the adjacency matrix representing the graph."""
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(row)


if __name__ == "__main__":
    g = DirectedGraph(4)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(0, 2)
    
    g.display_graph()
