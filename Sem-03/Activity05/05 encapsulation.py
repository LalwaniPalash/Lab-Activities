class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

    def display_employee_info(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")

emp = Employee("John Doe", 50000)

emp.display_employee_info() 

emp.set_name("Jane Doe")
emp.set_salary(60000)
emp.display_employee_info()

emp.set_salary(-1000)
