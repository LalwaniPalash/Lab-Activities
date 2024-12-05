import math

def euclidean_distance(p1, p2):
    """
    Calculate the Euclidean distance between two points p1 and p2.
    p1 and p2 are tuples in the form (x, y).
    """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def closest_pair(points):
    """
    Find the closest pair of points using brute force method.
    points: List of tuples (x, y) representing points in 2D space.
    Returns the closest pair of points and the distance between them.
    """
    if len(points) < 2:
        return None
    
    min_dist = float('inf')  # Initialize with a very large number
    closest_pair = None  # To store the closest pair of points

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])

    return closest_pair, min_dist

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest_pair_points, distance = closest_pair(points)

if closest_pair_points:
    print(f"The closest pair of points is: {closest_pair_points}")
    print(f"The distance between them is: {distance}")
else:
    print("There are fewer than two points.")
