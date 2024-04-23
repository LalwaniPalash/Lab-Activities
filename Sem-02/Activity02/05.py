import time

print("Compound Interest Calculator")
time.sleep(2)

p, r, n, t = None, None, None, None

while None in (p, r, n, t):
	try:
		p = int(input("Enter the principal amount: "))
		r = int(input("Enter the rate of interest (Do not use \% sign): "))
		n = int(input("Enter number of times the interest is compounded in a year: "))
		t = int(input("Enter number of years (only the number): "))
	except ValueError:
		print("Invalid Input!")

r = r/100
A = p*(1 + (r/n))**(n*t)
CI = A - p

print(f"The amount after {t} years will be {A:.2f} and the total interest will be {CI:.2f}.")
