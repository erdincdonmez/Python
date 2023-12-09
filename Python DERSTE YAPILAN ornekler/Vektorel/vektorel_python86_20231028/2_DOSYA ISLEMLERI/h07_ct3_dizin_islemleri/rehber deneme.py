
def menu():
    print ("╔════════════════════════╗")
    print ("║  REHBER PROGRAMI       ║")
    print ("╠════════════════════════╣")
    print ("║  1-Rehbere ekle        ║")
    print ("║  2-Kayıtları listele   ║")
    print ("║  3-Kayıt düzelt        ║")
    print ("║  4-Kayıt sil           ║")
    print ("║  5-Çıkış               ║")
    print ("║  6-Okuma               ║")
    print ("║  Seçimizini giriniz    ║")
    print ("╚════════════════════════╝")
    secim = input ()
    if secim == "1": 
        rehbereEkle()
        listele()
        menu()
    if secim == "2": 
        listele()
        menu()
    if secim == "6": 
        oku()
        menu()

def oku():
    print("\n\npozisyon bilgisi")
    abc = open("rehber.txt", "r+")
    position = abc.seek(3, 0);
    str = abc.read(5);
    print("1. okunan : ", str)
    position = abc.tell(); #pozisyon bilgisi

    print("Şu anki pozisyon : ", position)
    str = abc.read(5);
    print("2. okunan : ", str)
    #tekrar başa konumlan
    # position = abc.seek(0, 0);
    # str = abc.read(10);
    # print("2. okunan : ", str)
    abc.close()


def rehbereEkle():
    dosya = open("rehber.txt","a")
    ad =    input("Ad    : ")
    soyad = input("Soyad : ")
    numara= input("Numara: ")
    yazilacak = {"ad":ad,"soyad":soyad,"numara":numara}
    dosya.write(str(yazilacak)+"\n")
    dosya.close()

def listele():
    try:
        dosya = open("rehber.txt","r")
        print("   Rehber Kayıt Listesi ")        
        print("═════════════════════════════")
        a = 1        
        kayit = {}
        for k in dosya.readlines():
            kayit = k
            for a in kayit:
                print(a)
            # print(a, kayit)
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter'a basın.")
        input()


menu()
