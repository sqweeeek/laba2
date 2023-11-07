class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary