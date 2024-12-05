import numpy as np

# Create the 3x3 array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# a) Extract the diagonal elements and create a diagonal matrix using these values.
diagonal_elements = np.diag(array)
diagonal_matrix = np.diag(diagonal_elements)

print("a) Diagonal matrix:")
print(diagonal_matrix)

# b) Reverse the rows and columns of the array.
reversed_array = np.flipud(np.fliplr(array))

print("\nb) Array with rows and columns reversed:")
print(reversed_array)

# c) Replace all odd numbers in the array with -1.
array_with_replaced_odds = np.where(array % 2 != 0, -1, array)

print("\nc) Array with odd numbers replaced by -1:")
print(array_with_replaced_odds)
