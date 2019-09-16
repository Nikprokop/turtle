import turtle
import math

def circ(R):
    a = 2 * R * math.sin(math.pi/360)
    for i in range(180):
        turtle.forward(a)
        turtle.right(1)
D = 50
turtle.penup()
turtle.forward(-250)
turtle.pendown()
turtle.left(90)

for i in range(5):
    circ(D)
    circ(D/5)
