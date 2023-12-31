class Arac():
    tip = "arac"
    uretici = "mercedes"
    def __init__(self, gelenTip="tip tanımsız",gelenUretici="bilinmiyor"):# fonksiyon çağırılınca çalışacak fonksiyon
        self.tip=gelenTip
        self.uretici=gelenUretici
    def bilgi(self): 
        print("Araç tipi     :", self.tip)
        print("Araç ureticisi:", self.uretici,"\n")

print("Arac sınıfı için")
#Arac.bilgi() # hata
print("Araç tipi     :", Arac.tip)
print("Araç ureticisi:", Arac.uretici)

arac1=Arac() # Sınıftan Ornekleme

print("\narac1 Nesne örneği için")
arac1.bilgi()

arac2=Arac() # Sınıftan Ornekleme
arac2.tip="Araba"
arac2.uretici="volvo"
print("\narac2 Nesne örneği için")
arac2.bilgi()
arac2.kapiSayisi=4 # nesneye sonradan özellik atayabiliriz.
print("Arac kapi sayisi:",arac2.kapiSayisi,"\n")
arac2.bilgi() # kapi sayısını göstermez

print("\narac3 Nesne örneği için")
arac3=Arac("Kamyon","BMW")
arac3.bilgi()

print("\narac4 Nesne örneği için")
arac4=Arac()
arac4.bilgi()



