from collections import deque

class Graph:
    def __init__(self):
        """Initialize an empty graph represented by an adjacency list."""
        self.graph = {}

    def add_edge(self, u, v):
        """Add an edge between vertex u and vertex v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since this is an undirected graph

    def bfs_shortest_path(self, start):
        """
        Find the shortest path from the start vertex to all other vertices using BFS.

        :param start: The starting vertex
        :return: A tuple containing the distance dictionary and the parent dictionary
        """
        distance = {vertex: float('inf') for vertex in self.graph}
        distance[start] = 0  # Distance to the start vertex is 0
        
        parent = {vertex: None for vertex in self.graph}

        queue = deque([start])

        while queue:
            current = queue.popleft()

            for neighbor in self.graph[current]:
                if distance[neighbor] == float('inf'):
                    distance[neighbor] = distance[current] + 1
                    parent[neighbor] = current
                    queue.append(neighbor)

        return distance, parent

    def reconstruct_path(self, start, goal, parent):
        """Reconstruct the path from start to goal."""
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent[current]
        
        return path[::-1] if path[-1] == start else []

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 4)

    start_vertex = 0
    distance, parent = g.bfs_shortest_path(start_vertex)

    print(f"Distances from vertex {start_vertex}:")
    for vertex, dist in distance.items():
        print(f"Vertex {vertex}: {dist}")

    goal_vertex = 4
    path = g.reconstruct_path(start_vertex, goal_vertex, parent)
    
    print(f"Shortest path from {start_vertex} to {goal_vertex}: {path}")
