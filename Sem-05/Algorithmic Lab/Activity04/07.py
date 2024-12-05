class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Add an undirected edge between vertices u and v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def display_graph(self):
        """Display the graph as an adjacency list."""
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(map(str, self.graph[vertex]))}")

if __name__ == "__main__":
    g = Graph()

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("Graph representation (Adjacency List):")
    g.display_graph()
