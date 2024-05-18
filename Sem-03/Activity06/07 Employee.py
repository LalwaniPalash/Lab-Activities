class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, department, salary, num_employees_managed):
        super().__init__(name, department, salary)
        self.num_employees_managed = num_employees_managed

    def calculate_bonus(self):
        return self.num_employees_managed * 1000

def process_payroll(employee):
    print("Employee Information:")
    print(f"Name: {employee.name}")
    print(f"Department: {employee.department}")
    print(f"Salary: ${employee.salary:.2f}")

    if isinstance(employee, Manager):
        bonus = employee.calculate_bonus()
        print(f"Bonus: ${bonus:.2f}")

employee1 = Employee("John Doe", "Engineering", 60000)
process_payroll(employee1)

manager1 = Manager("Jane Smith", "Management", 80000, 5)
process_payroll(manager1)
