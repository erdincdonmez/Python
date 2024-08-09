class Ogrenci:
    AdSoyad = "Tanımsız"
    NotOrtalamasi = ""
    DisiplinCezasi = 0
    # aldigiDersler=["Ders listesi boş"]

    def __init__(ddd,ad,no=""):
        ddd.AdSoyad = ad
        ddd.Numara = no 
        # ddd.aldigiDersler.append(ad)
        ddd.aldigiDersler=[]

    def bilgi(yyy):
        print ("\n\nMetod ile: Adı Soyadı:",yyy.AdSoyad,", Numarası:",yyy.Numara)
        print ("Dersler:",*yyy.aldigiDersler,sep=", ")

    def ders_ekle(self,ww):
        self.aldigiDersler.append(ww)

    def ders_listesi(self):
        print("\n\nDersler listeleniyor")
        print (*self.aldigiDersler,sep="\n")

print("Sınıftaki adSoyad değeri:", Ogrenci.AdSoyad)
ogrenci1 = Ogrenci("Ahmet BAL")
ogrenci2 = Ogrenci("Veli GÜL",15)
ogrenci1.bilgi() 
ogrenci2.bilgi()
ogrenci1.ders_listesi()
ogrenci1.ders_ekle("Matematik")
ogrenci1.ders_ekle("Türkçe")
ogrenci2.ders_ekle("Fizik")
ogrenci1.ders_listesi()

ogrenci1.bilgi()
ogrenci2.bilgi()



