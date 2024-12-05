def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    
    items = []
    for i in range(n):
        items.append((values[i], weights[i], values[i] / weights[i]))
    
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for value, weight, ratio in items:
        if remaining_capacity == 0:
            break  # If the knapsack is full, stop
        
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += value * (remaining_capacity / weight)
            remaining_capacity = 0  # The knapsack is full now
    
    return total_value

weights = [10, 30, 20, 50]
values = [40, 30, 80, 70]
capacity = 60

result = fractional_knapsack(weights, values, capacity)
print(f"Maximum value in the knapsack: {result}")
