import time

print("Program to calculate area of a circle!")
time.sleep(2)

pi = 3.14159
r = None

while r is None:
    try:
        r = float(input("Enter the radius of a circle: "))
    except ValueError:
        print("Invalid Integer!")

Area = pi * (r**2)
print(f"\nThe area of a circle with radius {r} is {Area}.")
