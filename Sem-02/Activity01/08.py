import time

print("Factorial Program!")
time.sleep(2)

n = None
while n is None: 
    try:
    	n = int(input("Enter a non-negative integer: "))
    except ValueError: 
        print("Invalid Number!")

if n < 0:
    print("Factorial is undefined for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"The factorial of {n} is: {factorial}")
