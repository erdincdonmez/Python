a = input("Bir metin girin:")
b = input("Aranan harf    :")

arananS=0
for c in range(len(a)):
    if a[c] == b: arananS+=1

print(arananS)