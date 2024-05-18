import math

class GeometricFigure:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        print("This is a geometric figure.")

class Square(GeometricFigure):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

class Rectangle(Square):
    def __init__(self, name, width, height):
        super().__init__(name, width)
        self.height = height

    def calculate_area(self):
        return self.side_length * self.height

class Circle(GeometricFigure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

def display_figure_info(figure):
    if hasattr(figure, 'get_info'):
        figure.get_info()

    if isinstance(figure, (Square, Rectangle, Circle)):
        area = figure.calculate_area()
        print(f"The area of {figure.name} is: {area:.2f}")

square = Square("Square", 5)
display_figure_info(square)

rectangle = Rectangle("Rectangle", 4, 6)
display_figure_info(rectangle)

circle = Circle("Circle", 3)
display_figure_info(circle)
