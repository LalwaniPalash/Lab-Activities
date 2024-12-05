def count_occurrences_with_builtin(arr, element):
    return arr.count(element)

arr = [7, 3, 2, 1, 8, 6, 3, 3, 5]
element = 3
print(f"Occurrences of {element} using built-in function:", count_occurrences_with_builtin(arr, element))

-----------------

def count_occurrences_without_builtin(arr, element):
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count

arr = [7, 3, 2, 1, 8, 6, 3, 3, 5]
element = 3
print(f"Occurrences of {element} without using built-in function:", count_occurrences_without_builtin(arr, element))
