import hesapmakinesi.hesaplamalar
import oyunlar.oyun

def anamenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═══════════════════════╗")
    print("║\033[1;31;40m    VEKTOREL APP   \033[1;32;40m    ║")
    print("║                       ║")
    print("║  1-Hesap makinesi     ║")
    print("║  2-Oyunlar            ║")
    print("║  3-Çizimler           ║")
    print("║  4-                   ║")
    print("║                       ║")
    print("║    Seçimiz nedir?     ║")
    print("╚═══════════════════════╝")
    secim = input()
    if secim == "1" :
        hesapmakinesi.hesaplamalar.hmmenu()
        anamenu()
    if secim == "2" :
        oyunlar.oyun.oyunmenu()
        anamenu()
    else:
        anamenu()
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚
    # 188 ╝


anamenu()
##hesapmakinesi()
