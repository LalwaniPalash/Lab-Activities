import pandas as pd
import numpy as np

# a) Load a CSV file (replace 'your_file.csv' with the actual CSV file path)
df = pd.read_csv('your_file.csv')

# b) Sort the DataFrame by index in descending order
df_sorted_by_index = df.sort_index(ascending=False)

print("b) DataFrame sorted by index in descending order:")
print(df_sorted_by_index.head())

# c) Extract all rows of a column (replace 'column_name') where the values are between 50 and 80
filtered_column = df[(df['column_name'] >= 50) & (df['column_name'] <= 80)]

print("\nc) Rows where 'column_name' values are between 50 and 80:")
print(filtered_column)

# d) Create a DataFrame and calculate the mean, median, and standard deviation of a column
data = {'column1': [10, 20, 30, 40, 50]}
df_data = pd.DataFrame(data)

mean_value = df_data['column1'].mean()
median_value = df_data['column1'].median()
std_dev_value = df_data['column1'].std()

print("\nd) Mean, median, and standard deviation of 'column1':")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev_value}")

# e) Replace all negative values in a DataFrame with 0
df_no_negatives = df.applymap(lambda x: 0 if x < 0 else x)

print("\ne) DataFrame after replacing all negative values with 0:")
print(df_no_negatives.head())
