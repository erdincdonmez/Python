
def menu():
    print ("╔════════════════════════╗")
    print ("║  REHBER PROGRAMI       ║")
    print ("╠════════════════════════╣")
    print ("║  1-Rehbere ekle        ║")
    print ("║  2-Kayıtları listele   ║")
    print ("║  3-Kayıt düzelt        ║")
    print ("║  4-Kayıt sil           ║")
    print ("║  5-Çıkış               ║")
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
        
def rehbereEkle():
    dosya = open("rehber.txt","a")
    ad =    input("Ad    : ")
    soyad = input("Soyad : ")
    numara= input("Numara: ")
    yazilacak = ad +"|"+ soyad +"|"+ numara +"\n"
    dosya.write(yazilacak)
    dosya.close()

def listele():
    try:
        dosya = open("rehber.txt","r")
        print("   Rehber Kayıt Listesi ")        
        print("═════════════════════════════")
        a = 1        
        for kayit in dosya.readlines():
            print(a, kayit)
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter'a basın.")
        input()


menu()
