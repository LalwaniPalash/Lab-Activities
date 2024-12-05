def pop_element_from_position(arr, position):
    if position < 0 or position >= len(arr):
        print("Invalid position!")
        return arr  # Return the original array if position is invalid
    
    popped_element = arr.pop(position)
    
    print(f"Array after popping the element {popped_element}: {arr}")
    return arr

arr = [7, 3, 2, 1, 8, 6]
position = 3  # Position of the element to pop (0-based index)
arr = pop_element_from_position(arr, position)
