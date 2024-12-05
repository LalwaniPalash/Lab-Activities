import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def closest_in_strip(strip, delta):
    min_dist = delta
    closest_pair = None
    
    strip.sort(key=lambda p: p[1])
    
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (strip[i], strip[j])
    
    return closest_pair, min_dist

def closest_pair_rec(points_sorted_by_x, points_sorted_by_y):
    n = len(points_sorted_by_x)
    
    if n <= 3:
        min_dist = float('inf')
        closest_pair = None
        for i in range(n):
            for j in range(i + 1, n):
                dist = euclidean_distance(points_sorted_by_x[i], points_sorted_by_x[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (points_sorted_by_x[i], points_sorted_by_x[j])
        return closest_pair, min_dist
    
    mid = n // 2
    left_sorted_by_x = points_sorted_by_x[:mid]
    right_sorted_by_x = points_sorted_by_x[mid:]
    
    left_sorted_by_y = [p for p in points_sorted_by_y if p in left_sorted_by_x]
    right_sorted_by_y = [p for p in points_sorted_by_y if p in right_sorted_by_x]
    
    left_closest, left_dist = closest_pair_rec(left_sorted_by_x, left_sorted_by_y)
    right_closest, right_dist = closest_pair_rec(right_sorted_by_x, right_sorted_by_y)
    
    if left_dist < right_dist:
        closest_pair = left_closest
        min_dist = left_dist
    else:
        closest_pair = right_closest
        min_dist = right_dist
    
    strip = [p for p in points_sorted_by_y if abs(p[0] - points_sorted_by_x[mid][0]) < min_dist]
    strip_closest, strip_dist = closest_in_strip(strip, min_dist)
    
    if strip_closest:
        return strip_closest, strip_dist
    else:
        return closest_pair, min_dist

def closest_pair(points):
    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    
    points_sorted_by_y = sorted(points, key=lambda p: p[1])
    
    return closest_pair_rec(points_sorted_by_x, points_sorted_by_y)

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest_pair_points, distance = closest_pair(points)

if closest_pair_points:
    print(f"The closest pair of points is: {closest_pair_points}")
    print(f"The distance between them is: {distance}")
else:
    print("There are fewer than two points.")
