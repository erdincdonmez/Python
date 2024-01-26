def topla(*sayi):
    print("Gönderilen veri/dizi:",sayi)
    print("Gönderilen parametre sayısı:",len(sayi))
    toplam = 0
    for x in sayi:
        toplam += x
        # print(x)
    return toplam
    # print(sayi[0])
    # print(sayi[1])

print("Toplam:",topla(10,20,14,52))
