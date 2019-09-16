import turtle
import math
turtle.speed(5)

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
turtle.left(90)
D=24
for i in range(10):
    circ1(D)
    circ2(D)
    D+=D/6

