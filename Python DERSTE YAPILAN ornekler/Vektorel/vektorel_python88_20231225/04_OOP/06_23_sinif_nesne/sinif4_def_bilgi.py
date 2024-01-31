class Ogrenci:
    adsoyad = ""
    numara = ""
    notOrtalamasi = ""
    disiplinCezasi = 0

    def __init__(self,xx="ad yok",yy=0):
        self.adSoyad = xx
        self.numara = yy

    def bilgi(self):
        print ("Metod ile: Adı:",self.adSoyad,"Soyadı:",self.numara)

ogrenci1 = Ogrenci("Ali",55)
ogrenci2 = Ogrenci("Veli",66)

# print(Ogrenci)
# print(Ogrenci.adsoyad)

ogrenci1.adSoyad="Ahmet"
ogrenci2.adSoyad="Mehmet"
# print(ogrenci1.ad)
# print(ogrenci2.ad)

print(ogrenci1.bilgi())
print(ogrenci2.bilgi())

# Ogrenci.bilgi()

