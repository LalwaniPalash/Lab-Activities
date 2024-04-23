class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def honk_horn(self):
        print("Honk Honk!")

c1 = Car("black", "BMW")
c1.honk_horn()
