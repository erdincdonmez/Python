class Ogrenci:
    AdSoyad = "Boş"
    NotOrtalamasi = ""
    DisiplinPuanı = 100

    def __init__(self,ad,no):
        self.AdSoyad = ad
        self.Numara = no 
        
    def bilgi(self):
        print ("Metod ile: Adı Soyadı:",self.AdSoyad,", Numarası:",self.Numara)

print("Sınıftaki adSoyad değeri:", Ogrenci.AdSoyad)
ogrenci1 = Ogrenci()
ogrenci1.bilgi() 
ogrenci2 = Ogrenci()
ogrenci2.bilgi() 
