import time
import math

print("Program to calculate area of triangle!")
time.sleep(2)

print("Select what type of triangle do you want to use for area calculation.")
print("\nSelect 1 if base and height of a triangle are given.")
print("Select 2 if sides of a triangle are given as a, b, and c.")
print("Select 3 if two sides and the included angle is given.")
print("Select 4 if it is an equilateral triangle and one side is given.")
print("Select 5 if it is an isosceles triangle and an equal side and base is given.")

x = None
area = None
while x is None:
	try:
		x = int(input("Enter a number: "))
	except ValueError:
		print("Invalid Input!")

if x == 1:
	b, h = None, None
	while None in (b, h):
		try:
			b = float(input("Enter the base of the triangle: "))
			h = float(input("Enter the height of the triangle: "))
		except ValueError:
			print("Invalid Input!")
	area = 1/2 * (b * h)

elif x == 2:
	a, b, c = None, None, None

	while None in (a,b,c):
		try:
			a = float(input("Enter the measurements of the first side: "))
			b = float(input("Enter the measurements of the second side: "))
			c = float(input("Enter the measurements of the third side: "))
		except ValueError: 
			print("Invalid Input!")	
	s = (a + b + c) / 2
	area = math.sqrt(s * (s - a) * (s - b) * (s - c))	

elif x == 3:
	s1, s2, angle = None, None, None
	while None in (s1, s2):
		try:
			s1 = float(input("Enter the first side: "))
			s2 = float(input("Enter the second side: "))
			angle = int(input("Enter the angle provided to you (Keep in mind, the angle should be the one between the two sides): "))
		except ValueError:
			print("Invalid Input!")
	area = 1/2 * s1 * s2 * math.sin(angle)

elif x == 4: 
	side = None
	while side is None:
		try: 
			side = float(input("Input the measurement of side: "))
		except ValueError:
			print("Invalid Input!")
	area = (math.sqrt(3) / 4) * side**2

elif x == 5: 
	a, b = None, None
	while None in (a, b):
		try: 
			a = float(input("Enter the measurement of the side which is equal: "))
			b = float(input("Enter the base: "))
		except ValueError:
			print("Invalid Input!")
	area = 1/4 * (b * (math.sqrt((4 * a ** 2) - (b**2))))

else:
	print("Error: Invalid Input!")

print(f"The area of the triangle is {area}")
