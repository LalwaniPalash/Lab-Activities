import time

print("\nProgram to compare two user inputted numbers.\n")
time.sleep(2)

float1 = None
float2 = None

while float1 is None and float2 is None:
	try: 
		float1 = float(input("Enter first number: "))
		float2 = float(input("Enter second number: "))
	except ValueError:
		print("Error: Invalid Input!")

if float1 > float2:
	print(f"First number {float1} is greater than second number {float2}.")
elif float1 < float2:
	print(f"First number {float1} is smaller than second number {float2}")
elif float1 == float2:
	print(f"First number {float1} is equal to the second number {float2}")
else:
	print("Unknown Error Occurred. Please try again late.")
