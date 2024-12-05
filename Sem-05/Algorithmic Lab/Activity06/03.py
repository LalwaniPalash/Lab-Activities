import heapq

def read_graph_from_file(file_name):
    """
    Reads a weighted graph from a file and returns it as an adjacency list.
    
    Assumes the file contains:
    - The number of vertices V on the first line.
    - Subsequent lines with edges in the format: u v weight
    """
    graph = {}
    with open(file_name, 'r') as file:
        V = int(file.readline().strip())  # Number of vertices
        for i in range(V):
            graph[i] = []
        
        for line in file:
            u, v, weight = map(int, line.strip().split())
            graph[u].append((v, weight))
            graph[v].append((u, weight))  # For undirected graphs
    return graph

def dijkstra(graph, start):
    """
    Implements Dijkstra's Algorithm to find the shortest paths from the start node.
    
    Args:
    - graph: The graph represented as an adjacency list.
    - start: The source vertex.
    
    Returns:
    - A tuple (distances, previous_nodes) where:
      - distances: A dictionary with shortest distances from the source to all nodes.
      - previous_nodes: A dictionary for path reconstruction.
    """
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, target):
    """
    Reconstructs the shortest path from start to target using the previous_nodes dictionary.
    """
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    
    if path[-1] == start:
        path.reverse()
    else:
        return []  # No path found
    
    return path

if __name__ == "__main__":
    file_name = 'graph.txt'  # Replace with the path to your graph file
    
    graph = read_graph_from_file(file_name)
    
    start_node = int(input("Enter the source node: "))
    target_node = int(input("Enter the target node: "))
    
    distances, previous_nodes = dijkstra(graph, start_node)
    
    print(f"Shortest distances from node {start_node}:")
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")
    
    shortest_path = reconstruct_path(previous_nodes, start_node, target_node)
    if shortest_path:
        print(f"Shortest path from node {start_node} to node {target_node}: {shortest_path}")
    else:
        print(f"No path found from node {start_node} to node {target_node}")
