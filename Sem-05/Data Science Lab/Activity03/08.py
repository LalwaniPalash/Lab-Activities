import numpy as np

# a) Create a 5x5 matrix using numpy with 1 on the border and 0 inside and print it.
matrix_a = np.ones((5, 5))
matrix_a[1:-1, 1:-1] = 0

print("a) 5x5 matrix with 1 on the border and 0 inside:")
print(matrix_a)

# b) Using numpy array stack two arrays [1, 2] and [3, 4] vertically and print the output.
array_b1 = np.array([1, 2])
array_b2 = np.array([3, 4])

stacked_arrays = np.vstack((array_b1, array_b2))

print("\nb) Stacked arrays vertically:")
print(stacked_arrays)

# c) Generate a 3x3 matrix and fill with random values using numpy and calculate its rank. Print out the matrix and the rank.
matrix_c = np.random.rand(3, 3)

rank_c = np.linalg.matrix_rank(matrix_c)

print("\nc) Random 3x3 matrix:")
print(matrix_c)
print("Rank of the matrix:", rank_c)

