def vertex_degrees(adj_matrix):
    """Calculate the degree of each vertex in the graph represented by an adjacency matrix."""
    degrees = []
    
    for i in range(len(adj_matrix)):
        degree = sum(adj_matrix[i])  # Sum of row i gives the degree of vertex i
        degrees.append(degree)
    
    return degrees

if __name__ == "__main__":
    adj_matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    
    degrees = vertex_degrees(adj_matrix)
    
    for vertex, degree in enumerate(degrees):
        print(f"Degree of vertex {vertex}: {degree}")
