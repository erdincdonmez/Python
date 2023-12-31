class Ogrenci:
    TC = "000"
    adi ="adı tanımlanmamış"
    soyadi = "soyad tanımlanmamış"
    disiplinPuan = 100
    notOrtalamasi = 0
    def kisiBilgisi(self):
        print("Adı: ",self.adi,"\nSoyadı: ",self.soyadi,"\nNot Ortalaması :",self.notOrtalamasi)

class Ogretmen:
    TC = "0000"
    adi ="adı tanımlanmamış"
    soyadi = "Öğretmenin soyadı tanımlanmamış"
    brans = "Türkçe"
    def kisiBilgisi(self):
        print("Adı: ",self.adi,"\nSoyadı: ",self.soyadi,"\nBranşı :",self.brans)


kisi1 = Ogrenci()
kisi2 = Ogrenci()

kisi1.adi = "Halil Cem"

# print(Ogrenci)
print(kisi1)
# print("Adı    : ", kisi1.adi)
# print("Soyadı : ", kisi1.soyadi)
kisi1.kisiBilgisi()

