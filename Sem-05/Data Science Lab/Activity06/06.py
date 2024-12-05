import pandas as pd

# a) Create a DataFrame with columns 'Student', 'Subject', and 'Marks'
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math'],
    'Marks': [88, 92, 75, 89, 95]
}

df = pd.DataFrame(data)

# b) Sort the DataFrame by 'Marks' in descending order
df_sorted = df.sort_values(by='Marks', ascending=False)

# c) Add a column 'Rank' assigning a rank to each student within each subject using the rank() method
df_sorted['Rank'] = df_sorted.groupby('Subject')['Marks'].rank(method='min', ascending=False)
