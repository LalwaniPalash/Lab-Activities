def knapsack_recursive(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)
    
    include_item = values[n - 1] + knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)
    exclude_item = knapsack_recursive(weights, values, capacity, n - 1)
    
    return max(include_item, exclude_item)

weights = [2, 3, 4]
values = [3, 4, 5]
capacity = 5
n = len(weights)

result = knapsack_recursive(weights, values, capacity, n)
print(f"The maximum value that can be obtained is: {result}")
