class Ogrenci:
    AdSoyad = "---"
    NotOrtalamasi = ""
    DisiplinCezasi = 0

    def __init__(self):
        self.AdSoyad = "Tanımsız"
        self.Numara = 0 
        
    def Bilgi(self):
        print ("Metod ile: Adı Soyadı:",self.AdSoyad,", Numarası:",self.Numara)

print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)
ogrenci1 = Ogrenci()

ogrenci1.Bilgi()
