import random
#import turtle
from turtle import *

speed(100)

# turtle.goto(100,-200)

renkler=["red","green","blue","olive"]

#def forward():
#    print("merhaba")
    
def ciz(kenar,buyukluk):
    for a in range(kenar):
        forward(buyukluk)
        right(360/kenar)

for a in range(15):
    #print(random.choice(renkler))
    penup()
    xx = random.randint(-200,200)
    yy = random.randint(-200,200)
    goto(xx,yy)
    pendown()
    color(random.choice(renkler))
    b = random.randint(50,200)
    ciz (random.randint(3,7),b)

