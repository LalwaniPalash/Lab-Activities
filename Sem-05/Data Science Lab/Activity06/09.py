import pandas as pd

# a) Load a CSV file (any csv file) into a DataFrame
df = pd.read_csv('your_file.csv')

# b) Display the first five rows of the DataFrame
print(df.head())

# c) Check for missing values in the DataFrame
print(df.isnull().sum())

# d) Identify rows with more than two missing values
rows_with_missing_values = df[df.isnull().sum(axis=1) > 2]
print(rows_with_missing_values)

# e) Replace missing values with the median salary (assuming 'Salary' column exists)
median_salary = df['Salary'].median()
df['Salary'].fillna(median_salary, inplace=True)

# f) Sort the DataFrame by a column (e.g., 'Salary') in descending order
df_sorted = df.sort_values(by='Salary', ascending=False)
print(df_sorted)
