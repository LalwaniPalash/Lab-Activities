def selection_sort(arr):
    """
    Sorts a list using the selection sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    unsorted_list = [64, 25, 12, 22, 11, 90]
    
    print("Original list:")
    print(unsorted_list)
    
    selection_sort(unsorted_list)
    
    print("Sorted list:")
    print(unsorted_list)

if __name__ == "__main__":
    main()
