import turtle
def altigen(rnk):
    turtle.color(rnk)
    for abc in range(6):
        turtle.forward(100)
        turtle.right(60)

def ucgen():
    for abc in range(3):
        turtle.forward(100)
        turtle.right(120)

def kare():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)
    
def cizimmenu():
    ##print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║  ÇİZİMLER           ║")
    print("║                     ║")
    print("║  1-Kare çiz         ║")
    print("║  2-Üçgen            ║")
    print("║  3-Beşgen           ║")
    print("║  4-Altıgen          ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1" : kare()
    if secim == "2" : ucgen()
    if secim == "3" : ucgen()
    if secim == "4" :
        rrr = input("Renk nedir(İngilizcesini gir):")
        altigen(rrr)
    # 201 ╔
    # 205 ═
    # 187 ╗
    # 186 ║
    # 200 ╚
    # 188 ╝
