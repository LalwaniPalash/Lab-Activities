import time

print("Multiplication Table Program!")
time.sleep(2)

num = None
while num is None: 
    try:
        num = int(input("Enter a number to generate its multiplication table: "))
    except ValueError: 
        print("Invalid Number!")

table_range = 10

print(f"Multiplication table for {num}:\n")

for i in range(1, table_range + 1):
    result = num * i
    print(f"{num} x {i} = {result}")
