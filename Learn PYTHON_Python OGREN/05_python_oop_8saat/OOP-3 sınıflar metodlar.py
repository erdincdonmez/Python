class Arac():
    tip = "arac"
    uretici = "mercedes"
    def bilgi(self):
        print("Araç tipi     :", self.tip)
        print("Araç ureticisi:", self.uretici)

print("Arac sınıfı için")
#Arac.bilgi() # hata

arac1=Arac() # Sınıftan Ornekleme

print("\narac1 Nesne örneği için")
arac1.bilgi()

arac2=Arac() # Sınıftan Ornekleme
arac2.tip="Araba"
arac2.uretici="volvo"
print("\narac2 Nesne örneği için")
arac2.bilgi()
arac2.kapiSayisi=4 # nesneye sonradan özellik atayabiliriz.
print("Arac kapi sayisi:",arac2.kapiSayisi)
arac2.bilgi() # kapi sayısını göstermez



