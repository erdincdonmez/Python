
from turtle import *
from random import *
renk = ["red","green","blue","yellow"]

speed(10)
for a in range(20,200,10):
    penup()
    goto(randint(-200,200),randint(-200,200))
    pendown()
    zx = randint(50,150)
    kenar = randint(3,10)
    color(choice(renk))
    for x in range(kenar):
        forward(zx)
        right(360/kenar)


