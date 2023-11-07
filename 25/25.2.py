class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeesCollection:
    def __init__(self):
        self.employees = []

    __employees = None

    def __init__(self):
        self.__employees = []

    def add(self, emp):
        self.__employees.append(emp)