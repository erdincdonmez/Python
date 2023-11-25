"""
sorular = ["Elma","Armut","Kiraz"]
dosya = open("Sorular.txt", "w")
print (len(sorular))
abcr a in range(len(sorular)):
    dosya.write("sorular[a]")
dosya.close

abc = open("rehber.txt", "w")
abc.write("Merhaba Python dosya dünyası.\nİkinci satıra geçtik!!\n")
abc.write("Üçüncü satır çalışmaya devam--")
abc.write("!!!")
abc.close()
############OKUMA
abc = open("rehber.txt", "r+")
str = abc.read(10);
print("1. Okunan : ", str)
str = abc.read(10);
print("2. Okunan : ", str)
str = abc.read();
print("3. Okunan : ", str)
abc.close()
######### pozisyon bilgisi
"""
print("\n\npozisyon bilgisi")
abc = open("dosya.txt", "r+")
str = abc.read(10);
print("1. okunan : ", str)
position = abc.tell(); #pozisyon bilgisi
print("Şu anki pozisyon : ", position)

#tekrar başa konumlan
position = abc.seek(0, 0);
str = abc.read(10);
print("2. okunan : ", str)
abc.close()
"""
######### OTOMATİK KAPAMA
with open("test.txt", "w") as myfile:
    myfile.write("Merhaba with")


"""






"""
https://erdincuzun.com/python/10-2-dosya-islemleri-i-o/
https://python-istihza.yazbel.com/temel_dosya_islemleri.html
"""
