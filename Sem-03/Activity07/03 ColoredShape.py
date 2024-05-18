class Shape:
    def define_shape(self):
        raise NotImplementedError("Subclasses must implement the define_shape() method.")

class Color:
    def set_color(self, color):
        raise NotImplementedError("Subclasses must implement the set_color() method.")

class ColoredShape(Shape, Color):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def define_shape(self):
        return f"The shape is {self.shape}."

    def set_color(self, color):
        self.color = color
