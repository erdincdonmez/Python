# yazarken stringe çevirmek lazım
a = 5
b = 4
c = a+b
dosya = open("deneme2.txt","w")
dosya.write(str(c))
dosya.close()

okunan = open("deneme2.txt")
aa = okunan.read()
print(aa)
print(aa*2)
print(int(aa)*2)
okunan.close()

