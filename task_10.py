import turtle
import math
turtle.speed(10)
def circ1(R):
    a = 2 * R * math.sin(math.pi/360)
    for i in range(360):
        turtle.forward(a)
        turtle.left(1)

def circ2(R):
    a = 2 * R * math.sin(math.pi/360)
    for i in range(360):
        turtle.forward(a)
        turtle.right(1)
D=40
for i in range(3):
    circ1(D)
    circ2(D)
    turtle.left(60)