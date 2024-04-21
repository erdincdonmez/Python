class Ogrenci:
    AdSoyad = "Tanımsız"
    NotOrtalamasi = ""
    DisiplinCezasi = 10

    def __init__(self,ad,no,dc=30):
        self.AdSoyad = ad
        self.Numara = no 
        self.DisiplinCezasi = dc
        print(f"Nesne {ad}, {no} değerleriyle başarıyla oluşturuldu.")
        
    def Bilgi(self):
        print ("Bilgi : Metod ile Adı Soyadı:",self.AdSoyad,", Numarası:",self.Numara)

print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)
ogrenci1 = Ogrenci("Ahmet BAL",10)
ogrenci2 = Ogrenci("Erhan SARI",15,40)


ogrenci1.Bilgi()

print(Ogrenci.AdSoyad)
print(Ogrenci.DisiplinCezasi)
print(ogrenci1.DisiplinCezasi)
print(ogrenci2.DisiplinCezasi)
