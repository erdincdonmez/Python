import random
liste1 = []
print(liste1)
sayiadedi = 1000000
for a in range(sayiadedi):
    liste1.append(random.randint(10000,99999))

# print("liste1:")
# for x in liste1:
#     print(x)

aranan = int(input("Aradığınız sayı nedir?"))
a = 0
b = 0
# for b in liste1:
# for gg in range(1000000):
#     a += 1
#     if b == aranan :   
#         b += 1     
#         print (f"sayı {a}.sırada bulundu" )

bolmesayisi = 2
baslangic = 0
bitis = sayiadedi // bolmesayisi 
kackezbakti = 0
for gg in range(bolmesayisi):
    for gg in range(baslangic+2,bitis-2):
        kackezbakti += 1
        a += 1
        if liste1[gg] == aranan :   
            b += 1     
            print (f"sayı {a}.sırada bulundu" )
            break
    baslangic += sayiadedi // bolmesayisi
    bitis += sayiadedi // bolmesayisi
# print(f"{aranan} sayısından {b} adet bulundu.")    
print(f"{aranan} sayısı {kackezbakti}.kerede bulundu.")    
    

