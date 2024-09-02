import numpy as np
import array

array1_np = np.array([1, 2, 3, 4, 5])
array2_np = np.array([10, 20, 30, 40, 50])
result_numpy = array1_np + array2_np
print("NumPy array addition result:", result_numpy)

array1_arr = array.array('i', [1, 2, 3, 4, 5])
array2_arr = array.array('i', [10, 20, 30, 40, 50])

if len(array1_arr) != len(array2_arr):
    raise ValueError("Arrays must have the same length for element-wise addition.")

result_array = array.array('i', (a + b for a, b in zip(array1_arr, array2_arr)))
print("Array module addition result:", result_array)
