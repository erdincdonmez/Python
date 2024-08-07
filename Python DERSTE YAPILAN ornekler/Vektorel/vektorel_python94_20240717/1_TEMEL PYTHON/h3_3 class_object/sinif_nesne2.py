class Ogrenci: # referans, model
    adi = "Mustafa"
    soyadi = "ALP"
    no = "547"
    def __init__(self,xx="--",yy="//"):
        self.adi = xx
        self.no = yy 

print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi)

ogrenci1 = Ogrenci()
print("o1: ",ogrenci1.adi)
ogrenci2 = Ogrenci()
print("o2: ",ogrenci2.no)

ogrenci1.adi = "Ali"
print(ogrenci1.adi)
ogrenci2.adi = "Yasin"
print("ogrenci2.adi",ogrenci2.adi)
print("ogrenci1.adi",ogrenci1.adi)

ogrenci3 = Ogrenci("Ozancan",65)
ogrenci4 = Ogrenci
print("o1: ",ogrenci1.no)
print("o2: ",ogrenci2.no)
print("o3: ",ogrenci3.no)
print("o4: ",ogrenci4.no)
