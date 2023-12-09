# ad = "Doruk"
# soyad = "AKOĞLU"
# print (ad,soyad)

class Ogrenci:
    ad = "boş"
    soyad = "boş"
    def __init__(self,x,y):
        self.ad = x
        self.soyad = y

ogrenci1 = Ogrenci
ogrenci2 = Ogrenci
# ogrenci2 = Ogrenci("Helin","AK")
# ogrenci2.ad = "Helin" # init yoksa tüm sınıf
ogrenci2.ad = "Ahmet"

print ("Öğrenci1 Adı: ",ogrenci1.ad)
print ("Öğrenci2 Adı: ",ogrenci2.ad)