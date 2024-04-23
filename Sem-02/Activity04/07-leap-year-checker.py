import time

print("\nLeap-Year Checker.\n")
time.sleep(2)

year = None

while year is None:
    try: 
        user_input = input("Enter a year (4 digits): ")
        if user_input.isdigit() and len(user_input) == 4:
            year = int(user_input)
        else:
            print("Error: Invalid Input! Please enter a valid 4-digit year.")
    except ValueError:
        print("Error: Invalid Input!")

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
