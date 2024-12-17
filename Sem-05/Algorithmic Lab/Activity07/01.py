# Kruskal's Algorithm to find the Minimum Spanning Tree (MST)

# Helper functions for Disjoint Set (Union-Find)

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

# Kruskal's algorithm implementation
def kruskal(vertices, edges):
    # Sort edges based on weight
    edges.sort(key=lambda edge: edge[2])

    parent = {v: v for v in vertices}  # parent of each vertex
    rank = {v: 0 for v in vertices}    # rank of each vertex
    mst = []

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)

    return mst

# Graph vertices and edges
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('B', 'D', 4),
    ('C', 'D', 5),
    ('C', 'E', 6),
    ('D', 'E', 7)
]

# Find MST using Kruskal's algorithm
mst = kruskal(vertices, edges)

# Output the MST edges
print("Minimum Spanning Tree (MST) edges:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
