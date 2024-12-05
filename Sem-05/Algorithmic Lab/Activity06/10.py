def bellman_ford(vertices, edges, source):
    distances = {vertex: float('inf') for vertex in vertices}
    predecessors = {vertex: None for vertex in vertices}
    distances[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u

    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None, None
    
    return distances, predecessors

def reconstruct_path(predecessors, destination):
    path = []
    current = destination
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    return path

def display_results(distances, predecessors, source):
    print(f"Shortest paths from the source vertex '{source}':")
    for vertex in distances:
        if distances[vertex] == float('inf'):
            print(f"Vertex {vertex}: No path")
        else:
            path = reconstruct_path(predecessors, vertex)
            print(f"Vertex {vertex}: {' -> '.join(path)} with distance {distances[vertex]}")

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'E', 3),
    ('D', 'E', -1)
]

source = 'A'

distances_bf, predecessors_bf = bellman_ford(vertices, edges, source)
if distances_bf and predecessors_bf:
    display_results(distances_bf, predecessors_bf, source)
