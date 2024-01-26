def topla (a,b):
    return a+b

def kdvHesapla(miktar,vergiOrani=20):
    return (miktar * vergiOrani) /100

def vergiHesapla(miktar=int(input("Miktar nedir?")),oran=int(input("Oran nedir?"))):
    pass

c = topla(45,2)

print(c)
print("Kdv tutarı: ", kdvHesapla(50))