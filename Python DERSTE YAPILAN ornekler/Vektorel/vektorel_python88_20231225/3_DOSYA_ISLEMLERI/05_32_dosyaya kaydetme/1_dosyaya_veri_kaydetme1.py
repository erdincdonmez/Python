import os
import time

##os.mkdir("veriler")

dosya = open("rehber.txt","a")
ad = input("Kaydedilecek ad ve soyad :")
nu = input("Kaydedilecek numara      :")

veri = ad+" "+nu+"\n"
dosya.write(veri)
dosya.close()
