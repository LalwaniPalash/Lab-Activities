import numpy as np

def multiply_diagonal_matrices(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        raise ValueError("Both matrices must have the same dimensions")
    
    rows, cols = matrix1.shape
    
    result_matrix = np.zeros((rows, cols), dtype=int)
    
    for i in range(rows):
        result_matrix[i, i] = matrix1[i, i] * matrix2[i, i]
    
    return result_matrix

def main():
    n = int(input("Enter the size of the diagonal matrices: "))
    
    if n <= 0:
        print("The size of the matrix must be a positive integer.")
        return
    
    matrix1 = np.zeros((n, n), dtype=int)
    matrix2 = np.zeros((n, n), dtype=int)
    
    print("Enter the elements of the first diagonal matrix (space-separated values):")
    for i in range(n):
        matrix1[i, i] = int(input(f"Enter element at position ({i}, {i}): "))
    
    print("Enter the elements of the second diagonal matrix (space-separated values):")
    for i in range(n):
        matrix2[i, i] = int(input(f"Enter element at position ({i}, {i}): "))
    
    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)
    
    result_matrix = multiply_diagonal_matrices(matrix1, matrix2)
    
    print("The product of the two diagonal matrices is:")
    print(result_matrix)

if __name__ == "__main__":
    main()
