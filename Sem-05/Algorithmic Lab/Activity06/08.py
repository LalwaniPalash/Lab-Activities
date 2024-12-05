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

def get_user_input():
    num_vertices = int(input("Enter the number of vertices: "))
    
    vertices = []
    for i in range(num_vertices):
        vertex = input(f"Enter name for vertex {i+1}: ")
        vertices.append(vertex)
    
    num_edges = int(input("Enter the number of edges: "))
    
    edges = []
    for i in range(num_edges):
        u, v, weight = input(f"Enter edge {i+1} (format: u v weight): ").split()
        u, v, weight = u.strip(), v.strip(), int(weight)
        edges.append((u, v, weight))
    
    source = input("Enter the source vertex: ").strip()
    
    return vertices, edges, source

def display_results(distances, predecessors, source):
    print(f"Shortest paths from the source vertex '{source}':")
    for vertex in distances:
        if distances[vertex] == float('inf'):
            print(f"Vertex {vertex}: No path")
        else:
            path = reconstruct_path(predecessors, vertex)
            print(f"Vertex {vertex}: {' -> '.join(path)} with distance {distances[vertex]}")

if __name__ == "__main__":
    vertices, edges, source = get_user_input()
    
    distances, predecessors = bellman_ford(vertices, edges, source)
    
    if distances and predecessors:
        display_results(distances, predecessors, source)
