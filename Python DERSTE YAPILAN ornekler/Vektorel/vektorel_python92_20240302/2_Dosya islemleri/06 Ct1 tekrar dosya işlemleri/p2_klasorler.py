import os
aktifDizin = os.getcwd()
print("Çalışılan dizin: ",aktifDizin)

f = open("deneme2.txt", "w")
f.write("deneme")
f.close()

os.chdir("D:\\kk")

f = open("deneme3.txt", "w")
f.write("deneme")
f.close()