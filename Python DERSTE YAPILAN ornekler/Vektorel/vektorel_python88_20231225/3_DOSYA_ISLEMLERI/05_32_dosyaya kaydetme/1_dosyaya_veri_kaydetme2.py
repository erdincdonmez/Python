import os
import time

##os.mkdir("veriler")

dosya = open("rehber.txt","a")
ad = input("Kaydedilecek ad ve soyad :")
nu = input("Kaydedilecek numara      :")

veri = {"adi":ad,"num":nu}
dosya.write(str(veri))
dosya.close()
