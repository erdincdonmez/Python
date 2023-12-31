class Arac():
    tip = "arac"
    uretici = "tanımsız"

print("Arac sınıfı orellikleri")
print("Arac tipi     :",Arac.tip)
print("Arac ureticisi:",Arac.uretici)

arac1=Arac() # Sınıftan Ornekleme

print("\narac1 Nesne örneği için")
print("Arac tipi     :",arac1.tip) # değer atamadığım için default olanlar gelecek.
print("Arac ureticisi:",arac1.uretici)

arac2=Arac() # Sınıftan Ornekleme
arac2.tip="Araba"
arac2.uretici="volvo"
print("\narac2 Nesne örneği için")
print("Arac tipi     :",arac2.tip)
print("Arac ureticisi:",arac2.uretici)
arac2.kapiSayisi=4 # nesneye sonradan özellik atayabiliriz.
print("Arac kapi sayisi:",arac2.kapiSayisi)


