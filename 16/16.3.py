class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age


emp = Employee('Ksyusha', 3000000, 17)
print(emp.getName())
print(emp.getSalary())
print(emp.getAge())