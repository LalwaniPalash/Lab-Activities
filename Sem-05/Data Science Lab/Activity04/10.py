import numpy as np

# Create a 3x3 array using np.arange()
array = np.arange(9).reshape(3, 3)

print("Original 3x3 array:")
print(array)

# a) Reshape the array into a 1D array and split it into three equal parts.
array_1d = array.flatten()
split_array = np.split(array_1d, 3)

print("\na) Reshaped to 1D and split into three equal parts:")
print(split_array)

# b) Stack the split arrays vertically and horizontally using np.vstack and np.hstack.
vstack_result = np.vstack(split_array)
hstack_result = np.hstack(split_array)

print("\nb) Stacked arrays vertically and horizontally:")
print("Vertical stacking:")
print(vstack_result)
print("Horizontal stacking:")
print(hstack_result)
