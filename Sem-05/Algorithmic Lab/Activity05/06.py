import heapq

def prim_mst(graph):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    :param graph: 2D list (adjacency matrix) representing the weighted undirected graph.
                  graph[i][j] is the weight of the edge between vertex i and vertex j.
                  Use float('inf') to represent no direct edge between two vertices.
    :return: MST represented as a list of edges and the total weight of the MST.
    """
    n = len(graph)  # Number of vertices
    mst_edges = []  # List to store the edges in the MST
    total_weight = 0  # Total weight of the MST
    
    in_mst = [False] * n  # Boolean array to track vertices included in MST
    min_edge = [(0, 0)]  # Min-heap to store the edge with minimum weight
    edge_weights = [float('inf')] * n  # To track the minimum edge weight to each vertex
    edge_weights[0] = 0  # Start from vertex 0
    
    while min_edge:
        weight, u = heapq.heappop(min_edge)
        
        if in_mst[u]:
            continue
        
        in_mst[u] = True
        total_weight += weight
        
        if weight != 0:  # Skip the first vertex as it doesn't have a predecessor edge
            mst_edges.append((prev_u, u, weight))
        
        for v in range(n):
            if not in_mst[v] and graph[u][v] != float('inf') and graph[u][v] < edge_weights[v]:
                edge_weights[v] = graph[u][v]
                prev_u = u  # Store the previous vertex for edge reconstruction
                heapq.heappush(min_edge, (graph[u][v], v))
    
    return mst_edges, total_weight

if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    
    mst_edges, total_weight = prim_mst(graph)
    
    print("Edges in the Minimum Spanning Tree:")
    for edge in mst_edges:
        print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")
    
    print(f"\nTotal weight of the Minimum Spanning Tree: {total_weight}")
