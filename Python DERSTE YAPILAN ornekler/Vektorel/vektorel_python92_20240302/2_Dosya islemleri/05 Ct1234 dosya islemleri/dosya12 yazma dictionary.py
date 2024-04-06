# yazarken stringe çevirmek lazım
ogrenci={
    "Adi" : "Gökhan" ,
    "Numarasi" : "5236589547"
}
dosya = open("deneme2.txt","w")
dosya.write(str(ogrenci))
dosya.close()

okunan = open("deneme2.txt")
aa = okunan.read()
print(aa)

okunan.close()

