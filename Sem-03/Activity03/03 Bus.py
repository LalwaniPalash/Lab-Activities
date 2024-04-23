class Vehicle:
	def __init__(self, name, maxSpeed, mileage):
		self.name = name
		self.maxSpeed = maxSpeed
		self.mileage = mileage

bus = Vehicle("Bus", "120kmph", "15kmpl")

print(bus.name)
print(bus.maxSpeed)
print(bus.mileage)
