import random
import turtle

def kareciz(uzunluk,renk):
    turtle.up()
    turtle.goto(random.randint(-200,200),random.randint(-200,200))
    turtle.down()
    turtle.color(renk)
    for a in range(4):
        turtle.forward(uzunluk)
        turtle.right(90)

u = random.randint(50,200)
print(u)
renkler = ['red','blue']

for b in range (10):
    kareciz(random.randint(50,200),random.choice(renkler))
