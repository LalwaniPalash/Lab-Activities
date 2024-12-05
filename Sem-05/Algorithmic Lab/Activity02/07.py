def min_coins(coins, amount):
    if amount == 0:
        return 0
    
    if amount < 0:
        return float('inf')  # Represents an invalid state
    
    min_coins_required = float('inf')
    
    for coin in coins:
        result = min_coins(coins, amount - coin)
        
        if result != float('inf'):
            min_coins_required = min(min_coins_required, result + 1)
    
    return min_coins_required

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    result = min_coins(coins, amount)
    
    if result == float('inf'):
        print(f"Cannot make the amount {amount} with the given coins.")
    else:
        print(f"The minimum number of coins needed to make {amount} is: {result}")
