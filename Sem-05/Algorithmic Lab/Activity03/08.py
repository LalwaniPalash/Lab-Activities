from itertools import combinations

def knapsack_bruteforce(weights, values, capacity):
    n = len(weights)
    max_value = 0  # Variable to store the maximum value
    
    for subset_size in range(1, n + 1):  # from size 1 to size n
        for subset in combinations(range(n), subset_size):
            total_weight = sum(weights[i] for i in subset)
            total_value = sum(values[i] for i in subset)
            
            if total_weight <= capacity:
                max_value = max(max_value, total_value)
    
    return max_value

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 5

result = knapsack_bruteforce(weights, values, capacity)
print(f"The maximum value that can be obtained is: {result}")
