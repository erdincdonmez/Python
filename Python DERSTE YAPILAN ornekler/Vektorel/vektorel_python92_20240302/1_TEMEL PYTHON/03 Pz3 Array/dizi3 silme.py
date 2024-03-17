corbalar = ["Tarhana","Mercimek"]
print(corbalar)
# print(corbalar[1])

yemek1 = "Makarna"
yemek2 = "Mantı"
yemek3 = "Döner"
yemekler = [yemek1,yemek2, yemek3]
print(yemekler)
# ey = input("Silinecek yemek indisi")
yemekler.pop()
yemekler.pop(1)

print("\nÇORBALAR:")
for a in corbalar:
    print(a)

print("\nYEMEKLER:")
for a in yemekler:
    print(a)
    
