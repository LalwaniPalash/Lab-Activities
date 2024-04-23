import time

print("\nDivisibility Checker for 3 and 5.\n")
time.sleep(2)

number = None

while number is None:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: Invalid Input!")

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")
