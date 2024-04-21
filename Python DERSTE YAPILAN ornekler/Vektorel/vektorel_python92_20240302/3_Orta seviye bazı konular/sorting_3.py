
import random
dizi = []
kullanilanlar=[]
max = 10000
for a in range(max): # 10 bin kez buna yap.
    deger = random.randint(1,max*10) # 1-100 000 arası bir sayı seç
    
    if not deger in kullanilanlar : 
        kullanilanlar.append(deger)
        dizi.append(deger)
    else :
        print("Var")

for a in range(max):
    print(a,".eleman:",dizi[a])

# print(dizi)

dizi.sort()
print(dizi)







