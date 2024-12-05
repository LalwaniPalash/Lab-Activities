import numpy as np

# a) Create a NumPy array with integers from 0 to 8. Reshape the array into a 2x3 matrix and print the shape.
arr_a = np.arange(9).reshape(2, 3)
print("a) Reshaped Array:")
print(arr_a)
print("Shape of the array:", arr_a.shape)

# b) Create a NumPy array and initialize an array with 5 zeros and another with 5 ones.
arr_b_zeros = np.zeros(5)
arr_b_ones = np.ones(5)

# Perform slicing on the array to extract the first three elements.
arr_b_sliced = arr_b_zeros[:3]

# Multiply all elements of the array by 5 and print the output.
arr_b_zeros *= 5
print("\nb) Zero array after slicing and multiplication:")
print(arr_b_zeros)

# c) Create a 2x3 NumPy array filled with random values. Find the minimum value in the array.
arr_c = np.random.rand(2, 3)
min_value = np.min(arr_c)

# Add a scalar value 10 to each element of the array and print the array.
arr_c += 10
print("\nc) Random array:")
print(arr_c)
print("Minimum value in the array:", min_value)

# d) Create a 3x3 identity matrix using numpy. Compute the sum of elements along rows and columns.
arr_d = np.eye(3)

sum_rows = np.sum(arr_d, axis=1)
sum_columns = np.sum(arr_d, axis=0)

print("\nd) Identity Matrix:")
print(arr_d)
print("Sum along rows:", sum_rows)
print("Sum along columns:", sum_columns)

# e) Create a numpy array of 10 random integers between 1 and 100. Sort the array in ascending order.
arr_e = np.random.randint(1, 101, 10)
arr_e_sorted = np.sort(arr_e)

print("\ne) Random integers array:")
print("Original array:", arr_e)
print("Sorted array:", arr_e_sorted)

