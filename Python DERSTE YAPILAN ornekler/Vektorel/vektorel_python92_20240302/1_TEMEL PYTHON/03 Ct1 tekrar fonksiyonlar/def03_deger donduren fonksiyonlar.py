def topla(aa,bb):
    return f"Toplam:{aa+bb}"

def carp(x,yy):
    return f"Çarpım:{x*yy}"

sayi1 = int(input("Birinci sayı nedir?"))
sayi2 = int(input("İkinci sayı nedir? "))

# topla(sayi1,sayi2) # tek başına işlemi yapar ama bir yerde görünmez.
print (topla(sayi1,sayi2))
print (carp(sayi1,sayi2))

