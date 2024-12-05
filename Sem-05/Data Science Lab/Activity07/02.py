import matplotlib.pyplot as plt
import numpy as np

# a) Plot a line graph for y = sin(x) for x values between 0 and 2π. Use a dotted linestyle and red color for the line.
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, 'r:', label='y = sin(x)')  # 'r:' specifies red dotted line
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Graph: y = sin(x)')
plt.legend()
plt.grid(True)
plt.show()

# b) Create a horizontal bar chart for ['Tom', 'Dick', 'Harry', 'Slim', 'Jim'] with corresponding scores [10, 20, 15, 25, 18].
names = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
scores = [10, 20, 15, 25, 18]

plt.figure(figsize=(8, 5))
plt.barh(names, scores, color='skyblue')
plt.xlabel('Scores')
plt.ylabel('Names')
plt.title('Horizontal Bar Chart: Scores of Individuals')

# Add labels to the bars
for i, v in enumerate(scores):
    plt.text(v + 0.5, i, str(v), ha='center', va='center', color='black')

plt.show()

# c) Plot a pie chart showing the distribution of ['Apples', 'Bananas', 'Cherries', 'Dates'] with percentages [35, 25, 25, 15].
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [35, 25, 25, 15]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'yellow', 'pink', 'brown'])

# Highlight the segment for 'Apples'
plt.pie([35, 65], labels=['Apples', 'Others'], autopct='%1.1f%%', startangle=90, colors=['red', 'lightgray'], wedgeprops={'edgecolor': 'black'})

plt.title('Pie Chart: Distribution of Fruits')
plt.show()
