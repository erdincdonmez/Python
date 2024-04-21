sayilar = [11,22,3]

# def carp(xx):
#     return xx+3

# yeniDizi = list(map(carp,sayilar))
yeniDizi = list(map(lambda rr:rr+3,sayilar))
    
print(yeniDizi)
