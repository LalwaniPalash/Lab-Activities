class Person:
    def __init__(self, name, age=25, city="Unknown"):
        self.name = name
        self.age = age
        self.city = city

person1 = Person("John", 30, "New York")
print("Person 1 Attributes:")
print("Name:", person1.name)
print("Age:", person1.age)
print("City:", person1.city)
print()

person2 = Person("Alice")
print("Person 2 Attributes:")
print("Name:", person2.name)
print("Age:", person2.age) 
print("City:", person2.city) 
