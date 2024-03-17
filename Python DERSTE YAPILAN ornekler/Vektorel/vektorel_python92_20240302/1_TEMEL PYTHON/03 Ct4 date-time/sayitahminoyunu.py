import random
bas = 1
son = 100
hak = 5
puan = 100
tutulan = random.randint(bas,son)
print(tutulan)
print(f"Ben {bas} ile {son} arası bir sayı tuttum.")
print(f"{hak} hakkın var.")

for xx in range(hak):
    tahminEdilen = int(input("tahminin nedir?"))
    if tahminEdilen == tutulan:
        print("Bildin.")
        print("Puanın:",puan)
        break
    elif tahminEdilen > tutulan:
        print("Tahminin büyük.")
        puan -= 100//hak
        print("Puanın:",puan)
    elif tahminEdilen < tutulan:
        print("Tahminin küçük.")
        puan -= 100//hak
        print("Puanın:",puan)

    if xx == hak-1: print("Kaybettin")
