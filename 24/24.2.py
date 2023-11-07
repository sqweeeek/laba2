class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return f"{self.__salary}$"


empl = [
    Employee('john', 0),
    Employee('eric', 50000000),
    Employee('kyle', 45667232),
]
for employee in empl:
    print("Имя:" +employee.getName()+ " Зарплата: " +employee.getSalary())