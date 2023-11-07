class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self):
        pass

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            raise Exception('age is incorrect')
emp = Employee()
emp.setName('Ksyusha')
emp.setAge(17)
emp.setSalary(300000)

print(emp.getName())
print(emp.getAge())
print(emp.getSalary())