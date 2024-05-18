def calculate_area(shape):
    if hasattr(shape, 'area') and callable(shape.area):
        return shape.area()
    else:
        raise AttributeError("Object does not have a valid area method")

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

square = Square(5)
circle = Circle(3)

print("Area of square:", calculate_area(square))
print("Area of circle:", calculate_area(circle))
