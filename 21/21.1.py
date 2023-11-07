class Student:
  pass


class Employee:
  pass

emp = Employee()
print(isinstance(emp, Employee)) #True
print(isinstance(emp, Student)) #False