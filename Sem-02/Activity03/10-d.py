import time

print("\nProgram to obtain hexadecimal equivalent of decimal 34567!\n")
time.sleep(2)

user_input = input("Enter binary number to be converted to decimal (press Enter for default): ")
decimal_number = int(user_input) if user_input else 34567

hexadecimal_result = ""
hex_digits = "0123456789ABCDEF"

while decimal_number > 0:
    remainder = decimal_number % 16
    hexadecimal_result = hex_digits[remainder] + hexadecimal_result
    decimal_number //= 16

print(f"The hexadecimal equivalent is: 0x{hexadecimal_result}")
