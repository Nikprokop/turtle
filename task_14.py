import turtle
import math

def gr(n, D):
    for i in range(1,n+1):
        if i % 2 != 0:
            turtle.forward(-D)
            turtle.right(180/n)
        if i % 2 == 0:
            turtle.forward(D)
            turtle.right(180/n)
gr(5,100)
turtle.penup()
turtle.forward(-100)
turtle.pendown()
gr(11,100)