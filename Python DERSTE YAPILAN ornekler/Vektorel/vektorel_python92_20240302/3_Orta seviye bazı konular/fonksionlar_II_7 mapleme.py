# sayilar = [11,22,3]
# # x=lambda a:a*2
# def carp(xx):
#     return xx*2

# yeniDizi = list(map(carp,sayilar))
    
# print(yeniDizi)

sayilar = [11,22,3]
# x=lambda a:a*2
def carp(xx):
    return xx*2

yeniDizi = []
for a in sayilar:
    yeniDizi.append(carp(a))
    
print(yeniDizi)