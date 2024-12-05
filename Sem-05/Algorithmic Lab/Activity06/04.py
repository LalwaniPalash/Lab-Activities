def bellman_ford(vertices, edges, source):
    distances = {vertex: float('inf') for vertex in vertices}
    distances[source] = 0
    
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None
    
    return distances

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D']
    
    edges = [
        ('A', 'B', 1),
        ('B', 'C', 3),
        ('A', 'C', 4),
        ('C', 'D', 2),
        ('D', 'B', -5)
    ]
    
    source = 'A'
    
    distances = bellman_ford(vertices, edges, source)
    
    if distances:
        print(f"Shortest distances from vertex {source}:")
        for vertex in vertices:
            print(f"{vertex}: {distances[vertex]}")
