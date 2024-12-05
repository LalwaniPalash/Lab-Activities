import pandas as pd

# a) Load a CSV file (replace 'your_file.csv' with the actual CSV file path)
df = pd.read_csv('your_file.csv')

# b) Use .iloc[] to display the second row of the DataFrame
second_row = df.iloc[1]

print("b) Second row of the DataFrame:")
print(second_row)

# c) Drop a column from the DataFrame (replace 'column_name' with the actual column name)
df_dropped = df.drop(columns=['column_name'])

print("\nc) DataFrame after dropping a column:")
print(df_dropped.head())

# d) Display only the last 3 rows of the DataFrame
last_three_rows = df.tail(3)

print("\nd) Last 3 rows of the DataFrame:")
print(last_three_rows)

# e) Write a command to view a concise summary of the DataFrame
print("\ne) Concise summary of the DataFrame:")
print(df.info())
