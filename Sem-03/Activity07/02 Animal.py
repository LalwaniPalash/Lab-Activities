class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement the make_sound() method.")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
