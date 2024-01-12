
class Ogrenci:
    adi = "Mustafa"
    soyadi = "ALP"
    numarasi = "547"
    class AldigiDersler:
        ders1 = "matematik"
        ders2 = "fizik"
    class SaglikDurumu:
        boy = 174
        kilo = 67

ogrenci1 = Ogrenci # sınıf nesnesi
ogrenci2 = Ogrenci # sınıf nesnesi

print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi)
print("Öğrenci Bilgisi: ",ogrenci1.adi, ogrenci1.soyadi)
print("Öğrenci Bilgisi: ",ogrenci1.adi, ogrenci1.soyadi)
print("Öğrencinin aldığı dersler:", Ogrenci.AldigiDersler.ders1, Ogrenci.AldigiDersler.ders2)