class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.width * self.width

rectangle = Rectangle(4, 5)
square = Square(4)

print("Area of Rectangle:", rectangle.area())
print("Area of Square:", square.area())
