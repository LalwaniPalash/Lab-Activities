import numpy as np

def is_upper_triangular(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(i):
            if matrix[i, j] != 0:
                return False
    
    return True

def is_lower_triangular(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(i + 1, cols):
            if matrix[i, j] != 0:
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
    
    if is_upper_triangular(matrix):
        print("The matrix is an upper triangular matrix.")
    elif is_lower_triangular(matrix):
        print("The matrix is a lower triangular matrix.")
    else:
        print("The matrix is neither upper triangular nor lower triangular.")

if __name__ == "__main__":
    main()
