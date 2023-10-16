import turtle as t
t.speed(100)
def kare(x):    
    if x < 10 : return x
    else:
        t.penup()
        t.forward(5)
        t.right(90)
        t.forward(5)
        t.left(90)
        t.pendown()
        for i in range (4):
            t.forward(x)
            t.right(90)
        return kare(x-10)

aaa = int (input("Karenin uzun kenarı ne kadar?"))
t.penup()
t.goto(-(aaa//2),(aaa//2))
t.pendown()
kare(aaa)
