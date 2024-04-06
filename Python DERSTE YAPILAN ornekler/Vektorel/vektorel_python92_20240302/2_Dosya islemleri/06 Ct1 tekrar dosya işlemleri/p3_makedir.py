import os
aktifDizin = os.getcwd()
print("Çalışılan dizin: ",aktifDizin)

# REHBER = "ABC"
os.chdir("D:\\")
os.mkdir("REHBER")

f = open("D:\\REHBER\deneme2.txt", "w")
f.write("vektorel")
f.close()

