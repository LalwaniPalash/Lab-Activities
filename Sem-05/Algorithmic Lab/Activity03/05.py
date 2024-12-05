def knapsack(weights, values, capacity):
    n = len(weights)
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:  # Can we include the current item?
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

weights = [1, 3, 4]
values = [15, 20, 30]
capacity = 4

result = knapsack(weights, values, capacity)
print(f"The maximum value that can be obtained is: {result}")
