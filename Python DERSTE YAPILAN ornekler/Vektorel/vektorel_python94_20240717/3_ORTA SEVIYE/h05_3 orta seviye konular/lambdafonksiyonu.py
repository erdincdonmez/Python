# # Lambda satır içi basit fonksiyon demek
# # ör-1 temel kullanım
# print((lambda x:x**2)(5))

# # ör-2
# karesi = lambda n:n**2
# print (karesi(4))

# ör-3 Uzun şekli
sayilar = [11,22,3]
def karesi(xx): 
    return xx*xx

yeniDizi=[]
for a in sayilar:
    yeniDizi.append(karesi(a))

print(yeniDizi)

# # ör-2 lambda ile kısa şekli
# sayilar = [11,22,3]
# print(list(map(lambda a:a*2,sayilar))) 
