import time
import random

print("\nProgram to print five random numbers in range of 10 to 50!\n")
time.sleep(2)

seed_value = 6

random.seed(seed_value)
random_numbers_initial = [random.randint(10, 50) for _ in range(5)]
print(f"Random Numbers with seed {seed_value}: {random_numbers_initial}")

new_seed_value = int(time.time())
random.seed(new_seed_value)

random_numbers_updated = [random.randint(10, 50) for _ in range(5)]
print(f"Random Numbers with updated seed {new_seed_value}: {random_numbers_updated}")
