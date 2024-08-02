def hmmenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   HESAPLAMALAR  \033[1;32;40m      ║")
    print("║                     ║")
    print("║  1-TOPLA     ║")
    print("║  2-ÇIKAR          ║")
    print("║  3-ÇARP         ║")
    print("║  4-                 ║")
    print("║  ...                ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input()
    if secim =="1": topla()
    if secim =="2": cikar()
    if secim =="3": pass
    
# def topla(a,b):
def topla():
    """
    Topla fonksiyonu çalışması için iki parametre....
    bunlar....
    fonksiyon çıktısı...
    """
    aa = input("1.sayıyı gir:")
    bb = input("2.sayıyı gir:")
    print(f"{aa} ile {bb} toplamı {int(aa)+int(bb)}")
    # return a+b

def cikar():
    aa = int(input("1.sayıyı gir:"))
    bb = int(input("2.sayıyı gir:"))
    print(f"{aa} ile {bb} farkı {aa-bb}")

def carp(a,b):
    return a*b

def ikiKati(t):
    return t*2

