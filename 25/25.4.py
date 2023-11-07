class Employee:
    __name = None
    surname = None
  

    def getName(self):
        return self.__name

    def __init__(self, name, surname):
        self.__name = name
        self.surname = surname



class EmployeeCollection:
    __employees = None

    def __init__(self):
        self.__employees= []

    def add(self, emp):
        self.__employees.append(emp)

    def show(self):
        for employee in self.__emps:
            print(employee.getName())

    def sum_sal(self):
        summ_sal = 0
        for employee in self.__employeess:
            summ_sal += int(employee.salary)

    def mid_sal(self, summ_sal):
        total = summ_sal / len(self.__employees)