sozluk = {
    "fil" :"elephant",
    "kedi" :"cat",
    "köpek" :"dog",
}

araba = {
    "markasi" :"toyota",
    "fiyatı" :400000,
}

# print(araba["markasi"])


arabalar = {
    "ereninarabasi" : {"marka":"toyota","fiyatı":400000},
    "kadirinarabasi" : {"marka":"opel","fiyatı":500000},
    "kivancinarabasi" : {"marka":"mercedes","fiyatı":600000}
}

print ("araba elemanı  : ",arabalar["ereninarabasi"])
print ("Elemanın değeri: ",arabalar["ereninarabasi"]["marka"])

# for zz in sozluk:
#     print("İndex yerine ",zz,", değeri: " ,sozluk[zz])
