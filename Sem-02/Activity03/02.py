import time

print("Program to swap values of 2 variables!\n")
time.sleep(2)

a = None
b = None

while a is None and b is None:
	try:
		a = int(input("Value of a: "))
		b = int(input("Value of b: "))
	except ValueError:
		input("Invalid Input!")

swap = input("Do you want to swap the values?(y/n): ")

if swap == "y":
	a = a + b
	b = a - b
	a = a - b
else: 
	None

print(f"Value of A = {a} and Value of B = {b}")
