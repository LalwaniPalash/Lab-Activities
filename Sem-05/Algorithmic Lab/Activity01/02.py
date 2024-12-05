def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

index = binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")