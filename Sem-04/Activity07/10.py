def quick_sort(arr):
    """
    Sorts a list using the quick sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def main():
    unsorted_list = [64, 25, 12, 22, 11, 90]
    
    print("Original list:")
    print(unsorted_list)
    
    sorted_list = quick_sort(unsorted_list)
    
    print("Sorted list:")
    print(sorted_list)

if __name__ == "__main__":
    main()
