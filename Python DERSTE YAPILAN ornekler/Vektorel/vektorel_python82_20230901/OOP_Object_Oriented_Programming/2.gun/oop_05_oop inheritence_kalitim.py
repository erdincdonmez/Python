class Kisi():
    TC = "000"
    adi ="adı tanımlanmamış"
    soyadi = "soyad tanımlanmamış"

class Ogrenci(Kisi): # Kisi sınıfından kalıtım alındı
    ##    TC = "000"
    ##    adi ="adı tanımlanmamış"
    ##    soyadi = "soyad tanımlanmamış"
    disiplinPuan = 100
    notOrtalamasi = 0
    def __init__(self,x="öğrenci adı boş",y="boş bırakıldı"):
        self.adi= x
        self.soyadi = y
        print(self.adi,"adında bir öğrenci oluşturuldu.")

    def kisiBilgisi(self):
        print("=== ÖĞRENCİ ===")
        print("Adı: ",self.adi,"\nSoyadı: ",self.soyadi,"\nNot Ortalaması :",self.notOrtalamasi)
        print("===============")

class Ogretmen(Kisi):
    ##    TC = "0000"
    ##    adi ="adı yok"
    ##    soyadi = "Öğretmenin soyadı tanımlanmamış"
    brans = "Türkçe"

    def __init__(self,x="Öğretmen adı boş",y="boş bırakıldı"):
        self.adi= x
        self.soyadi = y
        print(self.adi,"adında bir öğretmen oluşturuldu.")

    def kisiBilgisi(self):
        print("==  ÖĞRETMEN ==")
        print("Adı: ",self.adi,"\nSoyadı: ",self.soyadi,"\nBranşı :",self.brans)
        print("===============")


kisi3=Ogrenci("Alper","TAŞ")
kisi4=Ogrenci("Aydın","TAŞ")
kisi5=Ogretmen("Arda","TAŞ")


kisi5.kisiBilgisi()
kisi3.kisiBilgisi()

