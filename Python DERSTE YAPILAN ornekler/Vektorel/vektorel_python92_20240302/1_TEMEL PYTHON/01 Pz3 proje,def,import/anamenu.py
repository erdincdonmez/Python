##print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
import hesaplamalar.hesapmakinesi
import oyunlar.oyun
import hesaplamalar.nothesabi
import cizimler.cizim
print("MErhaba")

def anamenu():
    print("╔═════════════════════╗")
    print("║  VEKTOREL DERS      ║")
    print("║                     ║")
    print("║  1-Hesap makinesi   ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Çizimler         ║")
    print("║  4-Sağlık           ║")
    print("║  5-Not hesabı       ║")
    print("║  6-..               ║")
    print("║  ç-çıkış            ║")
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
    if secim == "3" :
        cizimler.cizim.cizimmenu()
        anamenu()
    if secim == "5" :
        hesaplamalar.nothesabi.harfnotu()
        anamenu()
    if secim == "ç" or secim == "Ç": exit()
    else: 
       print("Seçim sadece 1,2,3,4,ç olabilir.")
       anamenu()
       
anamenu()    
    
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
