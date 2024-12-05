import heapq

def dijkstra(graph, start, target):
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0  # Distance to the start node is 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == target:
            break
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    
    if path[-1] != start:
        return []  # No valid path found
    
    path.reverse()
    
    return path

if __name__ == "__main__":
    graph = {
        0: [(1, 7), (2, 9), (5, 14)],
        1: [(0, 7), (2, 10), (3, 15)],
        2: [(0, 9), (1, 10), (3, 11), (5, 2)],
        3: [(1, 15), (2, 11), (4, 6)],
        4: [(3, 6), (5, 9)],
        5: [(0, 14), (2, 2), (4, 9)]
    }
    
    start_node = 0
    target_node = 4
    
    shortest_path = dijkstra(graph, start_node, target_node)
    
    print(f"Shortest path from node {start_node} to node {target_node}: {shortest_path}")
