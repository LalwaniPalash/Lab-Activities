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

if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    
    strip = [(2, 3), (3, 4), (5, 1), (12, 10), (12, 30)]  # example strip
    
    delta = 10
    
    closest_pair_points, distance = closest_in_strip(strip, delta)
    
    if closest_pair_points:
        print(f"The closest pair in the strip is: {closest_pair_points}")
        print(f"The distance between them is: {distance}")
    else:
        print("No pair found within the strip.")
