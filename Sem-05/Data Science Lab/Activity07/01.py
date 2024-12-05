import matplotlib.pyplot as plt
import numpy as np

# a) Plot a simple line graph for the values [1, 2, 3, 4] on the x-axis and their squares on the y-axis.
x = [1, 2, 3, 4]
y = [i**2 for i in x]

plt.figure(figsize=(6, 4))
plt.plot(x, y, label='y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Line Graph: y = x^2')
plt.legend()
plt.grid(True)
plt.show()

# b) Generate a plot that shows three lines on the same figure: y = x, y = x^2, and y = x^3 for x values from 0 to 5.
x = np.linspace(0, 5, 100)
y1 = x
y2 = x**2
y3 = x**3

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='y = x', color='r', marker='o', markersize=5)
plt.plot(x, y2, label='y = x^2', color='g', marker='^', markersize=5)
plt.plot(x, y3, label='y = x^3', color='b', marker='s', markersize=5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Multiple Lines: y = x, y = x^2, y = x^3')
plt.legend()
plt.grid(True)
plt.show()

# c) Create a bar graph showing fruit supplies: ['Apple', 'Banana', 'Cherry', 'Date'] with counts [20, 35, 30, 15].
fruits = ['Apple', 'Banana', 'Cherry', 'Date']
counts = [20, 35, 30, 15]

plt.figure(figsize=(8, 5))
plt.bar(fruits, counts, color=['red', 'yellow', 'pink', 'brown'])
plt.xlabel('Fruit')
plt.ylabel('Supply Count')
plt.title('Fruit Supply Bar Graph')
plt.show()
