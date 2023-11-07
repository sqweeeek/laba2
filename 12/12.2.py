class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)

emp = Employee('Kyusha', 3000000)
emp.show()