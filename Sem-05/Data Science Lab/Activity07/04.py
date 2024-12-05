import matplotlib.pyplot as plt
import numpy as np

# a) Create a line graph for y = log(x) with x values between 1 and 100. Set the linewidth to 3 and use a dash-dot linestyle.
x = np.linspace(1, 100, 1000)
y = np.log(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, linestyle='-.', linewidth=3, color='purple', label='y = log(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Graph: y = log(x)')
plt.legend()
plt.grid(True)
plt.show()

# b) Display a plot with multiple subplots: one for a bar chart, one for a line graph, and one for a scatter plot.
# Create some random data
x_data = np.linspace(0, 5, 10)
y_data_line = np.sin(x_data)
y_data_bar = [5, 10, 15, 10, 8, 6, 4, 7, 9, 12]
x_data_scatter = np.random.rand(30)
y_data_scatter = np.random.rand(30)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Bar chart subplot
axs[0].bar(x_data, y_data_bar, color='lightblue')
axs[0].set_title('Bar Chart')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')

# Line graph subplot
axs[1].plot(x_data, y_data_line, color='green', linestyle='-', linewidth=2)
axs[1].set_title('Line Graph')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')

# Scatter plot subplot
axs[2].scatter(x_data_scatter, y_data_scatter, color='orange')
axs[2].set_title('Scatter Plot')
axs[2].set_xlabel('X')
axs[2].set_ylabel('Y')

plt.tight_layout()
plt.show()

# c) Create a pie chart with custom colors and a legend. Use the categories ['A', 'B', 'C', 'D'] with sizes [10, 20, 40, 30].
sizes = [10, 20, 40, 30]
labels = ['A', 'B', 'C', 'D']
colors = ['lightcoral', 'lightblue', 'lightgreen', 'yellow']
explode = (0.1, 0, 0, 0)  # explode 'A' slice slightly

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode, wedgeprops={'edgecolor': 'black'})
plt.title('Pie Chart with Custom Colors and Legend')

# Add legend
plt.legend(labels, title='Categories', loc='best')
plt.show()
