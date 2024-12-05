import pandas as pd

# a) Load a CSV file (replace 'your_file.csv' with the actual CSV file path)
df = pd.read_csv('your_file.csv')

# b) Display the shape of the DataFrame
print("b) Shape of the DataFrame:")
print(df.shape)

# c) Display the data types of all columns in the DataFrame
print("\nc) Data types of all columns:")
print(df.dtypes)

# d) Check the number of missing values in each column of the DataFrame
print("\nd) Number of missing values in each column:")
print(df.isnull().sum())

# e) Drop rows with any missing values in the DataFrame
df_cleaned = df.dropna()

print("\ne) DataFrame after dropping rows with missing values:")
print(df_cleaned)
