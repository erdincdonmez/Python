#geriye değer döndüren fonksiyonlar

def selamla(xxx):
  return "Merhaba "+xxx+" nasılsın\n"

def topla(abc,yyy):
  return "Toplam: "+ str (abc+yyy)

ad = input("Adınız nedir? ")
print (selamla(ad))

k = int(input("Toplanacak 1. sayıyı giriniz: "))
j = int(input("Toplanacak 2. sayıyı giriniz: "))

print (topla(k,j))
