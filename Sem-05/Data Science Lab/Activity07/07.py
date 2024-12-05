import matplotlib.pyplot as plt

# Provided fruits list and counts
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]

# Customize bar colors
colors = ['red', 'blue', 'pink', 'orange']

# Create a vertical bar chart
plt.figure(figsize=(8, 5))
plt.bar(fruits, counts, color=colors)

# Add axis labels and a title
plt.xlabel('Fruit')
plt.ylabel('Supply Count')
plt.title('Fruit Supply Chart')

# Display the plot
plt.show()
