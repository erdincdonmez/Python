class Ogrenci:
    ad = "---"
    soyad = ""
    numara = ""
    notOrtalamasi = ""
    disiplinCezasi = 0

    def Bilgi(self):
        print ("Metod ile: Adı:",self.ad,"Soyadı:",self.soyad)

print("Sınıftaki ad değeri:",Ogrenci.ad)
ogrenci1 = Ogrenci()

ogrenci1.Bilgi()
print(ogrenci1.__dict__) # nesne içeriğini görüntüler.
print(Ogrenci.__dict__) # sınıf içeriğini görüntüler.




