# ekleme sonrası dosya içeriğine bakma
# f = open("dosya1.py", "r")
dosyalar = ["dosya1.py","dosya2.py"]

for a in dosyalar:
    f = open(a, "r", encoding="utf-8")
    print(f.read())

