import numpy as np

# Given numpy array
array = np.array([[1, 2], [3, 4], [5, 6]])

# a) Compute the mean, median, and standard deviation of all elements.
mean_value = np.mean(array)
median_value = np.median(array)
std_dev_value = np.std(array)

print("a) Mean, median, and standard deviation of all elements:")
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev_value)

# b) Calculate the cumulative sum and cumulative product along both axes.
cumulative_sum_axis0 = np.cumsum(array, axis=0)
cumulative_sum_axis1 = np.cumsum(array, axis=1)

cumulative_prod_axis0 = np.cumprod(array, axis=0)
cumulative_prod_axis1 = np.cumprod(array, axis=1)

print("\nb) Cumulative sum and cumulative product along both axes:")
print("Cumulative sum along axis 0 (columns):")
print(cumulative_sum_axis0)
print("Cumulative sum along axis 1 (rows):")
print(cumulative_sum_axis1)
print("Cumulative product along axis 0 (columns):")
print(cumulative_prod_axis0)
print("Cumulative product along axis 1 (rows):")
print(cumulative_prod_axis1)

# c) Find the correlation coefficient between the columns.
correlation_matrix = np.corrcoef(array.T)  # Transpose for column correlation
print("\nc) Correlation coefficient between the columns:")
print(correlation_matrix)

# d) Transpose the array and explain the difference in shape.
transposed_array = array.T

print("\nd) Transpose of the array:")
print(transposed_array)
print("Shape of the original array:", array.shape)
print("Shape of the transposed array:", transposed_array.shape)
