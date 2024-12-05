import heapq

def dijkstra(graph, source):
    V = len(graph)
    
    dist = [float('inf')] * V
    dist[source] = 0  # Distance to the source is 0
    
    priority_queue = [(0, source)]  # (distance, vertex)
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if current_dist > dist[u]:
            continue
        
        for v in range(V):
            if graph[u][v] != float('inf') and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                heapq.heappush(priority_queue, (dist[v], v))
    
    return dist

if __name__ == "__main__":
    graph = [
        [0, 7, 9, float('inf'), float('inf'), float('inf')],
        [7, 0, 10, 15, float('inf'), float('inf')],
        [9, 10, 0, 11, float('inf'), 2],
        [float('inf'), 15, 11, 0, 6, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0, 9],
        [float('inf'), float('inf'), 2, float('inf'), 9, 0]
    ]
    
    source = 0
    
    shortest_distances = dijkstra(graph, source)
    
    print(f"Shortest distances from vertex {source}:")
    for vertex, distance in enumerate(shortest_distances):
        print(f"Vertex {vertex}: {distance}")
