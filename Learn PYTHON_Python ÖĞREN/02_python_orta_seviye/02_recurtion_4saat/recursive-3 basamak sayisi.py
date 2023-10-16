def basamakSayisi(sayi):
    if sayi%10 < 1: return sayi
    else: return 1 + basamakSayisi(sayi/10)
    
s = int(input("Basamak sayısı hesaplanacak sayi gir:"))
print (basamakSayisi(s))
