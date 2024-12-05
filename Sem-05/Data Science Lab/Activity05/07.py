import pandas as pd

# Create a DataFrame from two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
df = pd.DataFrame({'Numbers': list1, 'Letters': list2})

# Save the DataFrame to a CSV file named output.csv
df.to_csv('output.csv', index=False)

# Print the DataFrame to confirm
print(df)
