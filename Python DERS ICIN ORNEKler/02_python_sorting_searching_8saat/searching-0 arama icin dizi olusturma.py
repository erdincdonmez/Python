import random
dizi = []
sayi = 0
elemanSayisi = 1000
for a in range(elemanSayisi):
    sayi += random.randint(1,elemanSayisi)
    dizi.append(sayi)

print(dizi)
