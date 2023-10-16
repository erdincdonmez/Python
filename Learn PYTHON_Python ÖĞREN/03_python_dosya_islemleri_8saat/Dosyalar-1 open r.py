# yandaki kod gibi bilgileri satır satır okur, ekrana yazar.
dosya = open("dosya1.txt", "r")
satirlar = dosya.readlines()
for satir in satirlar:
  print(satir)

