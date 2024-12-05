import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create the dataset
np.random.seed(42)

# Random sales data
products = ['Electronics', 'Clothing', 'Groceries', 'Home & Kitchen', 'Toys']
regions = ['North', 'South', 'East', 'West']
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')

# Generate random sales data
data = {
    'Product Category': np.random.choice(products, size=1000),
    'Region': np.random.choice(regions, size=1000),
    'Sales Amount': np.random.uniform(10, 1000, size=1000),  # Sales between 10 and 1000
    'Date': np.random.choice(dates, size=1000),
    'Customer Age': np.random.randint(18, 70, size=1000)  # Age between 18 and 70
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Display the first few rows of the dataset
print(sales_data.head())

# Step 2: Visualizations

# a) Bar Plot: Total Sales Amount for Each Product Category
plt.figure(figsize=(8, 6))
sales_by_category = sales_data.groupby('Product Category')['Sales Amount'].sum().sort_values(ascending=False)
sales_by_category.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Sales Amount for Each Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount ($)')
plt.xticks(rotation=45)
plt.show()

# b) Histogram: Distribution of Sales Amount
plt.figure(figsize=(8, 6))
sns.histplot(sales_data['Sales Amount'], bins=30, kde=True, color='purple', edgecolor='black')
plt.title('Distribution of Sales Amount')
plt.xlabel('Sales Amount ($)')
plt.ylabel('Frequency')
plt.show()

# c) Pie Chart: Percentage of Sales from Different Regions
region_sales = sales_data.groupby('Region')['Sales Amount'].sum()
plt.figure(figsize=(8, 6))
region_sales.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'salmon', 'lightcoral'], startangle=90)
plt.title('Percentage of Sales from Different Regions')
plt.ylabel('')  # Hide the y-label
plt.show()
