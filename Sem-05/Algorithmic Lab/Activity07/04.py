import heapq

# Function to implement Prim's algorithm with step-by-step visualization
def prim(graph, start):
    mst = []  # Store the edges in the MST
    visited = set()  # To keep track of visited nodes
    min_heap = []  # Priority queue to select the edge with the smallest weight
    
    # Start from the given starting vertex and add its edges to the min-heap
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))
    
    print(f"Starting Prim's algorithm from vertex {start}")
    print("Initial visited set:", visited)
    
    while min_heap:
        # Extract the edge with the minimum weight
        weight, u, v = heapq.heappop(min_heap)
        
        # Check if the destination vertex is not visited (to avoid cycles)
        if v not in visited:
            # Add the edge to the MST
            mst.append((u, v, weight))
            visited.add(v)
            
            # Print the state after adding this edge
            print(f"Added edge {u} - {v} with weight {weight}")
            print("Current visited vertices:", visited)
            print("Edges considered for inclusion in MST:", min_heap)
            
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
print("\nFinal Minimum Spanning Tree (MST) edges:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
