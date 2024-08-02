import turtle

renkler = ["cyan","red","yellow","olive","blue","green"]
turtle.speed(10)
for x in range(20,300,1):
    turtle.color(renkler[x%6])
    turtle.forward(x)
    turtle.right(20)

input()
