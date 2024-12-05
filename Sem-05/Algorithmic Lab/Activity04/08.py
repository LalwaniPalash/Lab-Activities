def count_vertices_and_edges(adj_matrix):
    num_vertices = len(adj_matrix)
    
    num_edges = 0
    for i in range(num_vertices):
        for j in range(i, num_vertices):  # Only check upper triangular part (i <= j)
            if adj_matrix[i][j] == 1:
                num_edges += 1
    
    return num_vertices, num_edges

if __name__ == "__main__":
    adj_matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    
    vertices, edges = count_vertices_and_edges(adj_matrix)
    
    print(f"Number of vertices: {vertices}")
    print(f"Number of edges: {edges}")
