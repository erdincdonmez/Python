# read(5) ile 5 karakter okunur
okunan = open("deneme1.txt","r")
a = okunan.read(5)
b = okunan.read(6)
print(b,a)
okunan.close()

