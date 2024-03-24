def eaPuani(sayi1,sayi2):
    puan1 = sayi1+sayi2
    puan2 = sayi1*sayi2
    puanlar = [puan1,puan2]
    return puanlar, puan1

def sayPuani(sayi1,sayi2):
    puan = sayi1*sayi2
    return puan

p1 = eaPuani(3,4)
p2 = eaPuani(3,4)
print("Sonuç :", p1) 
