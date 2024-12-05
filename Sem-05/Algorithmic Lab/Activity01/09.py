import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

if __name__ == "__main__":
    point1 = Point(2, 3)
    point2 = Point(5, 7)

    distance = point1.distance_to(point2)
    
    print(f"The Euclidean distance between {point1} and {point2} is: {distance}")
