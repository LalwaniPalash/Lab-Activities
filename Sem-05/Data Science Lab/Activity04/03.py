import numpy as np

# Given 2D NumPy array
array = np.array([[1, 2], [3, 4], [5, 6]])

# a) Use Boolean indexing to filter values greater than 2 and print it.
filtered_array = array[array > 2]

print("a) Values greater than 2:")
print(filtered_array)

# b) Perform integer array indexing to access specific elements and print it.
# Accessing elements at positions (0,1), (1,0), and (2,1)
indexed_elements = array[[0, 1, 2], [1, 0, 1]]

print("\nb) Accessed specific elements using integer array indexing:")
print(indexed_elements)

# c) Reshape the array into a 1D array and back into a 3x2 array and print it.
reshaped_array_1d = array.reshape(-1)
reshaped_array_3x2 = reshaped_array_1d.reshape(3, 2)

print("\nc) Reshaped to 1D and back to 3x2 array:")
print("1D array:")
print(reshaped_array_1d)
print("Back to 3x2 array:")
print(reshaped_array_3x2)
