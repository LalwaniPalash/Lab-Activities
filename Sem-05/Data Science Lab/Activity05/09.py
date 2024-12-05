import pandas as pd

# a) Load a CSV file (replace 'your_file.csv' with the actual CSV file path)
df = pd.read_csv('your_file.csv')

# b) Sort the DataFrame by a column (replace 'column_name' with the actual column name)
df_sorted = df.sort_values(by='column_name')

print("b) Sorted DataFrame:")
print(df_sorted.head())

# c) Remove duplicate rows from the DataFrame
df_no_duplicates = df.drop_duplicates()

print("\nc) DataFrame after removing duplicate rows:")
print(df_no_duplicates.head())

# d) Shuffle the rows of the DataFrame
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("\nd) Shuffled DataFrame:")
print(df_shuffled.head())

# e) Count the total number of rows in the DataFrame
total_rows = df.shape[0]

print("\ne) Total number of rows in the DataFrame:")
print(total_rows)
