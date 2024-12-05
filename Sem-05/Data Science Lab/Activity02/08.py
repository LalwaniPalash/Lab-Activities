# matrix_operations.py

def add_matrices(matrix1, matrix2):
    """Adds two matrices of the same dimensions."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def subtract_matrices(matrix1, matrix2):
    """Subtracts matrix2 from matrix1 (element-wise)."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    
    return result

def multiply_matrices(matrix1, matrix2):
    """Multiplies two matrices (matrix1 * matrix2)."""
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in matrix1 must be equal to number of rows in matrix2.")
    
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result
