a = 5
b = 2
c = a/b
print (c)

print(type(a))
print(type(b))
print(type(c))

sayi_listesi = [a,b,c]
print(sayi_listesi)

# ogrenci1 = 5
# ogrenci_listesi[ogrenci1,ogrenci2]

class Ogrenci:
    TC = "78546954125"
    ad = "Onat"
    no = 456

ogrenci1 = Ogrenci
ogrenci2 = Ogrenci

print(ogrenci1)
print(ogrenci1.ad)
print(ogrenci1.no)

ogrenci1.ad = "Elif"
print(ogrenci1.ad)

print(ogrenci2.ad)
ogrenci2.ad = "Murat"
print("ogrenci2.ad:",ogrenci2.ad)
print("ogrenci1.ad:",ogrenci1.ad)
print("Ogrenci:",Ogrenci.ad)

