import matplotlib.pyplot as plt
import numpy as np

# Example data for 12 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [30, 32, 35, 38, 40, 42, 43, 41, 39, 36, 33, 31]  # Temperature in Celsius
rainfall = [50, 45, 60, 70, 80, 90, 100, 85, 75, 60, 55, 50]  # Rainfall in mm

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot temperature data (line graph)
ax1.plot(months, temperature, color='tab:red', label='Temperature (°C)', marker='o', linestyle='-', linewidth=2)

# Label for the first y-axis (Temperature)
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a second y-axis for rainfall
ax2 = ax1.twinx()
ax2.bar(months, rainfall, color='tab:blue', alpha=0.6, label='Rainfall (mm)', width=0.5)

# Label for the second y-axis (Rainfall)
ax2.set_ylabel('Rainfall (mm)', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Title of the plot
plt.title('Temperature and Rainfall for 12 Months')

# Show the plot
plt.show()
