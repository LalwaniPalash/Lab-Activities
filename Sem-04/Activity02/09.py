import numpy as np

array_2d = np.random.randint(1, 101, size=(3, 3))

transposed_array = np.transpose(array_2d)

print("Original 3x3 array:")
print(array_2d)
print("\nTransposed 3x3 array:")
print(transposed_array)
