import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# a) Create a histogram of passenger fares with customized bins and colors
plt.figure(figsize=(8, 6))
sns.histplot(titanic['fare'], bins=20, kde=False, color='skyblue', edgecolor='black')
plt.title('Histogram of Passenger Fares')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# b) Create a box plot to show the distribution of ages categorized by passenger class
plt.figure(figsize=(8, 6))
sns.boxplot(x='pclass', y='age', data=titanic, palette='Set2')
plt.title('Box Plot of Ages by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

# c) Generate a KDE plot to visualize the density distribution of passenger ages
plt.figure(figsize=(8, 6))
sns.kdeplot(titanic['age'].dropna(), shade=True, color='purple')
plt.title('KDE Plot of Passenger Ages')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()
