def linear_search(arr, target):
    """Performs linear search on the list."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def binary_search(arr, target):
    """Performs binary search on the sorted list."""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

def main():
    unsorted_list = [4, 2, 7, 1, 9, 3]
    sorted_list = sorted(unsorted_list)
    target = 7
    
    print("Performing Linear Search...")
    index = linear_search(unsorted_list, target)
    if index != -1:
        print(f"Linear Search: Target {target} found at index {index}.")
    else:
        print(f"Linear Search: Target {target} not found.")
    
    print("Performing Binary Search...")
    index = binary_search(sorted_list, target)
    if index != -1:
        print(f"Binary Search: Target {target} found at index {index} in the sorted list.")
    else:
        print(f"Binary Search: Target {target} not found in the sorted list.")

if __name__ == "__main__":
    main()
