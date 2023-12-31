class Arac():
    tip = "arac"
    uretici = "mercedes"
    def __init__(self, gelenTip="tip tanımsız",gelenUretici="bilinmiyor"):# fonksiyon çağırılınca çalışacak fonksiyon
        self.tip=gelenTip # __init__ tanımına constructor yani yapıcı fonksiyon deniyor.
        self.uretici=gelenUretici # yapıcı fonksiyonlar fonksiyon çalışınca standar bir şey üretmek
    def bilgi(self): 
        print("Araç tipi     :", self.tip)
        print("Araç ureticisi:", self.uretici,"\n")
        
    def Ekle(self,eklemeYeri="Eklenecek yer default SQL"): 
        print("Araç Ekleme işlemi")
        print("==================")
        print("Araç tipi     :", self.tip)
        print("Araç ureticisi:", self.uretici)
        print("Ekleme yeri   :", eklemeYeri,"\n")
        print("Ekleme tamam")

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
arac3=Arac("Kamyon","BMW") # bunu init yapıcı fonksiyonu sayesinde yapabildik.
arac3.bilgi()

print("\narac4 Nesne örneği için")
arac4=Arac("Bisiklet","Carraro") 
print (arac4.Ekle())# burada Ekle metodunu kullandık
print (arac4.Ekle("access"))# burada Ekle metodunu kullandık

