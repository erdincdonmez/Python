# ogrenci_listesi[ogrenci1,ogrenci2]
class Ogrenci:
    print("Ogrenci sınıfı çalıştı")
    TC = "00000000000"
    ad = "Tanımsız"
    no = 000
    def __init__(self,xx,yy): # sınıftan nesne üretme fonksiyonu
        print("Ogrenci sınıfının init fonksiyonu çalıştı.")
        self.ad = xx
        self.no = yy

ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741)

# print(ogrenci1)
print(ogrenci1.ad)
print(ogrenci1.no)

# print(ogrenci2)
print(ogrenci2.ad)
print(ogrenci2.no)

print(Ogrenci.ad)
print(Ogrenci.no)

ogrenci2.ad = "Lukas"
print(ogrenci1.ad)
print(ogrenci2.ad)
print(Ogrenci.ad)



