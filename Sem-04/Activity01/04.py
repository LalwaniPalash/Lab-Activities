def find_index(data, element):
    elem_num = 0
    for i in data:
        elem_num+=1
        if i == element:
            return elem_num
    return -1
    
data = [2,4,5,1,6,7,8]
idx = find_index(data, 5)

print(idx)
