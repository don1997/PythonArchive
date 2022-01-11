from turtle import Turtle, Screen

bob = Turtle(shape="turtle")
print(bob)

#adds color
bob.color("blue", "red")

#begins filling
bob.begin_fill()

bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

#ends filling 
bob.end_fill()


screen = Screen()
screen.exitonclick()