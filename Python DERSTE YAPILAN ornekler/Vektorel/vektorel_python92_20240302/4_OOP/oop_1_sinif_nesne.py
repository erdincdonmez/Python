class Ogrenci ():
    ad = "aslı"
    no = 523

# print(Ogrenci)
print(Ogrenci.ad)

ogrenci1 = Ogrenci
print(ogrenci1)
print(ogrenci1.ad)
ogrenci1.ad = "Mahir"
print(ogrenci1.ad)
print(Ogrenci.ad)

ogrenci2 = Ogrenci
print(ogrenci2.ad)

ogrenci2.ad="Barış"
print("ogrenci1.ad:",ogrenci1.ad)




