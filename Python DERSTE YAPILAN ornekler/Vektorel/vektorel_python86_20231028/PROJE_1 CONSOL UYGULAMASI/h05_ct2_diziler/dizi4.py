corbalar = ["Mercimek","Ezogelin","Tarhana"]
anaYemekler = ["Tavuk sote","İskender","Orman kebabı"]
icecekler = ["Ayran","Kola","Şalgam"]
meyveler = ["Elma","Armut","Kiraz"]
ogrenciler = ["Eren","İbrahim","Kıvanç"]

import random
print("  MENÜ TAVSİYESİ ")
print(corbalar[random.randint(0,len(corbalar)-1)])
print(anaYemekler[random.randint(0,len(anaYemekler)-1)])
print(random.choice(icecekler))

