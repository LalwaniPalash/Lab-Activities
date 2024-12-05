import pandas as pd
import numpy as np

# a) Read a CSV file and create a DataFrame with some missing values
df = pd.read_csv('your_file.csv')

# b) Sort a DataFrame by index
df_sorted = df.sort_index()

# c) Replace missing values using forward fill (ffill) and backward fill (bfill)
df_ffill = df.fillna(method='ffill')
df_bfill = df.fillna(method='bfill')

# d) Verify the changes using the .isnull() method
df_isnull_ffill = df_ffill.isnull()
df_isnull_bfill = df_bfill.isnull()
