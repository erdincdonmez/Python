class Ogrenci:
    TC = "000"
    adi ="adı tanımlanmamış"
    soyadi = "soyad tanımlanmamış"
    disiplinPuan = 100
    notOrtalamasi = 0
    def __init__(self):
        self.adi="öğrenci adı boş"
        self.soyadi ="boş bırakıldı"

    def kisiBilgisi(self):
        print("Adı: ",self.adi,"\nSoyadı: ",self.soyadi,"\nNot Ortalaması :",self.notOrtalamasi)

class Ogretmen:
    TC = "0000"
    adi ="adı tanımlanmamış"
    soyadi = "Öğretmenin soyadı tanımlanmamış"
    brans = "Türkçe"
    def kisiBilgisi(self):
        print("Adı: ",self.adi,"\nSoyadı: ",self.soyadi,"\nBranşı :",self.brans)


# kisi1 = Ogrenci()
# kisi2 = Ogrenci()

# kisi1.adi = "Halil Cem"
# kisi1.soyadi = "ÇALIŞIR"

# print(kisi1)
# kisi1.kisiBilgisi()

kisi3=Ogrenci("Alper","TAŞ")

print(kisi3)
##kisi3.kisiBilgisi()

