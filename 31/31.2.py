class Employee:
    age = None

    def Age(self, age):
        self.age = age

    def GetAge(self):
        return self.age

    def SetAge(self, age):
        if age < 18:
            print("Error")
        elif age > 65:
            print("Error")
        else:
            self.age = age
            print("Correct")


worker = Employee()
worker.SetAge(98)
worker.SetAge(17)

print(worker.GetAge())