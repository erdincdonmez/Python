#değer alan fonksiyonlar

def selamla(xxx):
  print("Merhaba",xxx)
  print("Nasılsın\n")

def topla(abc,yyy):
  print("Toplam: ",abc+yyy)

ad = input("Adınız nedir? ")
selamla(ad)

k = int(input("Toplanacak 1. sayıyı giriniz: "))
j = int(input("Toplanacak 2. sayıyı giriniz: "))
topla(k,j)
