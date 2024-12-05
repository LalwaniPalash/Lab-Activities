import numpy as np

# Create the matrix and vector
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, 1])

# a) Demonstrate broadcasting by adding the vector to the matrix.
result_broadcasting = matrix + vector

print("a) Broadcasting result (adding vector to matrix):")
print(result_broadcasting)

# b) Replicate the vector to match the matrix shape and add them.
replicated_vector = np.tile(vector, (3, 1))  # Replicate the vector to match the shape (3, 3)
result_replicated = matrix + replicated_vector

print("\nb) Replicated vector added to matrix:")
print(result_replicated)
