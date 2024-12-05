import pandas as pd

# a) Create a DataFrame with columns 'Name', 'Age', and 'Salary' using a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'Salary': 50000},
    {'Name': 'Bob', 'Age': 30, 'Salary': 60000},
    {'Name': 'Charlie', 'Age': 35, 'Salary': 70000},
    {'Name': 'David', 'Age': 28, 'Salary': 55000},
]

df = pd.DataFrame(data)

# b) Add a new column 'Tax', where each value is 10% of the salary
df['Tax'] = df['Salary'] * 0.10

print("b) DataFrame after adding 'Tax' column:")
print(df)

# c) Sort the DataFrame by 'Age' in ascending order
df_sorted = df.sort_values(by='Age', ascending=True)

print("\nc) DataFrame sorted by 'Age' in ascending order:")
print(df_sorted)

# d) Drop any rows with missing values
df_cleaned = df.dropna()

print("\nd) DataFrame after dropping rows with missing values:")
print(df_cleaned)
