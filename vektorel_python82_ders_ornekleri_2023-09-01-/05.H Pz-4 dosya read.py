# yandaki kod gibi bilgileri satır satır okur, ekrana yazar.
dosya = open("rehber.txt", "r")
satirlar = dosya.readlines()
for satir in satirlar:
  print(satir)
