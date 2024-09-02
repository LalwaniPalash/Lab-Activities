def find_min(data):
    min = data[0]
    for i in data:
        if i < min:
            min = i
    return min
    
def find_max(data):
    max = data[0]
    for i in data:
        if i > max:
            max = i
    return max
    
data = [2,4,5,1,6,7,8]
min = find_min(data)
max = find_max(data)

print(f"Min = {min}, Max = {max}")
