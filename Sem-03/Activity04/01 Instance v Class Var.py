class Student:
	school_name = "XYZ"
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

	def show(self):
		print(self.name, self.grade, self.school_name)

s1 = Student("John", 10)
s2 = Student("Jane", 7)

s1.show()
s2.show()

s1.school_name = "ABC"

s1.show()
s2.show()
