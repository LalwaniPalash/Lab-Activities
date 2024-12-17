import heapq

def prim(graph, start):
    # Initialize data structures
    mst = []  # Store the edges in the MST
    visited = set()  # To keep track of visited nodes
    min_heap = []  # Priority queue to select the edge with the smallest weight
    
    # Add all edges from the start node to the min-heap
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))
    
    while min_heap:
        # Extract the edge with the minimum weight
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

# Graph representation (adjacency list)
graph = {
    'A': [('B', 8), ('C', 10)],
    'B': [('A', 8), ('C', 9), ('D', 7)],
    'C': [('A', 10), ('B', 9), ('D', 5)],
    'D': [('B', 7), ('C', 5)]
}

# Running Prim's algorithm starting from vertex 'A'
mst = prim(graph, 'A')

# Output the Minimum Spanning Tree (MST) edges
print("Minimum Spanning Tree (MST) edges:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
