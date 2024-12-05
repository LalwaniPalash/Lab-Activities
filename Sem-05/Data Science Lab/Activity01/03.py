def contains_duplicates_with_builtin(arr):
    return len(arr) != len(set(arr))

arr = [7, 3, 2, 1, 8, 6, 3]
print("Contains duplicates using built-in function:", contains_duplicates_with_builtin(arr))

-----------------

def contains_duplicates_without_builtin(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

arr = [7, 3, 2, 1, 8, 6, 3]
print("Contains duplicates without using built-in function:", contains_duplicates_without_builtin(arr))
