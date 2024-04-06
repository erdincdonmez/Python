# yazarken stringe çevirmek lazım
ogrenciler=["Mahir","Şeyma", "Metin","Barış","Ertan"]
dosya = open("deneme2.txt","w")
dosya.write(str(ogrenciler))
dosya.close()

okunan = open("deneme2.txt")
aa = okunan.read()
print(aa)

okunan.close()

