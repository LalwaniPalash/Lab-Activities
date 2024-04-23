class Fruit:

	objectsCounter = 0

	def __init__(self, name, size, color):
		self.name = name
		self.size = size
		self.color = color

		Fruit.objectsCounter += 1


f1 = Fruit("Kiwi", "10cm", "Green")
f2 = Fruit("Apple", "15cm", "Red")
f3 = Fruit("Banana", "6cm", "Yellow")
print(f"Total Fruit Objects Created: {Fruit.objectsCounter}")
