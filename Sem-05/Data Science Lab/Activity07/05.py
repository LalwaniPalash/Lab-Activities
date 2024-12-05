import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file containing sales data (assumed to have 'Product' and 'Quantity' columns)
df = pd.read_csv('sales_data.csv')

# Plot a bar chart of the quantities sold for each product
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Quantity'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.title('Bar Chart: Quantity Sold for Each Product')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
