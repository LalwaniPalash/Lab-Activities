import pandas as pd
import numpy as np

# Create a DataFrame with random values of shape (3, 4) using NumPy
random_values = np.random.rand(3, 4)
df_random = pd.DataFrame(random_values)

# Print the DataFrame
print(df_random)
