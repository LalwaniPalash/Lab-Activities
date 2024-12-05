import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# 1. Generate a KDE plot to visualize the density distribution of passenger ages on the Titanic
plt.figure(figsize=(8, 6))
sns.kdeplot(titanic['age'].dropna(), shade=True, color='purple')
plt.title('KDE Plot of Passenger Ages on the Titanic')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

# 2. Custom dataset for Line Chart: Trend of weights over ages
# Creating a custom dataset
np.random.seed(42)
ages = np.linspace(18, 80, 100)  # Ages from 18 to 80
weights = 50 + (ages - 18) * 0.4 + np.random.normal(0, 5, 100)  # Weight increases with age but with some noise

# Create a line chart for trend of weights over ages
plt.figure(figsize=(10, 6))
plt.plot(ages, weights, color='teal', marker='o', linestyle='-', linewidth=2)
plt.title('Trend of Weights over Ages (Custom Dataset)')
plt.xlabel('Age')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()

# 3. Custom dataset for Violin Plot: Compare the distribution of weights across different age groups
# Create age groups
age_groups = pd.cut(ages, bins=[18, 30, 40, 50, 60, 70, 80], labels=['18-30', '31-40', '41-50', '51-60', '61-70', '71-80'])
weight_data = pd.DataFrame({'Age Group': age_groups, 'Weight': weights})

# Create a violin plot to compare the distribution of weights across age groups
plt.figure(figsize=(10, 6))
sns.violinplot(x='Age Group', y='Weight', data=weight_data, palette='muted')
plt.title('Distribution of Weights across Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Weight (kg)')
plt.show()
