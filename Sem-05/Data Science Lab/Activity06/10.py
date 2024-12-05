import pandas as pd
import numpy as np

# a) Load a CSV file (any csv file) into a DataFrame
df = pd.read_csv('your_file.csv')

# b) Calculate the mean, median, and standard deviation for the numeric columns
mean_values = df.mean(numeric_only=True)
median_values = df.median(numeric_only=True)
std_dev_values = df.std(numeric_only=True)

print("Mean:\n", mean_values)
print("\nMedian:\n", median_values)
print("\nStandard Deviation:\n", std_dev_values)

# c) Identify and replace outliers (values beyond 3 standard deviations) with the column mean
for col in df.select_dtypes(include=np.number).columns:
    mean = df[col].mean()
    std_dev = df[col].std()
    lower_bound = mean - 3 * std_dev
    upper_bound = mean + 3 * std_dev
    df[col] = df[col].apply(lambda x: mean if x < lower_bound or x > upper_bound else x)

# d) Replace all occurrences of 'N/A', 'Missing', and 'Unknown' in string columns with 'Not Available'
df = df.applymap(lambda x: 'Not Available' if x in ['N/A', 'Missing', 'Unknown'] else x)

# Display the modified DataFrame
print(df)
