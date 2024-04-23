import time

print("Even-Odd Program!")
time.sleep(2)

n = None
while n is None: 
    try:
        n = int(input("Enter a number: "))
    except ValueError: 
        print("Invalid Integer")

r = n % 2

if r == 0:
    print(f"The number {n} is Even!")
else: 
    print(f"The number {n} is Odd!")
