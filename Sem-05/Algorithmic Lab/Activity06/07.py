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

def display_results(distances):
    print("Shortest distances from the source vertex:")
    for vertex, distance in distances.items():
        if distance == float('inf'):
            print(f"Vertex {vertex}: No path")
        else:
            print(f"Vertex {vertex}: {distance}")

if __name__ == "__main__":
    vertices, edges, source = get_user_input()
    
    distances = bellman_ford(vertices, edges, source)
    
    if distances:
        display_results(distances)
