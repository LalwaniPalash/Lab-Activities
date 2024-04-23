import time
import random
import math

print("\nProgram to get truncated, floored and celled value of [-0.2, -0.5, 0.2, 1.5, 2.9]!\n")
time.sleep(2)

numbers = [-2.8, -0.5, 0.2, 1.5, 2.9]

for num in numbers:
    truncated = math.trunc(num)
    floored = math.floor(num)
    ceiled = math.ceil(num)
    
    print(f"Original: {num}")
    print(f"Truncated: {truncated}")
    print(f"Floored: {floored}")
    print(f"Celed: {ceiled}")
    print()
