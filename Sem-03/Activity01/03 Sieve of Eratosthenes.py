import time

print("Prime Number Finder!\n")
time.sleep(2)

def sieve_of_eratosthenes(limit):
	primes = []
	sieve = [True] * (limit + 1)

	for p in range(2, limit + 1):
		if sieve[p]: 
			primes.append(p)
			for i in range(p * p, limit + 1, p):
				sieve[i] = False

	print(primes)


limit = None
while limit is None:
	try:
		limit = int(input("Enter an integer: "))
	except ValueError:
		print("Please enter a valid integer.")

sieve_of_eratosthenes(limit)
