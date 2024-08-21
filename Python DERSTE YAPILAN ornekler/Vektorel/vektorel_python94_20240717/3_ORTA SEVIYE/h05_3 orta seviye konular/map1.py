# sayilar = [11,22,3]
# def carp(xx):
#     return xx*2

# yeniDizi = list(map(carp,sayilar))   
# print(yeniDizi)

# ürünFiyatlari = [100,200,30]
# def yariyaIndir(xx):
#     return xx//2

# yeniDizi = list(map(yariyaIndir,ürünFiyatlari))   
# print(yeniDizi)

ürünFiyatlari = [100,200,30]
def yariyaIndir(xx):
    return xx//2

# yeniDizi = list(map(yariyaIndir,ürünFiyatlari))   
yeniDizi=[]
for a in range(len(ürünFiyatlari)):
    yeniDizi.append(yariyaIndir(ürünFiyatlari[a]))
print(yeniDizi)