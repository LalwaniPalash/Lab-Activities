import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def closest_pair(points):
    if len(points) < 2:
        return None
    
    min_dist = float('inf')  # Initialize with a large number
    closest_pair = None  # To store the closest pair of points

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])

    return closest_pair

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
result = closest_pair(points)

if result:
    print(f"The closest pair of points is: {result}")
else:
    print("There are fewer than two points.")
