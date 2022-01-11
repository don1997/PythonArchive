#OOP Exercise 3
#URL: https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes
#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:
    def __init__(self, max_speed, mileage):
      
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(500, 10000)

class Bus(Vehicle):
    pass

skoolbus = Bus(10, 100)
print(skoolbus.max_speed, skoolbus.mileage)
