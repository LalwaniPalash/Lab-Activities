import numpy as np

# Create a 4x4 array using np.arange()
array = np.arange(16).reshape(4, 4)

print("Original 4x4 array:")
print(array)

# a) Split the array into two halves vertically and horizontally.
split_vertical = np.vsplit(array, 2)  # Split vertically
split_horizontal = np.hsplit(array, 2)  # Split horizontally

print("\na) Split array:")
print("Vertical split:")
print(split_vertical)
print("Horizontal split:")
print(split_horizontal)

# b) Concatenate the resulting arrays back together.
concatenated_vertical = np.vstack(split_vertical)  # Concatenate vertically
concatenated_horizontal = np.hstack(split_horizontal)  # Concatenate horizontally

print("\nb) Concatenated arrays:")
print("Vertical concatenation:")
print(concatenated_vertical)
print("Horizontal concatenation:")
print(concatenated_horizontal)

# c) Flatten the array into 1D and reshape it back to its original shape.
flattened_array = array.flatten()  # Flatten the array
reshaped_array = flattened_array.reshape(4, 4)  # Reshape back to original shape

print("\nc) Flattened and reshaped array:")
print("Flattened array:")
print(flattened_array)
print("Reshaped back to 4x4:")
print(reshaped_array)
