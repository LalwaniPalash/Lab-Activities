import time

print("Program to calculate Simple Interest!")
time.sleep(2)

p = None
r = None
t = None

while p is None and r is None and t is None:
    try:
        p = float(input("Enter your Principal Amount: "))
        r = float(input("Enter the rate of interest per annum (as a decimal): "))
        t = int(input("Enter the term of this investment/loan in years: "))
    except ValueError:
        print("Invalid Input!")

SI = p * r * t

total_maturity = p + SI

print(f"Total Interest Amount is {SI:.2f} and the Total Maturity Amount is {total_maturity:.2f}.")
