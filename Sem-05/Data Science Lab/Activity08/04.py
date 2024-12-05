import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# 1. Regression relationship between Age and Fare for different embarkation points
plt.figure(figsize=(8, 6))
sns.lmplot(x='age', y='fare', hue='embarked', data=titanic, aspect=1.5, height=6, markers=['o', 's', 'D'])
plt.title('Regression Relationship Between Age and Fare for Different Embarkation Points')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

# 2. Heatmap showing survival count for each combination of class and gender
# First, create a pivot table to count survival for each combination of class and gender
survival_counts = titanic.pivot_table(index='sex', columns='pclass', values='survived', aggfunc='sum')

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(survival_counts, annot=True, cmap='YlGnBu', cbar_kws={'label': 'Survival Count'})
plt.title('Survival Count for Each Combination of Class and Gender')
plt.xlabel('Passenger Class')
plt.ylabel('Gender')
plt.show()
