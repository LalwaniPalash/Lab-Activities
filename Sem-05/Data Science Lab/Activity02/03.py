def median_with_builtin(arr):
    sorted_arr = sorted(arr)
    
    n = len(sorted_arr)
    
    if n % 2 != 0:
        return sorted_arr[n // 2]
    else:
        mid1, mid2 = sorted_arr[n // 2 - 1], sorted_arr[n // 2]
        return (mid1 + mid2) / 2

arr = [3, 1, 2, 5, 4]
print("Median using built-in functions:", median_with_builtin(arr))

#------------------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def median_without_builtin(arr):
    bubble_sort(arr)
    
    n = len(arr)
    
    if n % 2 != 0:
        return arr[n // 2]
    else:
        mid1, mid2 = arr[n // 2 - 1], arr[n // 2]
        return (mid1 + mid2) / 2

arr = [3, 1, 2, 5, 4]
print("Median without using built-in functions:", median_without_builtin(arr))
