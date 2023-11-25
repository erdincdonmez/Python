a = input("Bir metin girin:")
b = input("Aranan harf    :")

arananS=0
for c in range(len(a)-1):
    if a[c] == b: 
        print("Aradığın var")
        break
