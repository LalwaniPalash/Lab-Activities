import numpy as np

def is_identity_matrix(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(cols):
            if i == j and matrix[i, j] != 1:
                return False
            elif i != j and matrix[i, j] != 0:
                return False
    
    return True

def main():
    n = int(input("Enter the size of the square matrix: "))
    
    if n <= 0:
        print("The size of the matrix must be a positive integer.")
        return
    
    matrix = np.zeros((n, n), dtype=int)
    
    print("Enter the matrix elements row by row:")
    for i in range(n):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").split()))
        if len(row) != n:
            print(f"Error: Row {i + 1} does not have {n} elements.")
            return
        matrix[i] = row
    
    print("The matrix you entered is:")
    print(matrix)
    
    if is_identity_matrix(matrix):
        print("The matrix is an identity matrix.")
    else:
        print("The matrix is not an identity matrix.")

main()
