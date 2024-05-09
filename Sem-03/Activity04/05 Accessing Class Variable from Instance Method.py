class Student:
    school_name = 1
    
    def __init__(self, firstname, lastname, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade
        
    @staticmethod
    def calculate_average_grade(students):
        total_grade = sum(student.grade for student in students)
        average_grade = total_grade / len(students)
        return average_grade, Student.school_name

john = Student("John", "Doe", 85)
jane = Student("Jane", "Doe", 90)

average_grade, school_name = Student.calculate_average_grade([john, jane])
print("Average Grade:", average_grade)
print("School Name:", school_name)
