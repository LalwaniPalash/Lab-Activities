import array
import numpy as np

python_list = [1, 2, 3, 4, 5]
print("Standard Python List:")
print("Type:", type(python_list))
print("Contents:", python_list)
print("Size (length):", len(python_list))
print("Memory size (in bytes) of each element:", python_list.__sizeof__())
print()

array_module = array.array('i', [1, 2, 3, 4, 5])
print("Array using `array` module:")
print("Type:", type(array_module))
print("Contents:", array_module)
print("Size (length):", len(array_module))
print("Memory size (in bytes) of each element:", array_module.itemsize)
print()

numpy_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:")
print("Type:", type(numpy_array))
print("Contents:", numpy_array)
print("Size (length):", len(numpy_array))
print("Memory size (in bytes) of each element:", numpy_array.itemsize)
print()

print("Comparing Differences:")

print("\n1. Flexibility of Data Types:")
print("Python list can store elements of different types:", [1, 2.5, 'hello', True])
print("Array module stores elements of a single type, e.g., 'i' for integers:", array_module)
print("NumPy array can store elements of a single type, and the type is specified upon creation:", numpy_array)

import time
start_time = time.time()
for _ in range(1000000):
    python_list.append(10)
python_list_time = time.time() - start_time
print("\n2. Performance (Speed) - Python list append time:", python_list_time, "seconds")

start_time = time.time()
for _ in range(1000000):
    array_module.append(10)
array_module_time = time.time() - start_time
print("Array module append time:", array_module_time, "seconds")

start_time = time.time()
for _ in range(1000000):
    numpy_array = np.append(numpy_array, 10)
numpy_array_time = time.time() - start_time
print("NumPy array append time:", numpy_array_time, "seconds")

print("\n3. Memory Efficiency:")
print("Memory size of Python list (in bytes) for 5 elements:", python_list.__sizeof__())
print("Memory size of array module (in bytes) for 5 elements:", array_module.__sizeof__())
print("Memory size of NumPy array (in bytes) for 5 elements:", numpy_array.nbytes)
