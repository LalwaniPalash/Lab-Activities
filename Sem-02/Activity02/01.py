import time

print("Welcome to a simple Division program!")
time.sleep(2)

n11 = None
n12 = None

while n11 is None and n12 is None:
    try:
        n11 = int(input("Enter the first number: "))
        n12 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid Integer!")

result = n11/n12
print(f"\nWe get {result} when we divide {n11} by {n12}.")
