def min_coins(candidates, target):
    dp = [float('inf')] * (target + 1)
    
    dp[0] = 0
    
    for amount in range(1, target + 1):
        for coin in candidates:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[target] if dp[target] != float('inf') else -1

if __name__ == "__main__":
    candidates = [1, 2, 5]  # Coin denominations
    target = 11  # Target amount
    
    result = min_coins(candidates, target)
    print(f"The minimum number of coins to make {target} is: {result}")
