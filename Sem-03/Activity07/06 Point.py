import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __gt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def __le__(self, other):
        return self.distance_from_origin() <= other.distance_from_origin()

    def __ge__(self, other):
        return self.distance_from_origin() >= other.distance_from_origin()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

point1 = Point(3, 4)
point2 = Point(-2, 6)
point3 = Point(5, -5)

print("point1 < point2:", point1 < point2)   # Output: True
print("point1 > point3:", point1 > point3)   # Output: False
print("point2 <= point3:", point2 <= point3) # Output: False
print("point2 >= point3:", point2 >= point3) # Output: True
print("point1 == point3:", point1 == point3) # Output: False
print("point1 != point2:", point1 != point2) # Output: True
