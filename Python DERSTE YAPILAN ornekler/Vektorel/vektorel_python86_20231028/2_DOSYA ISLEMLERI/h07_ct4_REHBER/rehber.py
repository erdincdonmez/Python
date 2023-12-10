class Kayit:
    def __init__(self,gad,gsoyad,gtelefon="---"):
        self.ad = gad
        self.soyad = gsoyad
        self.telefon = gtelefon
    def __str__(self):
        return f"Kaydedilen: {self.ad} {self.soyad} {self.telefon}"
    
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
        
    if secim == "4": 
        sil()
        menu()
        
def rehbereEkle():
    dosya = open("rehber.txt","a")
    
    # kayit1 = Kayit
    # veriyi dictionary kullarak kaydetme
    ad =    input("Ad    : ")
    soyad = input("Soyad : ")
    telefon= input("Numara: ")
    yazilacak = {"ad":ad,"soyad":soyad,"numara":telefon}
    dosya.write(str(yazilacak)+"\n")
    
    # nesne kullanarak kaydetme
    # ad =    input("Ad    : ")
    # soyad = input("Soyad : ")
    # telefon= input("Numara: ")
    # kayit1 = Kayit(ad,soyad,telefon)
    # print("Kaydedilecek bilgi: ")
    # print(kayit1)
    # dosya.write(str(kayit1)+"\n")

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
            print(k)
            # for a in kayit:
            #     print(a)
            # print(a, kayit)
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter'a basın.")
        input()

def sil():
    pass

menu()
