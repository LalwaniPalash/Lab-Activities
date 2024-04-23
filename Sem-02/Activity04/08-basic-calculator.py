import time

print("\nBasic Calculator.\n")
time.sleep(2)

num1, num2, operator, result = None, None, None, None

while num1 is None:
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Error: Invalid Input!")

while operator not in ('+', '-', '*', '/'):
    operator = input("Enter the operator (+, -, *, /): ")

while num2 is None:
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid Input!")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")

if result is not None:
    print(f"The result of {num1} {operator} {num2} is: {result}")
