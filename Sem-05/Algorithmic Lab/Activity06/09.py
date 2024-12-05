import heapq

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

def dijkstra(vertices, edges, source):
    graph = {vertex: [] for vertex in vertices}
    for u, v, weight in edges:
        graph[u].append((v, weight))
    
    distances = {vertex: float('inf') for vertex in vertices}
    predecessors = {vertex: None for vertex in vertices}
    distances[source] = 0
    pq = [(0, source)]  # (distance, vertex)
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
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

vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 6),
    ('A', 'D', 7),
    ('B', 'C', 5),
    ('A', 'C', 4),
    ('C', 'D', -2),
    ('D', 'B', -5)
]

source = 'A'

print("Running Bellman-Ford Algorithm...")
distances_bf, predecessors_bf = bellman_ford(vertices, edges, source)
if distances_bf and predecessors_bf:
    display_results(distances_bf, predecessors_bf, source)

print("\nRunning Dijkstra's Algorithm...")
distances_dijkstra, predecessors_dijkstra = dijkstra(vertices, edges, source)
display_results(distances_dijkstra, predecessors_dijkstra, source)
