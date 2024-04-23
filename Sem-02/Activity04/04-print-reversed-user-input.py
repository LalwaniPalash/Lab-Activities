import time

print("\nProgram to reverse user inputted string.\n")
time.sleep(2)

userinput = None

while userinput is None:
	try: 
		userinput = str(input("Enter a string: "))
	except ValueError:
		print("Error: Invalid Input!")

print(userinput[::-1])
