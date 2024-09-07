import numpy as np

def calculate_determinant_of_triangular(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        raise ValueError("The matrix must be square.")
    
    determinant = 1
    for i in range(rows):
        determinant *= matrix[i, i]
    
    return determinant

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
    
    is_upper = all(matrix[i, j] == 0 for i in range(n) for j in range(i) if matrix[i, j] != 0)
    is_lower = all(matrix[i, j] == 0 for i in range(n) for j in range(i + 1, n) if matrix[i, j] != 0)
    
    if is_upper or is_lower:
        determinant = calculate_determinant_of_triangular(matrix)
        print(f"The determinant of the triangular matrix is: {determinant}")
    else:
        print("The matrix is neither upper triangular nor lower triangular.")

main()
