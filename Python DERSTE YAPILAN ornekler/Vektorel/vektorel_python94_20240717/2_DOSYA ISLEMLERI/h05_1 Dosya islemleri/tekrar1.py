import os
# print(*os.listdir(),sep="\n")
dosyadizin_listesi = os.listdir()
print("Çalışma dizini : ",os.getcwd())
for a in dosyadizin_listesi:
    print("Dosya\t" if os.path.isfile(a) == True else "Klasor\t", end="")
    print(a)
