
from turtle import *
renk = ["red","green","blue","yellow"]

speed(10)
for x in range(36):
    for y in range(4):
        forward(100)
        left(90)
        color(renk[y%4])
    right(10)

