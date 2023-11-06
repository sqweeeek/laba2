class Car:
    color = None
    fuel = None
    speed = None
    vladelec = None
    speed = 0

    def go(self):
        self.speeed = 100
    
    def turn(self):
        self.speeed = -100
    
    def stop(self):
        self.speeed = 0

myCar = Car()
myCar.color = "red"
myCar.fuel = 50
myCar.speed = 200
vladelec = "Ksyusha"
yCar.go()
print(myCar.speeed)