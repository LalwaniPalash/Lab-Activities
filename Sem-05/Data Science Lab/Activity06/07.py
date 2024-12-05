import pandas as pd

# a) Create a DataFrame with fictional e-commerce data
data = {
    'OrderID': [101, 102, 103, 104, 105],
    'Product': ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Smartwatch'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Price': [1200, 800, 150, 500, 200],
    'Quantity': [2, 3, 5, 1, 4]
}

df = pd.DataFrame(data)

# b) Add a column 'Total' as the product of 'Price' and 'Quantity'
df['Total'] = df['Price'] * df['Quantity']
