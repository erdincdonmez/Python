def kare():
    import turtle
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
    print("║  3-                 ║")
    print("║  4-                 ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1" : kare()
    # 201 ╔
    # 205 ═
    # 187 ╗
    # 186 ║
    # 200 ╚
    # 188 ╝
