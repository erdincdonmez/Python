import random
vMaaslari = []
# print(sayilar)
for a in range(1000):
    vMaaslari.append(random.randint(10,99))

# x=1
# print(x,".sayı: ",vMaaslari[x])

# x=8985632
# print(x,".sayı: ",vMaaslari[x])

maasAlanlar20 = 0
sonuc ="yok"
for xx in range(len(vMaaslari)//2):
    # if xx < 20: maasAlanlar20 += 1
    if vMaaslari[xx] == 99 : sonuc = "var"
    print(vMaaslari[xx])

if sonuc =="yok":
    for xx in range(len(vMaaslari)//2,len(vMaaslari)):
        # if xx < 20: maasAlanlar20 += 1
        if vMaaslari[xx] == 99 : sonuc = "var"
        print(vMaaslari[xx])


print("20 maaş alan sayısı: ", maasAlanlar20)
print("99 binlira maaş alan:", sonuc)
