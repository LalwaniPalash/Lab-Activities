def remove_duplicates(lst):
    unique_elements = []
    for element in lst:
        is_duplicate = False
        for unique in unique_elements:
            if unique == element:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_elements.append(element)
    return unique_elements

lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))
