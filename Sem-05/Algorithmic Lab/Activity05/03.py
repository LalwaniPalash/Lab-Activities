import heapq  

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Add a directed edge from vertex u to vertex v with the given weight."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        """Implement Dijkstra's algorithm to find the shortest path from the source vertex."""
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        priority_queue = [(0, start)]  # (distance, vertex)
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))  # Push the neighbor into the queue
        
        return distances


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 5, 1)

    start_vertex = 0
    distances = g.dijkstra(start_vertex)

    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"Vertex {vertex}: {distance}")
