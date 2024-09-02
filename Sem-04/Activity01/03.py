def reverse(data):
    temp = []
    while data:
        temp.append(data.pop())
    data[:] = temp
    
data = [2,4,5,1,6,7,8]
reverse(data)

print(f"Reversed List= {data}")
