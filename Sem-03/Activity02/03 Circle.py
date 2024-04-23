class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
    	pi = 3.14
    	r2 = self.radius * self.radius
    	print(pi * r2)

c1 = Circle(5)
c1.calcArea()
