import numpy as np

array_2d = np.random.randint(1, 101, size=(3, 4))

row_sums = np.sum(array_2d, axis=1)
print("Sum of each row:")
print(row_sums)

column_maxima = np.max(array_2d, axis=0)
print("Largest element in each column:")
print(column_maxima)

print("2D Array:")
print(array_2d)
