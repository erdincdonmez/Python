import hesaplamalar.hesapmakinesi as hm
# from hesaplamalar.hesapmakinesi import hmmenu 
# 1.fonksiyonu direk kullanmayı sağlar
# Hafızayı etkin kullanmayı sağlar
import oyunlar.oyun as oyn

def anamenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   VEKTOR APP  \033[1;32;40m      ║")
    print("║                     ║")
    print("║  1-Hesaplamalar     ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Çizimler         ║")
    print("║  4-                 ║")
    print("║  ...                ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input()
    if secim =="1": hm.hmmenu()
    # if secim =="1": hmmenu()
    # print("seçim 1 satırı geçti.")
    if secim =="2": oyn.xxx()
    if secim =="3": pass
    if secim =="9": pass
    else: anamenu()

anamenu()
# print(dir(hm))
# help(hm.topla)
