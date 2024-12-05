import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# 1. Univariate Analysis

# Histogram for 'age'
plt.figure(figsize=(8, 6))
sns.histplot(titanic['age'].dropna(), bins=20, kde=True, color='skyblue')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Histogram for 'fare'
plt.figure(figsize=(8, 6))
sns.histplot(titanic['fare'].dropna(), bins=20, kde=True, color='green')
plt.title('Histogram of Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Count plot for 'class'
plt.figure(figsize=(8, 6))
sns.countplot(x='pclass', data=titanic, palette='Set2')
plt.title('Count Plot of Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

# 2. Bivariate Analysis

# Scatter plot for Age vs Fare
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='fare', data=titanic, hue='survived', palette='Set1')
plt.title('Scatter Plot of Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(title='Survival', loc='upper left', labels=['Did Not Survive', 'Survived'])
plt.show()

# Scatter plot for Age vs Pclass
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='pclass', data=titanic, hue='survived', palette='Set1')
plt.title('Scatter Plot of Age vs Pclass')
plt.xlabel('Age')
plt.ylabel('Passenger Class')
plt.legend(title='Survival', loc='upper right', labels=['Did Not Survive', 'Survived'])
plt.show()

# Correlation Heatmap for numerical columns
plt.figure(figsize=(8, 6))
correlation_matrix = titanic[['age', 'fare', 'pclass']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')
plt.title('Correlation Heatmap of Age, Fare, and Pclass')
plt.show()

# Regression line for Age vs Fare
plt.figure(figsize=(8, 6))
sns.regplot(x='age', y='fare', data=titanic, scatter_kws={'s': 50, 'alpha': 0.6}, line_kws={'color': 'red', 'lw': 2})
plt.title('Regression Line for Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
