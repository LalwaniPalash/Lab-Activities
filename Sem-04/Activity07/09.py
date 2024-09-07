def insertion_sort(arr):
    """
    Sorts a list using the insertion sort algorithm.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    unsorted_list = [64, 25, 12, 22, 11, 90]
    
    print("Original list:")
    print(unsorted_list)
    
    insertion_sort(unsorted_list)
    
    print("Sorted list:")
    print(unsorted_list)

if __name__ == "__main__":
    main()
