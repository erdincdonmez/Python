import turtle as t

t.fillcolor("red")

t.begin_fill()
for a in range (4):
    t.forward(100)
    t.right(90)

t.end_fill()

t.penup()
t.goto(0,120)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
for a in range (4):
    t.forward(100)
    t.right(90)
t.end_fill()
