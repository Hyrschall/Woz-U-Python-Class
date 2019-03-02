# Lesson 8 Class Inheritance and Polymorphism
# Part 1


class Employee:
    """Employee class"""

    def __init__(self, name, salary, hire_date):
        self.name = str(name)
        self.salary = int(salary)
        self.hire_date = str(hire_date)

    def get_name(self):
        print('Hi! My name is', self.name)

    def get_salary(self):
        print('I make', self.salary, 'per year')

    def get_hired(self):
        print('I was hired on ', self.hire_date)


class Engineer(Employee):
    """Engineer sub class"""

    def __init__(self, name, salary, hire_date):
        super().__init__(name, salary, hire_date)


main_employee = Employee('John Doe', 100000, '01/05/1998')
engineer_employee = Engineer('Jane Smith', 75000, '03/15/2000')

main_employee.get_name()
engineer_employee.get_salary()
