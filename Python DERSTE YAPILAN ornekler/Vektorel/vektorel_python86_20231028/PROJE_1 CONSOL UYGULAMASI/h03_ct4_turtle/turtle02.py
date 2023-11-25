import turtle

def kareciz():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)

def ucgenciz():
    for a in range(3):
        turtle.forward(100)
        turtle.right(120)

def besgenciz():
    for a in range(5):
        turtle.forward(100)
        turtle.right(72)

def cokgenciz(ks,buyukluk):
    turtle.speed(10)
    for b in range(ks):
        turtle.forward(buyukluk)
        turtle.right(360/ks)
    
def menu():
    print(" Çizim menusu")
    print(" 1-Kare çiz")
    print(" 2-Üçgen çiz")
    print(" 3-Çokgen çiz")
    print(" Seçiminiz ne?")
    s = input()
    if s == "1":
        kareciz()
        menu()
    if s == "2":
        ucgenciz()
        menu()
    if s == "3":
        x = int(input("Kaç kenarlı    ?"))
        a = int(input("Kenar büyüklüğü?"))
        cokgenciz(x,a)
        menu()
    
menu()
