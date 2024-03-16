def topla(*sayi):
    toplam = 0
    for a in sayi:
        toplam += a
    return toplam

def carp(x=1,yy=1):
    return x*yy

# sayi1 = int(input("Birinci sayı nedir?"))
# sayi2 = int(input("İkinci sayı nedir? "))
sayi1 = 5
sayi2 = 7

# tek başına işlemi yapar ama bir yerde görünmez.
# # topla(sayi1,sayi2) 

print (topla(sayi1,8,sayi2,6,10,5))
print (topla(sayi1,sayi2))
print (f"Toplam:{topla(sayi1,sayi2)}")
print (topla(sayi1,topla(8,sayi1)))
print (carp(sayi1))

