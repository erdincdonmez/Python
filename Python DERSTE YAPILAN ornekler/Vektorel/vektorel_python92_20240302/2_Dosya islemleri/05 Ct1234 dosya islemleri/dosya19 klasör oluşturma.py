import os
# os.mkdir("bilgiler")
# os.rmdir("bilgiler")
liste = os.listdir()
durum = "yok"
aranan = "dosyalar2"
for a in liste:
    if a == aranan: durum = "var"

print(durum)
if durum == "yok":
    os.mkdir(aranan)

    



