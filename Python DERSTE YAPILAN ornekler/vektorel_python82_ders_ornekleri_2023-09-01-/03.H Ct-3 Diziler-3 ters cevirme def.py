def tersCevir(cevirilecek):
    yeniString = ""
    for a in range(len(cevirilecek)-1,-1,-1):
        yeniString += cevirilecek[a]
    return yeniString

kurumAdi = input("Bir şey gir: ")
print(tersCevir(kurumAdi))
