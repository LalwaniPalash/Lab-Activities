import numpy as np
import array
import math

array_np = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_np = np.mean(array_np)
median_np = np.median(array_np)
std_dev_np = np.std(array_np)

print("NumPy mean:", mean_np)
print("NumPy median:", median_np)
print("NumPy standard deviation:", std_dev_np)

array_arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
list_arr = list(array_arr)

mean_arr = sum(list_arr) / len(list_arr)

sorted_list = sorted(list_arr)
n = len(sorted_list)
if n % 2 == 1:
    median_arr = sorted_list[n // 2]
else:
    median_arr = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

variance = sum((x - mean_arr) ** 2 for x in list_arr) / len(list_arr)
std_dev_arr = math.sqrt(variance)

print("Array module mean:", mean_arr)
print("Array module median:", median_arr)
print("Array module standard deviation:", std_dev_arr)
