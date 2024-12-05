import pandas as pd
import numpy as np

# a) Create a DataFrame with columns 'Student', 'Math', 'Science', and 'English' with some incorrect and missing values
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 92, np.nan, 78, 'error'],
    'Science': [88, np.nan, 72, 94, 81],
    'English': [np.nan, 80, 85, 'error', 95]
}

df = pd.DataFrame(data)

# b) Verify all missing values are handled using .isnull().sum() and replace missing values
print(df.isnull().sum())

# Convert non-numeric values (like 'error') to NaN for consistent handling
df['Math'] = pd.to_numeric(df['Math'], errors='coerce')
df['English'] = pd.to_numeric(df['English'], errors='coerce')

# Replace missing values with the mean of each column
df.fillna(df.mean(), inplace=True)

# Verify again after handling missing values
print(df.isnull().sum())

# c) Calculate the mean, median, and mode for each subject
mean_scores = df.mean()
median_scores = df.median()
mode_scores = df.mode().iloc[0]

# d) Identify the top performer in each subject
top_performers = df.idxmax()

# Print results
print("Mean Scores:\n", mean_scores)
print("\nMedian Scores:\n", median_scores)
print("\nMode Scores:\n", mode_scores)
print("\nTop Performers:\n", top_performers)
