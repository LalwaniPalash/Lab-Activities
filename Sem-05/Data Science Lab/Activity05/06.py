import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# a) Load a CSV file (replace 'your_file.csv' with the actual CSV file path)
df = pd.read_csv('your_file.csv')

# b) Rename a column 'old_name' to 'new_name' in the DataFrame
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# c) Convert missing values (NaN) in a particular column (e.g., 'column_name') to the column's mean
df['column_name'] = df['column_name'].fillna(df['column_name'].mean())

# d) Replace all zeros in the DataFrame with NaN
df.replace(0, np.nan, inplace=True)

# e) Split the DataFrame into training (75%) and testing (25%) sets
train_df, test_df = train_test_split(df, test_size=0.25, random_state=42)

# Print the outputs for each operation
print("b) Renamed column:")
print(df.head())

print("\nc) Converted missing values in 'column_name' to mean:")
print(df['column_name'].head())

print("\nd) DataFrame after replacing zeros with NaN:")
print(df.head())

print("\ne) Training and testing sets:")
print("Training set:")
print(train_df.head())
print("Testing set:")
print(test_df.head())
