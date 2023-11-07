class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self):
      pass

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getSalary(self):
        return self.__salary

    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age
    def setSalary(self, salary):
        self.__salary = salary

emp = Employee()
emp.setName('Ksyusha')
emp.setAge(17)
emp.setSalary(300000)

print(emp.getName())
print(emp.getAge())
print(emp.getSalary())