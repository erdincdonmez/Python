# map her bir eleman için fonksiyon çalıştırma
def xxx(nn): 
    return nn+2

sayilar = [1,3,4,5,7,9]
sonuc = list(map(xxx,sayilar))
print (sonuc)
# veya aşağıdaki forlar ile de yazdırılabilir.
for x in sonuc: print(x)
for xx in map(xxx,sayilar): print(xx)
