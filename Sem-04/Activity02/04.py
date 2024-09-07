import numpy as np
from array import array

numbers = [3, 5, 1, 9, 2, 8, 7]

arr = array('i', numbers)

max_value_array = max(arr)
min_value_array = min(arr)

print("Using array module:")
print("Maximum value:", max_value_array)
print("Minimum value:", min_value_array)

np_array = np.array(numbers)

max_value_np = np.max(np_array)
min_value_np = np.min(np_array)

print("\nUsing NumPy:")
print("Maximum value:", max_value_np)
print("Minimum value:", min_value_np)
