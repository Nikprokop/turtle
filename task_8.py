import turtle

turtle.shape('turtle')
n = 20
turtle.penup()
turtle.right(90)
turtle.forward(n/2)
turtle.right(90)
turtle.forward(n/2)
turtle.right(180)
for i in range(10):
    turtle.pendown()
    turtle.forward(n)
    turtle.left(90)
    n +=10
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    n +=10
    turtle.forward(n)
    turtle.left(90)

