def length_with_builtin(arr):
    return len(arr)

arr = [1, 2, 3, 4, 5]
print("Length of array using built-in function:", length_with_builtin(arr))

------------------------

def length_without_builtin(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

arr = [1, 2, 3, 4, 5]
print("Length of array without using built-in function:", length_without_builtin(arr))
