import time

print("\nProgram to count number of vowels [a, e, i, o, u] in user input(Case Sensitivity will be ignored).\n")
time.sleep(2)

userinput = None

while userinput is None:
	try: 
		userinput = str(input("Enter a string: ")).lower()
	except ValueError:
		print("Error: Invalid Input!")

count = 0

for i in userinput:
	if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
		count += 1

print(f"Number of Vowels: {count}\n")	
