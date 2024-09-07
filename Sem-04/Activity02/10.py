import numpy as np

matrix1 = np.random.randint(1, 11, size=(2, 2))
matrix2 = np.random.randint(1, 11, size=(2, 2))

result_matrix = np.zeros((2, 2), dtype=int)

for i in range(2):
    for j in range(2):
        result_matrix[i, j] = sum(matrix1[i, k] * matrix2[k, j] for k in range(2))

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResulting Matrix after multiplication:")
print(result_matrix)
