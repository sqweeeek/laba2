class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname


employee = Employee("Camera", "Woman", 10000000000000)
print(employee.get_name())
print(employee.get_surname())
print(employee.get_salary())

employee.set_name("Itto")
employee.set_surname("Itadori")
employee.set_salary(500)

print(employee.get_name())
print(employee.get_surname())
print(employee.get_salary())