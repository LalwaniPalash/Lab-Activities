import time

print("Program to calculate Sum of 'n' numbers!")
time.sleep(2)

n = int(input("Enter a positive integer n: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = 0
    for i in range(1, n + 1):
        total += i

    print(f"The sum of the first {n} natural numbers is: {total}")
