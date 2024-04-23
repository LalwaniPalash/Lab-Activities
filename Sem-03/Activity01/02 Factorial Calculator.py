import time

print("Factorial Calculator!\n")
time.sleep(2)

def Factorial(x):
	if x < 0:
		print("Factorial cannot be calculated for negative numbers.")

	result = 1

	for i in range(1, x+1):
		result *= i

	print(result)

x = None
while x is None:
	try:
		x = int(input("Enter an integer: "))
	except ValueError:
		print("Please enter a valid integer.")

Factorial(x)
