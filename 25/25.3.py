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
def list_employees(self):
        for employee in self.employees:
            print("Имя:" +employee.getName()+ " Зарплата: " +employee.getSalary())

def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total