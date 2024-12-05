import matplotlib.pyplot as plt

# Data
y = [35, 25, 25, 15]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors = ['red', 'yellow', 'pink', 'brown']  # Custom colors
myexplode = [0.2, 0, 0, 0]  # Exploding the 'Apples' slice

# Create the pie chart
plt.figure(figsize=(6, 6))
plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=myexplode, wedgeprops={'edgecolor': 'black'})

# Add title
plt.title('Fruit Distribution Pie Chart')

# Show the plot
plt.show()
