meyveler = ["Elma","Armut","Kiraz"]
ogrenciler = ["Eren","İbrahim","Kıvanç"]

print(meyveler)

# eleman = input("Meyve giriniz:")
eleman = "Muz"
meyveler.insert(2,eleman)
print("insert ile eklenmiş: ",meyveler)
meyveler.insert(2,eleman)
meyveler.pop()
print("pop ile Silinmiş: ",meyveler)
meyveler.sort()
print("Sort ile sıralanmış: ",meyveler)
meyveler.reverse()
print("reverse ile ters çevirme: ",meyveler)


