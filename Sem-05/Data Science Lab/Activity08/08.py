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

# a) Pair Plot: Study Hours, Grades, and Age
sns.pairplot(data[['Age', 'Study Hours', 'Math Grade', 'Science Grade', 'English Grade', 'Overall Grade']])
plt.suptitle('Pair Plot of Study Hours, Grades, and Age', y=1.02)
plt.show()

# b) Heatmap: Correlation Matrix for Numerical Variables
corr_matrix = data[['Age', 'Math Grade', 'Science Grade', 'English Grade', 'Overall Grade', 'Study Hours']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')
plt.title('Correlation Matrix Heatmap')
plt.show()
