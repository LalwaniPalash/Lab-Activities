def intersection_lists(list1, list2):
    intersection = []
    for element in list1:
        if element in list2:
            already_added = False
            for e in intersection:
                if e == element:
                    already_added = True
                    break
            if not already_added:
                intersection.append(element)
    
    return intersection

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(intersection_lists(list1, list2))
