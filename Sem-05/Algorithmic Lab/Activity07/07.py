import heapq

# Disjoint Set (Union-Find) Helper Functions for Kruskal's Algorithm
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])
        return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        # Union by rank
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Kruskal's Algorithm
def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])
    
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    
    mst = []
    
    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)
    
    return mst

# Prim's Algorithm
def prim(graph, start):
    mst = []
    visited = set()
    min_heap = []
    
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, v, neighbor))
    
    return mst

# Function to read graph from a file
def read_graph_from_file(filename):
    graph = {}
    edges = []
    
    with open(filename, 'r') as f:
        # Read number of vertices (first line)
        num_vertices = int(f.readline().strip())
        
        # Initialize graph
        for i in range(num_vertices):
            graph[chr(65 + i)] = []  # Creates vertices A, B, C, ..., based on number of vertices
        
        # Read edges (remaining lines)
        for line in f:
            u, v, weight = line.strip().split()
            weight = int(weight)
            edges.append((u, v, weight))
            graph[u].append((v, weight))
            graph[v].append((u, weight))  # Since it's an undirected graph
    
    return graph, edges

# Function to calculate the total weight of the MST
def calculate_mst_weight(mst):
    total_weight = sum(weight for _, _, weight in mst)
    return total_weight

# Main function to apply both algorithms and compare outputs
def main():
    # Read graph from file
    filename = 'graph.txt'  # Change this to your file name
    graph, edges = read_graph_from_file(filename)
    
    # Get vertices from the graph
    vertices = list(graph.keys())
    
    # Apply Kruskal's algorithm
    print("Kruskal's Algorithm - Minimum Spanning Tree:")
    mst_kruskal = kruskal(vertices, edges)
    for u, v, weight in mst_kruskal:
        print(f"{u} - {v}: {weight}")
    total_weight_kruskal = calculate_mst_weight(mst_kruskal)
    print(f"Total weight of MST from Kruskal's algorithm: {total_weight_kruskal}\n")
    
    # Apply Prim's algorithm (starting from vertex 'A')
    print("Prim's Algorithm - Minimum Spanning Tree:")
    mst_prim = prim(graph, 'A')
    for u, v, weight in mst_prim:
        print(f"{u} - {v}: {weight}")
    total_weight_prim = calculate_mst_weight(mst_prim)
    print(f"Total weight of MST from Prim's algorithm: {total_weight_prim}")
    
    # Compare the total weights
    if total_weight_kruskal == total_weight_prim:
        print("\nThe MSTs are the same, and both algorithms give the same total weight!")
    else:
        print("\nThe MSTs are different, and the total weights are not the same.")

# Run the main function
if __name__ == "__main__":
    main()
