import pandas as pd
import matplotlib.pyplot as plt

# a) Create a DataFrame with columns 'Name', 'Age', 'Height', and 'Weight'
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 28, 35, 22],
    'Height': [165, 180, 175, 160, 155],
    'Weight': [55, 70, 68, 80, 50]
}
df = pd.DataFrame(data)

print("a) DataFrame:")
print(df)

# b) Filter rows where 'Age' is greater than 25 and 'Height' is less than 170
filtered_df = df[(df['Age'] > 25) & (df['Height'] < 170)]

print("\nb) Filtered DataFrame:")
print(filtered_df)

# c) Use Matplotlib to create a bar chart of the filtered rows with 'Name' on the x-axis and 'Weight' on the y-axis
plt.figure(figsize=(8, 5))
plt.bar(filtered_df['Name'], filtered_df['Weight'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Weight')
plt.title('Weight of Individuals (Age > 25 and Height < 170)')
plt.show()
