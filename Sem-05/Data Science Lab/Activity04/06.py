import numpy as np

# Create a 2D array and a 1D vector
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, 1])

# a) Add the vector to each row of the matrix using broadcasting
result_row_broadcasting = matrix + vector

print("a) Add vector to each row using broadcasting:")
print(result_row_broadcasting)

# b) Add the vector to each column of the matrix using reshaping
result_column_broadcasting = matrix + vector.reshape(1, -1)

print("\nb) Add vector to each column using reshaping:")
print(result_column_broadcasting)

# c) Compute the element-wise square and logarithm (base 10) of the matrix values
square_matrix = np.square(matrix)
log_matrix = np.log10(matrix)

print("\nc) Element-wise square and logarithm (base 10) of the matrix values:")
print("Element-wise square:")
print(square_matrix)
print("Element-wise logarithm (base 10):")
print(log_matrix)
