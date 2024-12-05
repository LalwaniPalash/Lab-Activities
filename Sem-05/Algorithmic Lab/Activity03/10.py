def knapsack_tabulation(costs, returns, budget):
    n = len(costs)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + returns[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]
    
    return dp[n][budget]

def knapsack_memoization(costs, returns, budget, n, memo=None):
    if memo is None:
        memo = {}

    if n == 0 or budget == 0:
        return 0
    
    if (n, budget) in memo:
        return memo[(n, budget)]

  if costs[n - 1] > budget:
        result = knapsack_memoization(costs, returns, budget, n - 1, memo)
    else:
        include_item = returns[n - 1] + knapsack_memoization(costs, returns, budget - costs[n - 1], n - 1, memo)
        exclude_item = knapsack_memoization(costs, returns, budget, n - 1, memo)
        result = max(include_item, exclude_item)

    memo[(n, budget)] = result
    return result

costs = [10, 20, 30, 40, 50]
returns = [60, 100, 120, 160, 200]
budget = 100
n = len(costs)

result_tabulation = knapsack_tabulation(costs, returns, budget)
print(f"Maximum return using Tabulation: {result_tabulation}")

result_memoization = knapsack_memoization(costs, returns, budget, n)
print(f"Maximum return using Memoization: {result_memoization}")
