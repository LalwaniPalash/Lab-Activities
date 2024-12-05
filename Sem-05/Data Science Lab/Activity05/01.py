import pandas as pd

# a) Load a CSV file (replace 'your_file.csv' with the actual CSV file path)
df = pd.read_csv('your_file.csv')

# b) Display the first 10 rows of the DataFrame
print("b) First 10 rows of the DataFrame:")
print(df.head(10))

# c) Replace all missing values (NaN) in the DataFrame with 0 and display the final dataframe
df_filled = df.fillna(0)

print("\nc) DataFrame after replacing missing values with 0:")
print(df_filled)
