meyveler = ["elma","muz","kiraz"]
yeri=-1
aranan = "muz"
for abc in range(len(meyveler)):
    if meyveler[abc] == aranan : yeri=abc
print(aranan,"ifadesinin yeri:",yeri)
