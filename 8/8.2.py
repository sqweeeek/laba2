class Student:
    name = None
    surname = None

    def show(self, string):
        if len(string) > 0:
            return string[0].upper() + string[1:]
        else:
            return string

stud = Student()
stud.name = 'Ksyusha'
stud.surname = 'Beloglazova'

print(stud.show(stud.name))