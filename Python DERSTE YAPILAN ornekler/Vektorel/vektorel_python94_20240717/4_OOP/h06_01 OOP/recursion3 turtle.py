import turtle as t
a = 200
def ciz():
    global a
    t.forward(a)
    t.right(90)
    a -=5
    if a > 30 : ciz()
    
ciz()
input()