def topla(aa,bb):
    print(f"Toplam:{aa+bb}")

def carp(x,yy):
    print(f"Çarpım:{x*yy}")

# sayi1 = 3
# sayi2 = 7
sayi1 = int(input("Birinci sayı nedir?"))
sayi2 = int(input("İkinci sayı nedir? "))
# topla(4,6)
topla(sayi1,sayi2)
# topla(sayi1,topla(sayi2,sayi2)) # fonksiyonlarda geri dönüş olmadan bu şekilde kullanılmaz.

# topla()
carp(sayi1,sayi2)
