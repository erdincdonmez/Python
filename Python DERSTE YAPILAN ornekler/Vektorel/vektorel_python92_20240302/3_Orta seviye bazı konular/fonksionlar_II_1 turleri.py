# Normal (basit) fonksiyonlar. Değer almaz, değer döndürmez.
# def selamla(): # düz fonksiyon
#     print("Merhaba")
#     print("Nasılsın")

# selamla()

# Değer alan fonksiyonlar
# def ekranaYaz(xxx="Değer gönderilmedi"): # Değer alan fonksiyon
# def ekranaYaz(xxx="\n"): # Değer alan fonksiyon
#     print(xxx)

# ekranaYaz()
# ekranaYaz()
# # print()
# # print()
# ekranaYaz("Napıyon?")

# # Değer döndüren fonksiyonlar
def topla(aaa, bbb): # Değer döndüren fonksiyon
    return aaa+bbb

print(topla(topla(topla(9,6),5),topla(3,5)))