import oyunlar.yilanOyunu
def xxx():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   OYUN LİSTESİ  \033[1;32;40m    ║")
    print("║                     ║")
    print("║  1-Yılan            ║")
    print("║  2-Tetris           ║")
    print("║  3-                 ║")
    print("║  4-                 ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1": oyunlar.yilanOyunu.oyna()
    # elif secim == "2": cikar()
         
        

# def topla(a,b):
def sayiTahmin():
    x = input("1.sayıyı gir:") 
    y = input("2.sayıyı gir:")
    print(f"{x} ile {y} toplamı {x+y} dir.")
    # return a+b

def oyun2():
    x = input("1.sayıyı gir:") 
    y = input("2.sayıyı gir:")
    print(f"{x} ile {y} farkı {x-y} dir.")
    # return a+b

