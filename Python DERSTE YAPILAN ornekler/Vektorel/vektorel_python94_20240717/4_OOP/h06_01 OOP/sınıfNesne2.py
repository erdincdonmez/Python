class Ogrenci:
    AdSoyad = "Tanımsız"
    NotOrtalamasi = ""
    DisiplinCezasi = 0

    def __init__(self,ad,no):
        self.AdSoyad = ad
        self.Numara = no 
        
    def Bilgi(self):
        print ("Metod ile: Adı Soyadı:",self.AdSoyad,", DisiplinCezasi:",self.DisiplinCezasi)
        # print ("Metod ile: Adı Soyadı:",self.AdSoyad,", Dizsiplin durumu:",self.DisiplinCezasi)

print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)

ogrenci1 = Ogrenci("Ahmet BAL",10)
ogrenci2 = Ogrenci("Cem BAŞ",20)
ogrenci3 = Ogrenci("ddd",5)
# ogrenci1 = Ogrenci()
# ogrenci1.AdSoyad = "Ahmet BAL"
# ogrenci1.DisiplinCezasi = 10

ogrenci1.Bilgi()
ogrenci2.Bilgi()
ogrenci3.Bilgi()
