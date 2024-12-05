import numpy as np

# a) Extract the first row and second column from the matrix [[2, 4], [6, 8]] and print it.
matrix_a = np.array([[2, 4], [6, 8]])

first_row = matrix_a[0]
second_column = matrix_a[:, 1]

# Flatten the 2D array into a 1D array and print it.
flattened_matrix = matrix_a.flatten()

print("a) First row:", first_row)
print("Second column:", second_column)
print("Flattened array:", flattened_matrix)

# b) Calculate the dot product of [1, 2] and [3, 4] and perform element-wise addition of the two arrays.
array_b1 = np.array([1, 2])
array_b2 = np.array([3, 4])

dot_product = np.dot(array_b1, array_b2)
element_wise_addition = array_b1 + array_b2

print("\nb) Dot product:", dot_product)
print("Element-wise addition:", element_wise_addition)

# c) Create a diagonal matrix with the values [1, 2, 3].
diagonal_matrix = np.diag([1, 2, 3])

print("\nc) Diagonal matrix:")
print(diagonal_matrix)

# d) Compute the transpose of the matrix [[1, 2], [3, 4]].
matrix_d = np.array([[1, 2], [3, 4]])
transpose_matrix = matrix_d.T

print("\nd) Transpose of the matrix:")
print(transpose_matrix)

# e) Create a numpy array with values [10, 20, 30, 40, 50] and extract every alternate element.
array_e = np.array([10, 20, 30, 40, 50])
alternate_elements = array_e[::2]

print("\ne) Alternate elements from the array:", alternate_elements)
