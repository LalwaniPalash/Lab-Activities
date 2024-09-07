def gaussian_elimination(A, B):
    n = len(A)
    
    for i in range(n):
        A[i].append(B[i])
    
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    break
        
        diag_element = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= diag_element
        
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n + 1):
                A[k][j] -= factor * A[i][j]
    
    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = A[i][n]
        for j in range(i + 1, n):
            X[i] -= A[i][j] * X[j]
    
    return X

A = [
    [2, 1],
    [1, 3]
]

B = [4, 7]

solution = gaussian_elimination(A, B)
print("Solution:", solution)
