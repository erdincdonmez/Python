"""
import turtle as t
t.forward(100)
t.right(90)
"""
import turtle

x = turtle.Turtle()
y = turtle.Turtle()
x.forward(100)

y.penup()
y.goto(100,100)
y.pendown()
y.forward(100)
