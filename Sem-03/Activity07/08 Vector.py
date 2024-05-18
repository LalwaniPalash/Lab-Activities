class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

vector1 = Vector(3, 4)
vector2 = Vector(-1, 6)

resultant_vector = vector1 + vector2

print("Resultant Vector (x, y):", resultant_vector.x, resultant_vector.y)  # Output: Resultant Vector (x, y): 2 10
