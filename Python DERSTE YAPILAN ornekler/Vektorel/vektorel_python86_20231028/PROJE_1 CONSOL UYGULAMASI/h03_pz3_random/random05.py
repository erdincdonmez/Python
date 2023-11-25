import random
print("Zorluk seviyesi ne olsun?")
print("1:kolay, 2:orta, 3:zor")
zorluk = int(input("Seçiniz: "))
if zorluk == 1 : 
    max=10
    hak = 5
if zorluk == 2 : 
    max=100
    hak = 6
if zorluk == 3 : 
    max=1000
    hak = 7
tutulan = random.randint(1,max)
print("Tutulan sayı:",tutulan)
print("Ben 1 ile",max,"arasında bir sayı tuttum.")
puan = 100
for a in range(hak,0,-1):
    tahmin = int(input("Tahminin nedir?"))
    if tahmin > tutulan :
        print("Tahminin tutulandan büyük")
        puan -= 100 // hak
        print(a,"hakkın kaldı. Kalan puanın:",puan)
        
    if tahmin < tutulan :
        print("Tahminin tutulandan küçük")
        puan -= 100 // hak
        print(a,"hakkın kaldı. Kalan puanın:",puan)
    if tahmin == tutulan:
        print("Bildin")
        print(puan,"puanı ile bitirdin.")


