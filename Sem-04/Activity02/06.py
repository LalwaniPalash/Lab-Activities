import numpy as np

array_2d = np.random.randint(1, 31, size=(4, 4))

element = array_2d[1, 2]
print("Element at the second row, third column:", element)

array_2d[0, 0] = 0

print("Modified 2D array:")
print(array_2d)
