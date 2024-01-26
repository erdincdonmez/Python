import os
import time

os.mkdir("veriler12")

dosya = open("rehber.txt","w")
dosya.write("Deneme1")
dosya.close()
time.sleep(6)
os.remove("veriler12")
