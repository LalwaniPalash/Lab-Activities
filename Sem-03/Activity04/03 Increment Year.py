class Student:
    school_name = 1
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def increment_year(cls):
        cls.school_name += 1

s1 = Student("John", "Doe")
s2 = Student("Jane", "Doe")

Student.increment_year()
print(s1.school_name)
print(s2.school_name)
