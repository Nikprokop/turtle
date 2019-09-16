import turtle
import math

turtle.shape('turtle')
turtle.speed(2)
def mnog(n,a):
    if n != 0:
        turtle.left((180/n))
        for i in range(n):
            turtle.forward(a)
            turtle.left((360/n))
        turtle.right((180/n))



len = 50
R = len/(2 * math.sin(math.pi/3))
k = int(input())
for c in range(3,k+3):
    turtle.left(90)
    turtle.pendown()
    mnog(c,len)
    turtle.right(90)
    len+=14
    R0 = R
    R = len/(2 * math.sin(math.pi/(c+1)))
    turtle.penup()
    turtle.forward(R-R0)
