def fibonacci_memo(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 10  # Compute the 10th Fibonacci number
    result = fibonacci_memo(n)
    print(f"The {n}th Fibonacci number is: {result}")
