def alternate_lists(list1, list2):
    result = []
    min_length = len(list1) if len(list1) < len(list2) else len(list2)
    for i in range(min_length):
        result.append(list1[i])
        result.append(list2[i])
    for i in range(min_length, len(list1)):
        result.append(list1[i])
    for i in range(min_length, len(list2)):
        result.append(list2[i])
    return result

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6]
print(alternate_lists(list1, list2))
