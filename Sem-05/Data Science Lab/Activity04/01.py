import numpy as np

# Given arrays
array_a = np.array([[1, 2], [3, 4], [5, 6]])
array_b = np.array([[7, 8], [9, 10], [11, 12]])

# a) Compute the element-wise sum, difference, product, and division and print the outputs
sum_result = array_a + array_b
difference_result = array_a - array_b
product_result = array_a * array_b
division_result = array_a / array_b

print("a) Element-wise operations:")
print("Sum:")
print(sum_result)
print("Difference:")
print(difference_result)
print("Product:")
print(product_result)
print("Division:")
print(division_result)

# b) Print the sum along rows and columns separately
sum_rows = np.sum(array_a, axis=1)
sum_columns = np.sum(array_a, axis=0)

print("\nb) Sum along rows and columns:")
print("Sum along rows:", sum_rows)
print("Sum along columns:", sum_columns)

# c) Perform element-wise square root and display the output
sqrt_result = np.sqrt(array_a)

print("\nc) Element-wise square root:")
print(sqrt_result)
