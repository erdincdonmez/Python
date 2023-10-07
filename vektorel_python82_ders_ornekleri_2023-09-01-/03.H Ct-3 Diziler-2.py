kurumAdi = input("Bir şey gir: ")
print(kurumAdi)
yeniString = ""
for a in range(len(kurumAdi)-1,-1,-1):
    yeniString += kurumAdi[a]
print(yeniString)
#print(kurumAdi[0])