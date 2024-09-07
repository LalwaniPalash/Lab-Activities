import numpy as np

def generate_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        
        new_i, new_j = (i - 1) % n, (j + 1) % n
        
        if magic_square[new_i, new_j]:
            new_i, new_j = (i + 1) % n, j
        
        i, j = new_i, new_j

    return magic_square

def main():
    n = int(input("Enter the size of the magic square (odd number): "))
    
    if n % 2 == 0:
        print("The size must be an odd number.")
        return
    
    magic_square = generate_magic_square(n)
    
    print("Magic Square:")
    print(magic_square)

main()
