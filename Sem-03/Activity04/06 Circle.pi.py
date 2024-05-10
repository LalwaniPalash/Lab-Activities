class Circle:
    PI = 3.14159
    
    def __init__(self, radius):
        self.radius = radius

circle1 = Circle(5)
print(circle1.PI)

print(Circle.PI)

Circle.PI = 3.14
print(circle1.PI)
print(Circle.PI) 


# Mutability: Class variables in Python are mutable, meaning they can be modified. However, constants like math.pi are immutable and cannot be modified. Once math.pi is imported from the math module, its value cannot be changed.
# Scope: PI within the Circle class has class scope, meaning it's accessible both from instances and the class itself. On the other hand, math.pi has module scope; it's accessible only by importing the math module.
