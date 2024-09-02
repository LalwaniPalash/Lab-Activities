def count(data):
    count = 0
    for i in data:
        count+=1
    return count
    
data = [2,4,5,1,6,7,8]
elements = count(data)

print(f"Total Elements = {elements}")
