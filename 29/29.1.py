class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Employee(User):
    pass

emp = Employee()
emp.setName('Ksyuha')

print(emp.getName())