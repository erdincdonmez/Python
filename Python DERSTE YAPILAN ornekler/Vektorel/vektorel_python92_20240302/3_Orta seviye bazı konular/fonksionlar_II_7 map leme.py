# sayilar = [5,22,3]
# # x=lambda a:a*2
# def carp(xx):
#     return xx*2

# def tekCift(xx):
#     if xx % 2 == 0: sonuc = 'çift'
#     else: sonuc = 'tek'
#     return f'{xx} {sonuc}'

# yeniDizi = list(map(tekCift,sayilar))
    
# print(yeniDizi)

sayilar = [11,22,3]
# x=lambda a:a*2
def carp(xx):
    return xx*2

yeniDizi = []
for a in sayilar:
    yeniDizi.append(carp(a))
    
print(yeniDizi)