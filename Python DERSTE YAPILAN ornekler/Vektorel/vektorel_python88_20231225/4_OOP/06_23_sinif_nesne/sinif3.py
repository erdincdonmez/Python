class Ogrenci:
    adsoyad = "Ad tanımlanmamış"
    numara = ""
    notOrtalamasi = ""
    disiplinCezasi = 0

    def __init__(self):
        self.AdSoyad = "Tanımsız"
        self.Numara = 0 


    def bilgi(self):
        print ("Metod ile: Adı:",self.ad,"Soyadı:",self.soyad)

ogrenci1 = Ogrenci
ogrenci2 = Ogrenci

print(Ogrenci)
print(Ogrenci.adsoyad)

# ogrenci1.ad="Ahmet"
# ogrenci2.ad="Mehmet"
# print(ogrenci1.ad)
# print(ogrenci2.ad)

print(ogrenci1.bilgi())

Ogrenci.bilgi()

