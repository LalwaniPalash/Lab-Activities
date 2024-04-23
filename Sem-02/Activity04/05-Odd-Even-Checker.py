import time

print("\nProgram to check if user input is odd or even.\n")
time.sleep(2)

userinput = None

while userinput is None:
	try: 
		userinput = int(input("Enter an integer: "))
	except ValueError:
		print("Error: Invalid Input!")

r = userinput % 2

if r == 0:
	print(f"User Input is even.")
else:
	print(f"User Input is odd.")
