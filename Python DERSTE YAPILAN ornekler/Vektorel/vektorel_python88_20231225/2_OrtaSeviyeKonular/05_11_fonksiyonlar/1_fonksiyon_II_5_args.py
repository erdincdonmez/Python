# klavyeden boş geçilene kadar girilen sayıların ortalamasını alan program.
# def ortalamasiniAl(*sayi):
#     print("Gönderilen veri/dizi:",sayi)
#     print("Gönderilen parametre sayısı:",len(sayi))
#     toplam = 0
#     for x in sayi:
#         toplam += x
#     return toplam / len(sayi)

deger=" "
deger1=0
toplam = 0
girilenMiktar = 0
while deger!="":
    deger = input ("Ortalama için sayı girin(Bitirmek içni boş geçin):")
    if deger !="" : 
        deger1 = int(deger)
        girilenMiktar +=1
        toplam += deger1
    


print("Ortalama:",toplam/girilenMiktar)
