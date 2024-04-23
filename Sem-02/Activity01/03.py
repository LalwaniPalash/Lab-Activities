import time

print("Welcome to a Rectangle area calculator program!")
time.sleep(2)

while True:
    try:
        l = int(input("Enter the length: "))
        b = int(input("Enter the breadth: "))
        if l > 0 and b > 0:
            break
        else:
            print("Invalid Measurements, please input the measurements again.")
    except ValueError:
        print("Invalid Integer!")

unit = input("Enter the unit used for the measurements: ")

ans = l * b
print(f"The area of this rectangle is {ans} {unit}²")
