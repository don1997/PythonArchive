from turtle import Turtle, Screen
import random


bob = Turtle(shape="turtle")
print(bob)

bob.speed(0)

for i in range(1000):
    value = random.randint(1,360)

    bob.forward(100)
    bob.left(95)
    bob.forward(100)
    bob.rt(95)
    bob.backward(100)
    


screen = Screen()
screen.exitonclick()