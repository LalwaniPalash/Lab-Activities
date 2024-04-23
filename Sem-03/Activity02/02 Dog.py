class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof Woof!")

    def play_fetch(self):
    	print(f"{self.name} plays fetch.")

d1 = Dog("Cooper", "Labrador")
d1.bark()
d1.play_fetch()
