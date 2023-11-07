class Student:
    name = None
    surname = None
    def show(self, first_name, last_name):
        initials = first_name[0].upper() + last_name[0].upper()
        return initials

stud = Student()
stud.name = 'Ksyusha'
stud.surname = 'Beloglazova'

print(stud.show(stud.name, stud.surname))