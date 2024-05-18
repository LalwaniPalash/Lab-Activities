from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, dimensions):
        self.__dimensions = dimensions

    @abstractmethod
    def calculate_area(self):
        pass

    def get_dimensions(self):
        return self.__dimensions

class Square(Shape):
    def __init__(self, side_length):
        super().__init__([side_length])

    def calculate_area(self):
        side_length = self.get_dimensions()[0]
        return side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        super().__init__([radius])

    def calculate_area(self):
        radius = self.get_dimensions()[0]
        return math.pi * (radius ** 2)

square = Square(4)
print(f"Area of square: {square.calculate_area()}")

circle = Circle(3)
print(f"Area of circle: {circle.calculate_area()}")
