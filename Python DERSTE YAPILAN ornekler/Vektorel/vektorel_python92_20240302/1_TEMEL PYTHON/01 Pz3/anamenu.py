##print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
import hesaplamalar.hesapmakinesi
import oyunlar.oyun
print("MErhaba")

def anamenu():
    print("╔═════════════════════╗")
    print("║  VEKTOREL DERS      ║")
    print("║                     ║")
    print("║  1-Hesap makinesi   ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Çizimler         ║")
    print("║  4-Sağlık           ║")
    print("║  5-..               ║")
    print("║  6-..               ║")
    print("║  9-exit             ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1" :
     hesaplamalar.hesapmakinesi.hmmenu()
     anamenu()
    if secim == "2" :
        oyunlar.oyun.oyunmenu()
        anamenu()
    if secim == "9" : exit()
       
anamenu()    
    
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
