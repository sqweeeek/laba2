class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
     
    def show(self):
        salary10 = self.salary*1.1
        print(int(salary10))   
emp = Employee('Kyusha', 3000000)
emp.show()