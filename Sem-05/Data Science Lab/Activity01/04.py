def highest_product_pair(arr):
    if len(arr) < 2:
        return None  # Return None if there are less than two elements

    max1 = max2 = float('-inf')  # The two largest numbers
    min1 = min2 = float('inf')   # The two smallest numbers

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    product_max_pair = max1 * max2
    product_min_pair = min1 * min2

    if product_max_pair >= product_min_pair:
        return (max1, max2), product_max_pair
    else:
        return (min1, min2), product_min_pair

arr = [1, 2, 3, 4, 7, 0, 8, 4]
pair, product = highest_product_pair(arr)
print(f"The pair with the highest product is {pair} with product = {product}")
