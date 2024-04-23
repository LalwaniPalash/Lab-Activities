import time
import math


print("This Program will calculate any quadratic equation given the co-efficients a, b, and c!")
time.sleep(2)

a = None; b = None; c = None

while a is None and b is None and c is None:
	try:
		a = int(input("Enter the value of a: "))
		b = int(input("Enter the value of b: "))
		c = int(input("Enter the value of c: "))
	except ValueError: 
		print("Invalid Integer! Try again.")

p1 = -b
p2 = math.sqrt(((b**2) - 4*a*c))

r1 = (p1 + p2) / (2*a)
r2 = (p1 - p2) / (2*a)

print(f"First root is {r1} and Second root is {r2}.")
