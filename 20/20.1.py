class Employee:
    __name = None

    def __init__(self, name):
        self.__name = name

emp1 = Employee('Ksyu')
emp2 = Employee('Itto')

print(emp1 == emp2) #False