class araclar():
    tip = "arac"
    uretici = "mercedes"
    def listele(self):
        print("Araç tipi     :", self.tip)
        print("Araç ureticisi:", self.uretici)

print("araclar sınıfı için")
#araclar.listele() # hata

arac1=araclar() # Sınıftan Ornekleme

print("\narac1 Nesne örneği için")
arac1.listele()

arac2=araclar() # Sınıftan Ornekleme
arac2.tip="Araba"
arac2.uretici="volvo"
print("\narac2 Nesne örneği için")
arac2.listele()
arac2.kapiSayisi=4 # nesneye sonradan özellik atayabiliriz.
print("Arac kapi sayisi:",arac2.kapiSayisi)
arac2.listele() # kapi sayısını göstermez



