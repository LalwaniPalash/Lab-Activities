def sum_list(data):
    sum = 0
    for i in data:
        sum += i
    return sum
    
data = [2,4,5,1,6,7,8]
sum = sum_list(data)

print(sum)
