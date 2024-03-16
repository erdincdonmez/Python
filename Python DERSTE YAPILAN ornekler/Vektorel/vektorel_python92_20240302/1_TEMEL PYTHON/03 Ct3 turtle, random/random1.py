import turtle
import random
renkler=["red","blue","magenta","yellow","pink"]
for a in range(5):
    # print(renkler[a])
    # turtle.color(renkler[a])
    turtle.color(random.choice(renkler))
    turtle.forward(100)
    turtle.right(90)
    
input()