import numpy as np

# a) Initialize a NumPy array using random values, and display its type and shape. Access its elements individually and print the outputs.
array_a = np.random.rand(3, 3)

print("a) Array:")
print(array_a)
print("Type of array:", type(array_a))
print("Shape of array:", array_a.shape)

# Accessing individual elements
print("First element (0,0):", array_a[0, 0])
print("Second element (0,1):", array_a[0, 1])
print("Element in the second row, first column (1,0):", array_a[1, 0])

# b) Create an array of 20 evenly spaced values between 0 and 1 using NumPy’s built-in function.
array_b = np.linspace(0, 1, 20)

# Create a 3x3 array filled with random values
array_b_random = np.random.rand(3, 3)

print("\nb) 20 evenly spaced values between 0 and 1:")
print(array_b)
print("3x3 Random array:")
print(array_b_random)

# c) Using NumPy, create the following arrays and demonstrate the respective operations:
# a) Create a 3x3 array of all zeros and a 2x2 array of ones and print it.
array_c_zeros = np.zeros((3, 3))
array_c_ones = np.ones((2, 2))

print("\nc) Arrays of zeros and ones:")
print("3x3 Array of zeros:")
print(array_c_zeros)
print("2x2 Array of ones:")
print(array_c_ones)

# b) Create a 3x3 identity matrix and print it.
array_identity = np.eye(3)

print("\nb) 3x3 Identity Matrix:")
print(array_identity)

# c) Create a matrix with random integers in a specified range (50-100) and print it.
array_random_ints = np.random.randint(50, 101, size=(3, 3))

print("\nc) Matrix with random integers between 50 and 100:")
print(array_random_ints)
