def find_index_with_builtin(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1  # Return -1 if the element is not found

arr = [7, 3, 2, 1, 8, 6, 3, 5]
element = 3
print(f"Index of {element} using built-in function:", find_index_with_builtin(arr, element))

-----------

def find_index_without_builtin(arr, element):
    for index, value in enumerate(arr):
        if value == element:
            return index
    return -1  # Return -1 if the element is not found

arr = [7, 3, 2, 1, 8, 6, 3, 5]
element = 3
print(f"Index of {element} without using built-in function:", find_index_without_builtin(arr, element))
