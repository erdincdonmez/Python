corbalar = [
    ["Mercimek",40],
    ["Ezogelin",50],
    ["Tarhana",45]
]
anaYemekler = [
    ["Tavuk sote",100],
    ["İskender",120],
    ["Orman kebabı",110]
]
icecekler = ["Ayran","Kola","Şalgam"]
meyveler = ["Elma","Armut","Kiraz"]
ogrenciler = ["Eren","İbrahim","Kıvanç"]

import random
tutar = 0
print("  MENÜ TAVSİYESİ ")

x = random.randint(0,len(corbalar)-1)
print(corbalar[x][0], "(fiyatı:",corbalar[x][1],")")
tutar += corbalar[x][1]

xx = random.randint(0,len(anaYemekler)-1)
print(anaYemekler[xx][0],"(fiyatı:",anaYemekler[xx][1],")")
tutar += anaYemekler[xx][1]

print(random.choice(icecekler))
print("Tutar",tutar)