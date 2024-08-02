# ! Random number generator
# ? deneme
# ! Random.
# TODO sdfadfs
import random
tutulan = random.randint(1,100)
print(tutulan)
hak = 5
puan = 100
for i in range(hak):
    tahmin = int(input("Tahminin ne: "))
    if tahmin == tutulan:
        print("bildin")
        print("Puanın: ", puan)
        break
    elif tahmin > tutulan:
        puan -= 10
        print("Sayın büyük, küçült. ")
        print("Puanın: ", puan)
    elif tahmin < tutulan:
        puan -= 10
        print("Sayın küçük, büyüt. ")
        print("Puanın: ", puan)
else:
    print("Hakkın bitti, Kaybettin")

print("Puanın: ", puan)