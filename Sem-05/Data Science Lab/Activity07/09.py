import matplotlib.pyplot as plt
import numpy as np

# Generate 100 random points with x and y values ranging from -10 to 10
x = np.random.uniform(-10, 10, 100)
y = np.random.uniform(-10, 10, 100)

# Determine the quadrant for each point
# Quadrant 1: x > 0, y > 0
# Quadrant 2: x < 0, y > 0
# Quadrant 3: x < 0, y < 0
# Quadrant 4: x > 0, y < 0

colors = []
for i in range(len(x)):
    if x[i] > 0 and y[i] > 0:
        colors.append('red')     # Quadrant 1
    elif x[i] < 0 and y[i] > 0:
        colors.append('blue')    # Quadrant 2
    elif x[i] < 0 and y[i] < 0:
        colors.append('green')   # Quadrant 3
    elif x[i] > 0 and y[i] < 0:
        colors.append('orange')  # Quadrant 4

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, alpha=0.6)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of 100 Random Points with Quadrant-based Color Coding')

# Draw lines for the x and y axes
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

# Show the plot
plt.show()
