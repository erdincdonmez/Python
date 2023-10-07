kelime = "Ankara".lower()
aranan = "a"
bulunanSayisi = 0

for a in range(len(kelime)):
    if kelime[a]==aranan : bulunanSayisi += 1
print (kelime," kelimesinde",aranan," ifadesi",bulunanSayisi," adet var.")