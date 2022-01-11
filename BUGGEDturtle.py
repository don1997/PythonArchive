#URL: https://stackoverflow.com/questions/60480328/attributeerror-partially-initialized-module-turtle-has-no-attribute-turtle

#weird bug
#Because of the file name which is turtle.py
#it interferes with the turtle library 
#causing it to have the error circular callback
# Python program to draw square
# using Turtle Programming
#ALSO
#needed to install tk
# on pacman not pip #url https://stackoverflow.com/questions/48504746/importerror-libtk8-6-so-cannot-open-shared-object-file-no-such-file-or-direct

import turtle
skk = turtle.Turtle()
 
for i in range(4):
    skk.forward(50)
    skk.right(90)
     
turtle.done()

