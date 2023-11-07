class Position:
    def __init__(self, title):
        self.title = title


class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


position = None
department = None

emp = Employee("Ksyusha", position, department)
print("name:", emp.name)
print("position:", emp.position)
print("department:", emp.department)