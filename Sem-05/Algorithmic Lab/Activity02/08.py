def power(x, n):
    if n == 0:
        return 1
    
    if n > 0:
        return x * power(x, n - 1)
    
    if n < 0:
        return 1 / power(x, -n)

if __name__ == "__main__":
    x = 2
    n = 3
    result = power(x, n)
    print(f"{x}^{n} = {result}")
    
    # Test with negative exponent
    x = 2
    n = -3
    result = power(x, n)
    print(f"{x}^{n} = {result}")
