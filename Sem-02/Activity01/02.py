import time

print("Welcome to a simple Calculator program!")
time.sleep(2)

n1 = None
n2 = None

while n1 is None:
    try:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid Integer!")

valid = False
while not valid:
	operation = input("Enter the operation which you want to perform: ")	

	if operation == "*" or operation == "multiply":
	    print(n1 * n2)
	    valid = True
	elif operation == "/" or operation == "divide":
	    if n2 == 0:
	        print("Division by zero is not allowed.")
	    else:
	        print(n1 / n2)
	        valid = True
	elif operation == "+" or operation == "addition" or operation == "add" or operation == "plus":
	    print(n1 + n2)
	    valid = True
	elif operation == "-" or operation == "subtract" or operation == "minus" or operation == "subtraction":
	    print(n1 - n2)
	    valid = True
	else:
	    print("Invalid operation. Please enter *, /, +, or -.")
