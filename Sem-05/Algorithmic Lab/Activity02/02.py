def fibTerm(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibTerm(n - 1) + fibTerm(n - 2)

if __name__ == "__main__":
    n = 10
    result = fibTerm(n)
    print(f"The {n}th term of the Fibonacci sequence is: {result}")
