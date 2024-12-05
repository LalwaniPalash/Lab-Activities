import numpy as np

# a) Given a 1D NumPy array [5, 6, 7, 8, 9]: Reverse the array using slicing and print it.
array_a = np.array([5, 6, 7, 8, 9])
reversed_array_a = array_a[::-1]

print("a) Reversed 1D array:")
print(reversed_array_a)

# b) Given a 2D numpy array [[2, 3, 4, 5], [5, 6, 7, 8], [4, 6, 8, 10]]: Extract the first two rows and the first three columns using slicing and print it.
array_b = np.array([[2, 3, 4, 5], [5, 6, 7, 8], [4, 6, 8, 10]])
sliced_array_b = array_b[:2, :3]

print("\nb) Extracted first two rows and first three columns:")
print(sliced_array_b)

# c) Create a 2D numpy array filled with random values: Extract the first two rows and the first three columns using slicing and print it.
array_c = np.random.rand(4, 4)
sliced_array_c = array_c[:2, :3]

print("\nc) Random 2D array with first two rows and first three columns:")
print(sliced_array_c)

# d) Create a 2D numpy array filled with random values: Extract all rows and alternate columns and print it.
array_d = np.random.rand(4, 4)
sliced_array_d = array_d[:, ::2]

print("\nd) Random 2D array with alternate columns:")
print(sliced_array_d)

# e) Create a 2D (4x4) numpy array filled with random values: Extract a 2x2 subarray from the top-left corner.
array_e = np.random.rand(4, 4)
subarray_e = array_e[:2, :2]

print("\ne) 2x2 subarray from the top-left corner:")
print(subarray_e)
