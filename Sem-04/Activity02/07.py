import numpy as np

array_2d = np.random.randint(1, 101, size=(3, 3))

found = False
for row in range(array_2d.shape[0]):
    for col in range(array_2d.shape[1]):
        if array_2d[row, col] == 37:
            print(f"37 found at row {row}, column {col}")
            found = True
            break
    if found:
        break

if not found:
    print("Not found")

print("2D Array:")
print(array_2d)
