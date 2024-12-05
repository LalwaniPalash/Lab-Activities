import numpy as np

# a) Generate a 4x4 numpy array with random values and compute the mean of each row, then replace all even numbers with -1 and print the array.
array_a = np.random.randint(1, 100, size=(4, 4))
row_means = np.mean(array_a, axis=1)

# Replace even numbers with -1
array_a[array_a % 2 == 0] = -1

print("a) Row means:", row_means)
print("Array with even numbers replaced by -1:")
print(array_a)

# b) Create a 3x3 numpy array filled with random numbers, replace all odd numbers with zero, and print it.
array_b = np.random.randint(1, 100, size=(3, 3))

# Replace odd numbers with zero
array_b[array_b % 2 != 0] = 0

# Perform broadcasting to add [1, 2, 3] to each row of the 3x3 matrix
array_b += np.array([1, 2, 3])

print("\nb) Array with odd numbers replaced by 0 and broadcasting added:")
print(array_b)

# c) Create two 2x2 matrices using numpy and fill them with random values using random module, then perform matrix multiplication and print the output.
matrix_c1 = np.random.randint(1, 10, size=(2, 2))
matrix_c2 = np.random.randint(1, 10, size=(2, 2))

# Matrix multiplication
result_c = np.dot(matrix_c1, matrix_c2)

print("\nc) Matrix multiplication result:")
print("Matrix 1:")
print(matrix_c1)
print("Matrix 2:")
print(matrix_c2)
print("Result of multiplication:")
print(result_c)
