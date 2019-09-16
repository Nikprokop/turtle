import turtle

turtle.shape('turtle')
n = int(input())
len = 50
q =360/n
for i in range(n):
    turtle.forward(len)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(len)
    turtle.right(180 + q)

