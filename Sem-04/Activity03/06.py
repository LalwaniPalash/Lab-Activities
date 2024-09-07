import numpy as np

def create_identity_matrix(n):
    identity_matrix = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        identity_matrix[i, i] = 1
    
    return identity_matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    n = int(input("Enter the size of the identity matrix: "))
    
    if n <= 0:
        print("The size of the matrix must be a positive integer.")
        return
    
    identity_matrix = create_identity_matrix(n)
    
    print("Identity Matrix:")
    display_matrix(identity_matrix)

main()
