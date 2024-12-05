def find_lowest_value(arr):
    lowest = arr[0]
    
    for num in arr:
        if num < lowest:
            lowest = num
            
    return lowest

arr = [7, 3, 2, 1, 8, 6]
print("Lowest value without using built-in function:", find_lowest_value(arr))

------------------------------

def find_lowest_value_with_builtin(arr):
    return min(arr)

arr = [7, 3, 2, 1, 8, 6]
print("Lowest value using built-in function:", find_lowest_value_with_builtin(arr))
