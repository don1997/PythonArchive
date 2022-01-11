#ex5

#OOP Exercise 5: Define a property that must have the same value
#  for every class instance (object)

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def color(self, color):
        return f"Color:{color}, Name: {self.name}, Max speed: {self.max_speed}, Mileage:{self.mileage} "
class Bus(Vehicle):
    def color(self, color = "white"):
        return super().color(color ="white")

        
class Car(Vehicle):
    def color(self, color = "white"):
        return super().color(color ="white")


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color())

camry = Car("camry", 60, 15)
print(camry.color())