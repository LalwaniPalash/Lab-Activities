import time

print("Program to print numbers in an inversed right angled triangle.\n")
time.sleep(2) 

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("\n")
