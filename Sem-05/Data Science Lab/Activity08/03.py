import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# 1. Scatter Plot of Fare vs. Age with Regression Line
plt.figure(figsize=(8, 6))
sns.regplot(x='age', y='fare', data=titanic, scatter_kws={'s': 50, 'alpha': 0.6}, line_kws={'color': 'red', 'lw': 2})
plt.title('Scatter Plot of Fare vs. Age with Regression Line')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

# 2. Stacked Bar Chart to Show Survival Rates Across Different Classes
# First, calculate the survival rates
survival_rates = titanic.groupby(['pclass', 'survived']).size().unstack(fill_value=0)
survival_rates = survival_rates.div(survival_rates.sum(axis=1), axis=0)  # Normalize to get proportions

# Plot the stacked bar chart
survival_rates.plot(kind='bar', stacked=True, color=['red', 'green'], figsize=(8, 6))
plt.title('Survival Rates Across Different Classes')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.xticks(ticks=[0, 1, 2], labels=['Class 1', 'Class 2', 'Class 3'], rotation=0)
plt.legend(['Did Not Survive', 'Survived'], title='Survival Status', loc='upper right')
plt.show()
