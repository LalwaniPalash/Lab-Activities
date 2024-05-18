class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

class Car(Vehicle):
    def __init__(self, make, model, color, num_wheels):
        super().__init__(make, model, color)
        self.num_wheels = num_wheels

def display_vehicle_info(vehicle):
    print("Vehicle Information:")
    print(f"Make: {vehicle.make}")
    print(f"Model: {vehicle.model}")
    print(f"Color: {vehicle.color}")

    if isinstance(vehicle, Car):
        print(f"Number of Wheels: {vehicle.num_wheels}")

vehicle1 = Vehicle("Toyota", "Corolla", "Blue")
display_vehicle_info(vehicle1)

car1 = Car("Tesla", "Model S", "Red", 4)
display_vehicle_info(car1)
