def ortalamasiniAl(*sayi):
    print("Gönderilen veri/dizi:",sayi)
    print("Gönderilen parametre sayısı:",len(sayi))
    toplam = 0
    for x in sayi:
        toplam += x
        # print(x)
    return toplam / len(sayi)
    # print(sayi[0])
    # print(sayi[1])

print("Ortalama:",ortalamasiniAl(10,20,30,"40"))
