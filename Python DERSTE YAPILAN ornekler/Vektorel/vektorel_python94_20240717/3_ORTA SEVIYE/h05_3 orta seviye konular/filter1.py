# sayilar = [11,22,3,6,7,5,8]

# # yeniDizi = list(filter(lambda x:True,sayilar))
# yeniDizi = list(filter(lambda x: x%2==0,sayilar))
   
# print(yeniDizi)


# sayilar = [11,22,3,6,7,5,8]
# def ciftmi(x): 
#     return x%2==0
# # yeniDizi = list(filter(lambda x:True,sayilar))
# yeniDizi = list(filter(ciftmi,sayilar))
   
# print(yeniDizi)


ogrenciNotlari = [[60,90,80],[20,60],[90,90,80]]
def gectimi(x): 
    # toplam = 0
    # for a in x: toplam+=a
    # return toplam
    if len(x)>2 : durum = True
    else: durum =False
    return durum
# yeniDizi = list(filter(lambda x:True,sayilar))
yeniDizi = list(filter(gectimi,ogrenciNotlari))
   
print(yeniDizi)

# # map her bir eleman için fonksiyon çalıştırma
# def kareAl(nn): return nn**2

# sayilar = [1,3,4,5,7,9]
# sonuc = list(map(kareAl,sayilar))
# print (sonuc)
# # veya aşağıdaki forlar ile de yazdırılabilir.
# for x in sonuc: print(x)
# for xx in map(kareAl,sayilar): print(xx)


