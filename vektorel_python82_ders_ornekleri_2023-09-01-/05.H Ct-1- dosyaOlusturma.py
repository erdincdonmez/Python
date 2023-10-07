import os
import random

#calisilacakYer = "D:\\cc1\\"

print(os.getcwd())

for b in range(5):
    od = "vektorel"+str(b+1)+".txt"
    dosya = open(od,"w")
    os.mkdir("vektorel"+str(b+1))
    dosya.write(str(random.randint(0,100)))
    dosya.close()

input()



print(os.listdir(os.getcwd()))

for a in os.listdir(os.getcwd()):
    print(a)
    if a[:3]=="vek":
        silinecek = a
        #if a=="abc":
        #os.rmdir(silinecek)
        os.remove(silinecek)
