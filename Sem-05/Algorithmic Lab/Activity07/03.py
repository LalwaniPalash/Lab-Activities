import heapq

# Function to check if the graph is connected using DFS
def is_connected(graph):
    visited = set()

    # Helper function for DFS traversal
    def dfs(node):
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from an arbitrary node (choose the first key from the graph)
    start_node = next(iter(graph))
    dfs(start_node)
    
    # If the number of visited nodes is equal to the number of nodes in the graph, it's connected
    return len(visited) == len(graph)

# Function to implement Prim's algorithm
def prim(graph, start):
    mst = []  # Store the edges in the MST
    visited = set()  # To keep track of visited nodes
    min_heap = []  # Priority queue to select the edge with the smallest weight
    
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        
        # If the destination vertex is not yet visited, add it to the MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            
            # Add all edges from the newly visited node to the heap
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, v, neighbor))
    
    return mst

# Main function to check connectivity and apply Prim's algorithm
def minimum_spanning_tree(graph, start):
    # First, check if the graph is connected
    if not is_connected(graph):
        return "The graph is disconnected, cannot apply Prim's algorithm."
    
    # If the graph is connected, apply Prim's algorithm
    mst = prim(graph, start)
    
    return mst

# Graph representation (adjacency list)
graph = {
    'A': [('B', 8), ('C', 10)],
    'B': [('A', 8), ('C', 9), ('D', 7)],
    'C': [('A', 10), ('B', 9), ('D', 5)],
    'D': [('B', 7), ('C', 5)]
}

# Running the function to check connectivity and apply Prim's algorithm
result = minimum_spanning_tree(graph, 'A')

# Output the result
if isinstance(result, str):
    print(result)
else:
    print("Minimum Spanning Tree (MST) edges:")
    for u, v, weight in result:
        print(f"{u} - {v}: {weight}")
