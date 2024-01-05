from turtle import *
import random as r

xxx = ["red","blue","yellow"]
color("red")
speed(10)
for b in range(10):
    penup()
    goto(r.randint(-100,100),r.randint(-150,150))
    pendown()
    color(r.choice(xxx))
    for b in range (4):
        
        forward(100)
        right(90)

