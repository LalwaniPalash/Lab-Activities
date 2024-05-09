class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_full_name(self):
        return f"Fullname: {self.firstname} {self.lastname}"

s1 = Student("John", "Doe")
s2 = Student("Jane", "Doe")

print(s1.get_full_name())
print(s2.get_full_name())
