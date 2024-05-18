class Student:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__grades = []

    def add_grade(self, grade):
        if 0.0 <= grade <= 100.0:
            self.__grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Invalid grade. Grade must be between 0.0 and 100.0.")

    def get_average_grade(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

student = Student("John", "Doe")
student.add_grade(85.5)
student.add_grade(92.0)
student.add_grade(78.5)

print(f"Average grade: {student.get_average_grade():.2f}")
