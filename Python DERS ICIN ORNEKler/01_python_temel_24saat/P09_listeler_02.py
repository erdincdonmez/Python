# listeler 2

YemekListesi=[
  "Klasik makarna",
  "Patates kızartması",
  "Elmalı turta",
  "Kirazlı dondurma"  
  "İtalyan makarnası"
]

print ("\nYemeklerimiz: ",YemekListesi)

YemekListesi.append("Biber kızartması")

print ("\nYemeklerimiz: ",YemekListesi," (ekleme yapılmış)\n")

print("\nKızartma içeren yemekler:")
for yemek in YemekListesi:
  if str.__contains__(yemek,'kızartma'):
    print (yemek)

print("\nKızartma içermeyen yemekler:")
for yemek in YemekListesi:
  if not str.__contains__(yemek,'kızartma'):
    print (yemek)

print("\nMakarnaları listeden çıkardık:")
for yemek in YemekListesi:
  if str.__contains__(yemek,'makarna'):
    YemekListesi.pop (YemekListesi.index(yemek))

print(YemekListesi)
    
"""
print("\nK ile başlayanlar:")
for yemek in YemekListesi:
  if yemek.startswith("K"):# K ile başlayan yemekler.
    print(yemek) 

print("\na ile bitenler:")
for yemek in YemekListesi:
  if yemek.endswith("a"):# a ile biten yemekler.
    print(yemek) 

for yemek in YemekListesi:
  yemek=yemek.replace("a","x") # ifadeleri değiştirme.

print("xxx",YemekListesi)


dir(list) 
 
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__',
 '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
 '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
