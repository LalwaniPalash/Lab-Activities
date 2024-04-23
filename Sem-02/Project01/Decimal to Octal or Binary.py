import time


print("Program to convert Decimal Number to Binary / Octal Number.\n")
time.sleep(2)  

initial_input = None

while initial_input is None:
    try:
        initial_input = int(input("Enter a decimal number: "))
    except ValueError:
        print("Error: Invalid Input!")

convert_to = input("\nWhat number system do you want to convert your decimal? (B/O): ")

if convert_to == "B":
    binary_result = ""
    while initial_input // 2 != 0:
        binary_result = str(initial_input % 2) + binary_result
        initial_input = initial_input // 2
    binary_result = str(initial_input % 2) + binary_result
    binary_result = binary_result[::-1]
    print(f"\nThe binary equivalent of {initial_input} is: {binary_result}")

elif convert_to == "O":
    octal_result = ""
    while initial_input // 8 != 0:
        octal_result = str(initial_input % 8) + octal_result
        initial_input = initial_input // 8
    octal_result = str(initial_input % 8) + octal_result
    octal_result = octal_result[::-1]
    print(f"\nThe octal equivalent of {initial_input} is: {octal_result}")

else:
    print("Error: Invalid Input!")
