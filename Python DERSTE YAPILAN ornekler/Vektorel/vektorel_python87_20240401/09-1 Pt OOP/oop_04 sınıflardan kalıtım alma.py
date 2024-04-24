class Ogrenci:
    TC = "00000000000" 
    ad = "Tanımsız"
    no = 000
    puan = 10
    def __init__(self,xx="Ad yok",yy=111,zz=20): 
        self.ad = xx
        self.no = yy
        self.puan = zz
    def bilgiVer(self):
        print ("Metod ile bilgi veriliyor: Adı:",self.ad,", Numarası:",self.no)

    def belgeDurumu(self):
        if self.puan < 80: durum = "Teşekkür"
        else: durum = "Taktir"
        return durum

class IlkokulOgrenci(Ogrenci):
    pass

class LiseOgrenci(Ogrenci):
    lgsp = 0
    def __init__(self, xx="Ad yok", yy=111, zz=20, lgs_gelen=0):
        super().__init__(xx, yy, zz)
        self.lgsp = lgs_gelen

    def bilgiVer(self):
        print ("Metod ile bilgi veriliyor: Adı:",self.ad,", Numarası:",self.no, "LGS:",self.lgsp)

ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741,87)
ogrenci3 = IlkokulOgrenci()

ogrenci1.bilgiVer()
print("Ogrenci.puan  :",Ogrenci.puan)
print("ogrenci1.puan :",ogrenci1.puan)
print("ogrenci2.puan :",ogrenci2.puan)

print("ogrenci1.belgeDurumu :",ogrenci1.belgeDurumu())
print("ogrenci2.belgeDurumu :",ogrenci2.belgeDurumu())

print("ogrenci3.ad:",ogrenci3.ad)
print("ogrenci3.bilgiVer:",ogrenci3.bilgiVer())

ogrenci4 = IlkokulOgrenci("Mediha",458,90)

print("ogrenci4.ad:",ogrenci4.ad)
ogrenci4.bilgiVer()

ogrenci5 = LiseOgrenci("Dila",5236,90,450)
print("ogrenci5.lgsp:",ogrenci5.lgsp)
print("ogrenci5.bilgiVer:",ogrenci5.bilgiVer())



