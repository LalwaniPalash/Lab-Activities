def knapsack_tabulation(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def knapsack_memoization(weights, values, capacity, n, memo=None):
    if memo is None:
        memo = {}

    if n == 0 or capacity == 0:
        return 0
    
    if (n, capacity) in memo:
        return memo[(n, capacity)]

    if weights[n - 1] > capacity:
        result = knapsack_memoization(weights, values, capacity, n - 1, memo)
    else:
        include_item = values[n - 1] + knapsack_memoization(weights, values, capacity - weights[n - 1], n - 1, memo)
        exclude_item = knapsack_memoization(weights, values, capacity, n - 1, memo)
        result = max(include_item, exclude_item)

    memo[(n, capacity)] = result
    return result


weights = [5, 10, 15, 22, 25]
values = [30, 40, 45, 77, 90]
capacity = 50
n = len(weights)

result_tabulation = knapsack_tabulation(weights, values, capacity)
print(f"Maximum value using Tabulation: {result_tabulation}")

result_memoization = knapsack_memoization(weights, values, capacity, n)
print(f"Maximum value using Memoization: {result_memoization}")
