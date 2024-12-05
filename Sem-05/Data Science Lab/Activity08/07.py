import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Create the custom dataset
np.random.seed(42)

# Student names (for simplicity, we use generic names)
names = [f"Student {i}" for i in range(1, 21)]

# Random ages between 18 and 22
ages = np.random.randint(18, 23, size=20)

# Random grades in 3 subjects (Math, Science, English) between 50 and 100
math_grades = np.random.randint(50, 101, size=20)
science_grades = np.random.randint(50, 101, size=20)
english_grades = np.random.randint(50, 101, size=20)

# Calculate overall grade as the average of the three subjects
overall_grades = (math_grades + science_grades + english_grades) / 3

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
    'Overall Grade': overall_grades,
    'Study Hours': study_hours,
    'Extracurricular': extracurricular
})

# Display the first few rows of the dataset
print(data.head())

# Step 2: Visualizations

# a) Scatter Plot: Study Hours vs. Overall Grades with Regression Line
plt.figure(figsize=(8, 6))
sns.regplot(x='Study Hours', y='Overall Grade', data=data, scatter_kws={'s': 100, 'alpha': 0.6}, line_kws={'color': 'red'})
plt.title('Study Hours vs. Overall Grades with Regression Line')
plt.xlabel('Study Hours per Week')
plt.ylabel('Overall Grade')
plt.show()

# b) Violin Plot: Comparison of Grades Across Age Groups
plt.figure(figsize=(8, 6))
sns.violinplot(x='Age', y='Overall Grade', data=data, palette='Set2')
plt.title('Distribution of Grades Across Different Age Groups')
plt.xlabel('Age')
plt.ylabel('Overall Grade')
plt.show()

# c) KDE Plot: Density of Grades for Students Involved vs. Not Involved in Extracurricular Activities
plt.figure(figsize=(8, 6))
sns.kdeplot(data[data['Extracurricular'] == 1]['Overall Grade'], label='Extracurricular', fill=True, color='blue', alpha=0.6)
sns.kdeplot(data[data['Extracurricular'] == 0]['Overall Grade'], label='No Extracurricular', fill=True, color='red', alpha=0.6)
plt.title('Density of Grades for Students Involved vs. Not Involved in Extracurricular Activities')
plt.xlabel('Overall Grade')
plt.ylabel('Density')
plt.legend()
plt.show()
