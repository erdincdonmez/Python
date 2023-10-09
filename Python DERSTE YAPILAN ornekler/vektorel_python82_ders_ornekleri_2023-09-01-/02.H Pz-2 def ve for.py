import turtle as t
buyukluk = int(input("Büyüklük ne olsun: ")) 
tekrar   = int(input("kaç tane olsun   : ")) 
def kareciz():
    for k in range(4):
        t.forward(buyukluk)
        t.right(90)
def ucgenciz():    
    for k in range(3):
        t.forward(buyukluk)
        t.right(120)
for b in range(tekrar):
    kareciz()
    t.forward(buyukluk)
    ucgenciz()
    t.forward(buyukluk)
    t.left(360/tekrar)
input()