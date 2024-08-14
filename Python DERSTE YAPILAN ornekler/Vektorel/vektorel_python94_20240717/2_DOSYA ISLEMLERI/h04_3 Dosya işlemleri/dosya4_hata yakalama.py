# ekleme sonrası dosya içeriğine bakma
# f = open("dosya1.py", "r")
try:
    f = open("dosya3.py", "r")
    print(f.read())
except:
    print("İşlem başarısız.")