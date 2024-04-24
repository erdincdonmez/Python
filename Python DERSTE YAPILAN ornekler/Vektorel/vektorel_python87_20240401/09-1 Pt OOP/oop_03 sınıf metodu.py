# ogrenci_listesi[ogrenci1,ogrenci2]
class Ogrenci:
    # print("Ogrenci sınıfı çalıştı")
    TC = "00000000000" 
    ad = "Tanımsız"
    no = 000
    puan = 10
    def __init__(self,xx="Ad yok",yy=111,zz=20): # sınıftan nesne üretme fonksiyonu
        # print("Ogrenci sınıfının init fonksiyonu çalıştı.")
        self.ad = xx
        self.no = yy
        self.puan = zz
    def bilgiVer(self):
        print ("Metod ile bilgi veriliyor: Adı:",self.ad,", Numarası:",self.no)

    def belgeDurumu(self):
        if self.puan < 80: durum = "Teşekkür"
        else: durum = "Taktir"
        return durum

ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741,87)

# print(ogrenci1)
# print(ogrenci1.ad)
# print(ogrenci1.no)
ogrenci1.bilgiVer()
print("Ogrenci.puan  :",Ogrenci.puan)
print("ogrenci1.puan :",ogrenci1.puan)
print("ogrenci2.puan :",ogrenci2.puan)

# print("Ogrenci.belgeDurumu  :",Ogrenci.belgeDurumu()) # olmaz, nesne değil
print("ogrenci1.belgeDurumu :",ogrenci1.belgeDurumu())
print("ogrenci2.belgeDurumu :",ogrenci2.belgeDurumu())




