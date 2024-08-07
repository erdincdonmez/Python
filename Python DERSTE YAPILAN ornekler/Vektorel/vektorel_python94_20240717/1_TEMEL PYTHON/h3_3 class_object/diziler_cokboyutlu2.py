tren = []
vagon1 = ["Alper","Niyazi","Beyza","Beste"]
vagon2 = ["Ozancan","Yasin","","Ahmet","Onur"]
# tren += vagon1
# tren += vagon2
# tren += vagon1 + vagon2 # her bir dizinin elemanları ana diziye eklenir. çok boyutluda dizi elemanı olmaz.
tren.append(vagon1)
tren.append(vagon2)
print("Trendekiler      : ",tren)
print("1.vagon yolcuları: ",tren[0])

print("2. vagon 2 numarada oturan:",tren[1][1])
print("2. vagon 3 numarada oturan:",tren[1][2] if tren[1][2]!="" else "--")
tren[1][2] = "Erdinç"
print("2. vagon 3 numarada oturan:",tren[1][2] if tren[1][2]!="" else "--")
print("Trendekiler      : ",tren)
print("Vagon 2 yolcuları:",*vagon2, sep="\n")

