import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

# a) Heatmap: Correlations across regions, categories, and customer demographics
# First, we will need to pivot the data and compute correlation among numerical features.
# We will create a pivot table for sales by region, category, and customer age.

# Create a new column for "Region-Product" to calculate correlation
sales_data['Region-Product'] = sales_data['Region'] + '-' + sales_data['Product Category']

# Pivot the data to create a sales matrix
pivot_data = sales_data.pivot_table(
    values='Sales Amount',
    index='Region',
    columns='Product Category',
    aggfunc='sum'
)

# Compute the correlation matrix
corr_matrix = pivot_data.corr()

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')
plt.title('Correlation Matrix Heatmap: Sales by Region and Product Category')
plt.show()

# b) Facet Grid: Sales trends over time for each product category
sales_data['Year-Month'] = sales_data['Date'].dt.to_period('M')  # Add Year-Month column

# Plotting sales trends over time
g = sns.FacetGrid(sales_data, col='Product Category', col_wrap=3, height=4)
g.map(sns.lineplot, 'Year-Month', 'Sales Amount', color='blue')
g.set_titles("{col_name}")
g.set_axis_labels('Year-Month', 'Sales Amount ($)')
g.fig.suptitle('Sales Trends Over Time by Product Category', fontsize=16)
g.fig.tight_layout()
g.fig.subplots_adjust(top=0.9)
plt.show()

# c) Pair Plot: Explore relationships among Customer Age, Sales Amount, and Product Category
# We will use the pairplot to visualize relationships between Customer Age, Sales Amount, and Product Category.
sns.pairplot(sales_data[['Customer Age', 'Sales Amount', 'Product Category']], hue='Product Category', palette='Set1')
plt.suptitle('Pair Plot: Relationships Among Customer Age, Sales Amount, and Product Category', y=1.02)
plt.show()
