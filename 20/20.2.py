class Employee:
    __name = None

    def __init__(self, name):
        self.__name = name

emp1 = Employee('john')
emp2 = Employee('john')

print(emp1 == emp1) #true