import time

print("Welcome to a simple Division program!")
time.sleep(2)

n13 = None
n14 = None

while n13 is None and n14 is None:
    try:
        n13 = float(input("Enter the first floating-point number: "))
        n14 = float(input("Enter the second floating-point number: "))
    except ValueError:
        print("Invalid Integer!")

result = n13/n14
print(f"\nWe get {result} when we divide {n13} by {n14}.")
