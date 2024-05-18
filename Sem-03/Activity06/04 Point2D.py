import math

class Point2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def translate(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distance_to(self, other_point):
        dx = other_point.get_x() - self.__x
        dy = other_point.get_y() - self.__y
        return math.sqrt(dx**2 + dy**2)

point1 = Point2D(3, 4)
point2 = Point2D(6, 8)

print(f"Coordinates of point1: ({point1.get_x()}, {point1.get_y()})")
print(f"Coordinates of point2: ({point2.get_x()}, {point2.get_y()})")

point1.translate(2, -1)
print(f"New coordinates of point1 after translation: ({point1.get_x()}, {point1.get_y()})")

distance = point1.distance_to(point2)
print(f"Distance between point1 and point2: {distance:.2f}")
