import pandas as pd
import numpy as np

# a) Read a CSV file and create a DataFrame with some missing values (replace 'your_file.csv' with your actual file)
df = pd.read_csv('your_file.csv')

# b) Replace missing values with the mean for numeric columns and 'Unknown' for non-numeric columns
df_filled = df.apply(lambda col: col.fillna(col.mean()) if col.dtype in [np.int64, np.float64] else col.fillna('Unknown'), axis=0)

print("b) DataFrame after replacing missing values:")
print(df_filled.head())

# c) Drop rows where more than 2 columns have missing values
df_cleaned = df.dropna(thresh=len(df.columns) - 2)

print("\nc) DataFrame after dropping rows where more than 2 columns have missing values:")
print(df_cleaned.head())

# d) Verify the changes using the .isnull() method
print("\nd) Verify missing values using .isnull():")
print(df_filled.isnull().sum())
