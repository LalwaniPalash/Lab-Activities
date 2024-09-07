def is_symmetric(matrix):
    n = len(matrix)
    
    if any(len(row) != n for row in matrix):
        raise ValueError("The matrix must be square.")
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
