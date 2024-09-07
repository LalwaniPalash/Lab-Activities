from array import array
import numpy as np

numbers = [3, 5, 1, 9, 2, 8, 7, 4, 10]

arr = array('i', numbers)
even_numbers_array = array('i', [num for num in arr if num % 2 == 0])
print("Even numbers using array module:")
print(even_numbers_array.tolist())

np_array = np.array(numbers)
even_numbers_np = np_array[np_array % 2 == 0]
print("Even numbers using NumPy:")
print(even_numbers_np)
