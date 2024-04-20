sayilar = [11,22,3,6,7]

# yeniDizi = list(filter(lambda x:True,sayilar))
yeniDizi = list(filter(lambda x: x%2==0,sayilar))
    
print(yeniDizi)
