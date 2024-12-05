def insert_multiple_elements(arr, index, elements):
    """
    Inserts multiple elements at the specified index in the array.
    
    Parameters:
        arr (list): The list in which elements are inserted.
        index (int): The index at which elements should be inserted.
        elements (list): List of elements to be inserted.
    """
    for element in elements:
        arr.insert(index, element) 
        index += 1 

arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

elements_to_insert = [10, 20, 30]
insert_multiple_elements(arr, 2, elements_to_insert)

print("Array after inserting elements:", arr)
