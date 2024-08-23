# sınıftan nesne üretme
class Ogrenci:
    ad = "---"
    soyad = ""
    numara = ""
    notOrtalamasi = ""
    disiplinCezasi = 0
    # def __init__():


print("Sınıftaki ad değeri:",Ogrenci.ad)
ogrenci1 = Ogrenci() # parantezli olunca init çalışır
ogrenci2 = Ogrenci()

ogrenci1.ad = "Ali"
ogrenci2.ad = "Veli"

print("ogrenci1 nesnesinin ad değeri:",ogrenci1.ad)
print("ogrenci2 nesnesinin ad değeri:",ogrenci2.ad)
ogrenci1.ad="Cem"
print("ogrenci1 nesnesinin ad değeri:",ogrenci1.ad)
print("ogrenci2 nesnesinin ad değeri:",ogrenci2.ad)

print("Sınıftaki ad değeri:",Ogrenci.ad)


