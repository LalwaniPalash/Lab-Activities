class Shape:
    def __init__(self):
        print("Shape constructor")

class Color:
    def __init__(self):
        print("Color constructor")

class ColoredShape(Shape, Color):
    def __init__(self, color):
        self.color = color
        super().__init__()

colored_shape = ColoredShape("red")
