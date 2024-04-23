import time

print("\nProgram to convert a float value to numeric string!\n")
time.sleep(2)

user_input = input("Enter a float value to be converted to numeric string (press Enter for default[4.33]: ")
float_value = float(user_input) if user_input else 4.33

numeric_string = str(float_value)

print(f"The numeric string equivalent is: {numeric_string}")
