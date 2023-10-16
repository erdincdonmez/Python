import os
"""
print(os.listdir())
yer = os.getcwd()
print(os.getcwd())
yer += "/deneme"
os.chdir(yer)
print(os.getcwd())
"""
dosyalar = os.listdir()
for dosya in dosyalar:
     if dosya.endswith(".py"):
             print(dosya)
#os.mkdir("aa")
os.rmdir("aa")
