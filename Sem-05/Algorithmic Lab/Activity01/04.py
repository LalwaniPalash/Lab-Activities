def closest_pair(arr):
    if len(arr) < 2:
        return None
    
    min_diff = float('inf') 
    closest_pair = None 

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            
            if diff < min_diff:
                min_diff = diff
                closest_pair = (arr[i], arr[j])

    return closest_pair

arr = [13, 17, 11, 5, 22]
result = closest_pair(arr)

if result:
    print(f"The closest pair of points is: {result}")
else:
    print("The list has fewer than 2 elements, so no pair exists.")
