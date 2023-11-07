class Employee():

    name = None
    age = None
    salary = None

    def show(self,name,salary):
        return name + ' ' + salary
    
emp = Employee()
emp.name = "Ksyusha"
emp.salary = 3000000
print(emp.name, emp.salary)