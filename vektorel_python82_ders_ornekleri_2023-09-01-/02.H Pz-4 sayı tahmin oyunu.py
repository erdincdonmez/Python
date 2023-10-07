import random

print("SAYI TAHMİN OYUNU")

tutulan = random.randint(1,100)
print("Ben 1-100 arası bir sayı tuttum 5 kerede bilebilir misin?")
print(tutulan)

for hak in range(5):
    tahmin = int(input("Tahminin nedir?"))
    if tahmin == tutulan:
        print("Bildin")
        break
    elif tahmin>tutulan: print("aşağıda")
    elif tahmin<tutulan: print("yukarıda")
else: print("malesef bilemedin")

# print("Ben 1-100 arası bir sayı tuttum 5 kerede bilebilir misin?")
