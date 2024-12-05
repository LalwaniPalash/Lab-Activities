def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    
    items = []
    for i in range(n):
        items.append((values[i], weights[i], values[i] / weights[i]))
    
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    fraction_taken = []

    for value, weight, ratio in items:
        if remaining_capacity == 0:
            break  # Stop if the knapsack is full
        
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
            fraction_taken.append((value, weight, 1))  # Full item taken
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0  # Knapsack is full now
            fraction_taken.append((value * fraction, remaining_capacity, fraction))  # Fractional item taken
    
    return total_value, fraction_taken


weights = [5, 4, 7, 3]
values = [20, 24, 35, 21]
capacity = 10

total_value, fraction_taken = fractional_knapsack(weights, values, capacity)

print(f"Maximum value in the knapsack: {total_value}")
print("Fraction details (Value taken, Weight, Fraction of item taken):")
for value_taken, weight, fraction in fraction_taken:
    print(f"Value: {value_taken:.2f}, Weight: {weight}, Fraction: {fraction:.2f}")
