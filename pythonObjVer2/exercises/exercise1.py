#OOP Exercise 1
#URL: https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes
#Create a class with instance attribute

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(500, 10000)

print(modelx.max_speed, modelx.mileage)