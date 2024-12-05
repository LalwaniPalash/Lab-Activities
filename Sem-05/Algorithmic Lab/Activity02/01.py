def sumTo(n):
    if n == 1:
        return 1
    else:
        return n + sumTo(n - 1)

if __name__ == "__main__":
    n = 5
    result = sumTo(n)
    print(f"The sum of integers from 1 to {n} is: {result}")
