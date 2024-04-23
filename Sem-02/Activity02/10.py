import time

print("Program to calculate the sum of reciprocals of 1-10!")
time.sleep(2)

N = 0

for i in range(1, 11):
    N += 1/i

print(f"The sum of reciprocals of numbers from 1 to 10 is: {N}")
