import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# a) Read a CSV file containing sales data (product and quantity sold).
# Assuming the CSV has columns 'Product' and 'Quantity'
df = pd.read_csv('sales_data.csv')

# Plot a bar chart of the quantities sold for each product
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Quantity'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.title('Bar Chart: Quantity Sold for Each Product')
plt.xticks(rotation=45)
plt.show()

# b) Create a scatter plot showing age vs. height for random data. 
# Use marker size to represent weight.
# Generating random data for demonstration
np.random.seed(0)  # For reproducibility
ages = np.random.randint(18, 60, 100)
heights = np.random.uniform(150, 190, 100)
weights = np.random.uniform(45, 90, 100)  # Use as marker size

plt.figure(figsize=(8, 5))
plt.scatter(ages, heights, s=weights, c=weights, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)
plt.xlabel('Age')
plt.ylabel('Height (cm)')
plt.title('Scatter Plot: Age vs Height (Marker size = Weight)')
plt.colorbar(label='Weight')
plt.show()
