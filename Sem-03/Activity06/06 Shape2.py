from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

def print_area(shape):
    area = shape.calculate_area()
    print(f"Area of the shape: {area:.2f}")

square = Square(5)
print_area(square)

circle = Circle(3)
print_area(circle)
