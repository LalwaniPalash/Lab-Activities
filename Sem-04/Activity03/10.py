import numpy as np

def is_toeplitz(matrix):
    rows, cols = matrix.shape
    
    for r in range(rows):
        value = matrix[r, 0]
        i, j = r, 0
        while i < rows and j < cols:
            if matrix[i, j] != value:
                return False
            i += 1
            j += 1
    
    for c in range(1, cols):
        value = matrix[0, c]
        i, j = 0, c
        while i < rows and j < cols:
            if matrix[i, j] != value:
                return False
            i += 1
            j += 1
    
    return True

def main():
    n = int(input("Enter the number of rows of the matrix: "))
    m = int(input("Enter the number of columns of the matrix: "))
    
    if n <= 0 or m <= 0:
        print("The number of rows and columns must be positive integers.")
        return
    
    matrix = np.zeros((n, m), dtype=int)
    
    print("Enter the matrix elements row by row:")
    for i in range(n):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").split()))
        if len(row) != m:
            print(f"Error: Row {i + 1} does not have {m} elements.")
            return
        matrix[i] = row
    
    print("The matrix you entered is:")
    print(matrix)
    
    if is_toeplitz(matrix):
        print("The matrix is a Toeplitz matrix.")
    else:
        print("The matrix is not a Toeplitz matrix.")

main()
