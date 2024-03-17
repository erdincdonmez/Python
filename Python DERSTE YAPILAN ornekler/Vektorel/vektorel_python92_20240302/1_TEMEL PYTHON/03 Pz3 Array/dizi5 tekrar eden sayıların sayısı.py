# dizideki tekrar eden elemanların sayısı
sayilar = [2,6,5,8,7,7,1,5]
for a in sayilar:
    print (a)

adet = []

print("tekrar edenler")
for a in range(len(sayilar)):
    for b in range(a,len(sayilar)):
        # print (sayilar[a], sayilar[b])
        if sayilar[a] == sayilar[b] : print (sayilar[a])

