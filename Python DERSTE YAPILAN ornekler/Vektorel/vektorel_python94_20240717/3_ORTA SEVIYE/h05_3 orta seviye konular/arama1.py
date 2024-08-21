import random
dizi = []

for a in range(10000):
    dizi.append(random.randint(1,10000))

dizi.sort()
for b in range(10000):
    print(f"{b} : {dizi[b]}")