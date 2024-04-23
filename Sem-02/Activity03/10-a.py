import time

print("\nProgram to print decimal equivalent of binary 1100001110!\n")
time.sleep(2)

user_input = input("Enter binary number to be converted to decimal (press Enter for default): ")
binary_number = int(user_input) if user_input else 1100001110

count = len(str(binary_number))

decimal_result = 0

for i in range(0, count):
    digit = binary_number % 10
    decimal_result += digit * (2 ** i)
    binary_number //= 10

print(f"The decimal equivalent is: {decimal_result}")
