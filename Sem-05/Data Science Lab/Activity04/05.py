import numpy as np

# Define the arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# a) Compute their matrix product using NumPy functions and print the result matrix.
result_matrix = np.dot(a, b)

print("a) Matrix product:")
print(result_matrix)

# b) Find the determinant of result matrix and its transpose.
det_result_matrix = np.linalg.det(result_matrix)
det_transpose_result_matrix = np.linalg.det(result_matrix.T)

print("\nb) Determinant of the result matrix and its transpose:")
print("Determinant of the result matrix:", det_result_matrix)
print("Determinant of the transpose of the result matrix:", det_transpose_result_matrix)

# c) Add a scalar value (e.g., 10) to each element in result matrix.
scalar_added_matrix = result_matrix + 10

print("\nc) Result matrix after adding scalar value 10 to each element:")
print(scalar_added_matrix)
