class Employee:
    __name = None

    def __init__(self, name):
        self.__name = name

emp1 = Employee('john') 
emp2 = emp1 
emp2.name = 'eric' 

print(emp1 == emp2) #true