
f = open("PythonRehber.txt", "r")
for x in f:
    a, s, n = x.split()
    print("Adı: ",a,"Soyadı: ",s,"Numarası: ",n)

"""
# Yukarıdaki kodlar ile aynı işi yapar.
f = open("PythonRehber.txt", "r")
satirlar = f.readlines()
for satir in satirlar:
    ad, soyad, numara = satir.split()
    print("Adı: ",ad,"Soyadı: ",soyad,"Numarası: ",numara)

"""
