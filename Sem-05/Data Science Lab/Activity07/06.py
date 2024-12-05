import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
np.random.seed(0)  # For reproducibility
ages = np.random.randint(18, 60, 100)  # Random ages between 18 and 60
heights = np.random.uniform(150, 190, 100)  # Random heights between 150 cm and 190 cm
weights = np.random.uniform(45, 90, 100)  # Random weights between 45 kg and 90 kg

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(ages, heights, s=weights, c=weights, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Height (cm)')
plt.title('Scatter Plot: Age vs Height (Marker size = Weight)')

# Add color bar to indicate weight scale
plt.colorbar(label='Weight (kg)')

# Show the plot
plt.show()
