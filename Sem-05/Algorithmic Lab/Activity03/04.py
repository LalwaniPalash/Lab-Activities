def initialize_knapsack_table(n, W):
    table = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for row in table:
        print(row)

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    W = int(input("Enter the knapsack capacity: "))
    
    initialize_knapsack_table(n, W)
