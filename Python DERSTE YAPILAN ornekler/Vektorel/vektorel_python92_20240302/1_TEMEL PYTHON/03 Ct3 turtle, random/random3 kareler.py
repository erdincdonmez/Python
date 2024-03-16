import turtle
import random
renkler=["red","blue","magenta","yellow","pink"]
turtle.speed(10)
for xx in range(random.randint(1,10)):
    turtle.penup()
    # turtle.goto(-200,200)
    turtle.goto(random.randint(-400,400),random.randint(-400,400))
    turtle.pendown()
    ku = random.randint(50,200)
    for a in range(4):
        turtle.color(random.choice(renkler))
        turtle.forward(ku)
        turtle.right(90)    
input()
