class Ogrenci:
    TC = "78546954125"
    adi = "Onat"
    numarasi = 456


print(Ogrenci.adi)
print(Ogrenci.TC)

ogrenci1 = Ogrenci
ogrenci2 = Ogrenci

print(ogrenci1.adi)
print(ogrenci1.TC)

ogrenci1.adi = "Gökhan DEMİR"
print(ogrenci1.adi)
print(Ogrenci.adi)
ogrenci2.adi = "Melisa VARDAR"
print(ogrenci1.adi)
print(ogrenci2.adi)

