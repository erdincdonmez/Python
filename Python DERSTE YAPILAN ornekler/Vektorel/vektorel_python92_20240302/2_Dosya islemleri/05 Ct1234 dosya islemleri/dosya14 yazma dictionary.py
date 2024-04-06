# yazarken stringe çevirmek lazım

ad = input("Kaydedilecek kişi adı:      ")
no = input("Kaydedilecek kişi numarası: ")
# ogrenci={
#     "Adi" : ad ,
#     "Numarasi" : no
# }
dosya = open("dosyalar/rehber.txt","a")
# dosya = open("dosyalar/rehber.txt","a")
# dosya.write(f"{str(ogrenci)}\n")
dosya.write(f'{str({"adi":ad,"num":no})},')
dosya.close()


import ast
okunan = open("dosyalar/rehber.txt")
for a in okunan:
    bb = okunan.readline()
    # print(bb)
    # cevirilen = bb
    cevirilen = ast.literal_eval(bb)
    # print(cevirilen)
    print(cevirilen["Adi"])
    # print(cevirilen["Numarasi"])

# for a in cevirilen:
#     print("=> ",a)
#     # print(a[:])
# okunan.close()

