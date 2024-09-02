def reverse(data):
    temp = []
    while data:
        temp.append(data.pop())
    return temp
    
data = [2,4,5,1,6,7,8]
reversed_list = reverse(data)

print(f"Reversed List= {reversed_list}")
