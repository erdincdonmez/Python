# a = 5
# b = "5"
# print(a*2)
# print(type(a))
# print(b*2)
# print(type(b))

class Ogrenci: # referans, model
    adi = "Mustafa"
    soyadi = "ALP"
    numarasi = "547"

print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi)

ogrenci1 = Ogrenci
print(ogrenci1.adi)
ogrenci2 = Ogrenci
print(ogrenci2.adi)

ogrenci1.adi = "Ali"
print(ogrenci1.adi)
ogrenci2.adi = "Yasin"
print("ogrenci2.adi",ogrenci2.adi)
print("ogrenci1.adi",ogrenci1.adi)
