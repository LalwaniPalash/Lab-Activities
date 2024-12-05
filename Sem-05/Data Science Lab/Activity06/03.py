import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# a) Create a DataFrame with 100 rows and 5 columns of random integer data
df = pd.DataFrame(np.random.randint(1, 100, size=(100, 5)), columns=['A', 'B', 'C', 'D', 'E'])

print("a) Created DataFrame with 100 rows and 5 columns:")
print(df.head())

# b) Shuffle the DataFrame
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("\nb) Shuffled DataFrame:")
print(df_shuffled.head())

# c) Split the DataFrame into a training set (80%) and a testing set (20%)
train_df, test_df = train_test_split(df_shuffled, test_size=0.2, random_state=42)

print("\nc) Training and testing sets:")
print("Training set:")
print(train_df.head())
print("Testing set:")
print(test_df.head())
