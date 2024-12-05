import numpy as np

# a) Create a 3x3 matrix using numpy array and print it. Find the eigenvalues and eigenvectors of the 3x3 matrix and print the output.
matrix_a = np.random.rand(3, 3)

eigenvalues, eigenvectors = np.linalg.eig(matrix_a)

print("a) 3x3 matrix:")
print(matrix_a)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# b) Create two 1D arrays using numpy and calculate the outer product of two vectors. Print both the vector and their outer product.
vector_b1 = np.array([1, 2])
vector_b2 = np.array([3, 4])

outer_product = np.outer(vector_b1, vector_b2)

print("\nb) Vectors:")
print("Vector 1:", vector_b1)
print("Vector 2:", vector_b2)
print("Outer product:")
print(outer_product)

# c) Create a 3D array using numpy and slice a subarray from it.
array_c = np.random.randint(1, 10, size=(3, 3, 3))

subarray_c = array_c[1, :, :]

print("\nc) 3D array:")
print(array_c)
print("Sliced subarray from the 3D array:")
print(subarray_c)
