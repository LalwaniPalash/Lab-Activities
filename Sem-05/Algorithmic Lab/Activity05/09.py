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

    def dfs_paths(self, start, goal, path=None):
        """
        Find all paths from start to goal using DFS.
        
        :param start: The starting vertex
        :param goal: The target vertex
        :param path: The current path (initialized to None)
        :return: List of all paths from start to goal
        """
        if path is None:
            path = []
        
        path.append(start)  # Add the current vertex to the path

        if start == goal:
            return [list(path)]
        
        paths = []
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in path:  # Avoid revisiting nodes in the current path (to avoid cycles)
                new_paths = self.dfs_paths(neighbor, goal, path)
                paths.extend(new_paths)  # Add all new paths found
        
        path.pop()  # Remove the current vertex from the path (backtrack)
        return paths

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 4)

    all_paths = g.dfs_paths(0, 4)
    
    print("All paths from 0 to 4:")
    for path in all_paths:
        print(path)
