from abc import ABC, abstractmethod

class Shape2D(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def get_info(self):
        print("This is a 2D shape.")

class Rectangle(Shape2D):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Triangle(Shape2D):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

def calculate_and_display_area(shape):
    if hasattr(shape, 'get_info'):
        shape.get_info()
    area = shape.get_area()
    print(f"The area of the shape is: {area}")

rectangle = Rectangle(4, 5)
calculate_and_display_area(rectangle)

triangle = Triangle(3, 6)
calculate_and_display_area(triangle)
