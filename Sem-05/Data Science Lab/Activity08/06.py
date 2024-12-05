import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
np.random.seed(42)

# Student names (for simplicity, we use generic names)
names = [f"Student {i}" for i in range(1, 21)]

# Random ages between 18 and 22
ages = np.random.randint(18, 23, size=20)

# Random grades in 3 subjects (Math, Science, English) between 50 and 100
math_grades = np.random.randint(50, 101, size=20)
science_grades = np.random.randint(50, 101, size=20)
english_grades = np.random.randint(50, 101, size=20)

# Random study hours per week between 5 and 30 hours
study_hours = np.random.randint(5, 31, size=20)

# Random participation in extracurricular activities (0 = No, 1 = Yes)
extracurricular = np.random.randint(0, 2, size=20)

# Create a DataFrame
data = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'Math Grade': math_grades,
    'Science Grade': science_grades,
    'English Grade': english_grades,
    'Study Hours': study_hours,
    'Extracurricular': extracurricular
})

# Show the first few rows of the dataset
print(data.head())

# Step 2: Visualizations

# a) Histogram for Study Hours
plt.figure(figsize=(8, 6))
sns.histplot(data['Study Hours'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title('Histogram of Study Hours per Week')
plt.xlabel('Study Hours per Week')
plt.ylabel('Frequency')
plt.show()

# b) Bar Chart for Average Grades in Each Subject
average_grades = data[['Math Grade', 'Science Grade', 'English Grade']].mean()

plt.figure(figsize=(8, 6))
sns.barplot(x=average_grades.index, y=average_grades.values, palette='Set2')
plt.title('Average Grades in Each Subject')
plt.xlabel('Subject')
plt.ylabel('Average Grade')
plt.show()
