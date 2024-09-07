def bubble_sort(arr):
    """
    Sorts a list using the bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break

def main():
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original list:")
    print(unsorted_list)
    
    bubble_sort(unsorted_list)
    
    print("Sorted list:")
    print(unsorted_list)

if __name__ == "__main__":
    main()
