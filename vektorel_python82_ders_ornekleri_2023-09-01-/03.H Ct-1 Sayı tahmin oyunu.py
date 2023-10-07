import random

kotu = ['olmadı','tekrar dene','ha gayret']
iyi = ['süpersin','harikasın','böyle devam']

tutulan=random.randint(1,100)
print("1-100 arası bir sayı tuttum 5(❤❤❤❤❤)  hakkın var")
hak = 5
kullanilan = 0
print (tutulan)

for x in range (hak):
    tahmin=int(input("tahminin ne : "))
    if tahmin== tutulan:
        print("bildin",random.choice(iyi))

        break
    elif tahmin<tutulan:
        kullanilan += 1 
        print(kullanilan)
        print("❤"*(hak-kullanilan),"💔"*kullanilan)
        print(random.choice(kotu))
        print("yukarıda")
    elif tahmin>tutulan: 
        kullanilan += 1
        print(kullanilan)        
        print("❤"*(hak-kullanilan),"💔"*kullanilan)
        print ("aşağıda")


print(':( uzuldum ama 5 hakinda bitti :(')
print('💔💔💔💔💔') 
print('cevap', tutulan)
exit()