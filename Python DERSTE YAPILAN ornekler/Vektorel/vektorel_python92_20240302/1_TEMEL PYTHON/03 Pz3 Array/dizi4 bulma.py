corbalar = ["Tarhana","Mercimek"]
print(corbalar)
# print(corbalar[1])

yemek1 = "Makarna"
yemek2 = "Mantı"
yemek3 = "Döner"
yemekler = [yemek1,yemek2, yemek3]
print(yemekler)
sy = input("Silinecek yemek:")
# yemekler.pop()
for a in range(len(yemekler)):
    print("a değeri:",a)
    print(yemekler[a])
    if yemekler[a] == sy: 
         yemekler.pop(a)
         break

print("\nÇORBALAR:")
for a in corbalar:
    print(a)

print("\nYEMEKLER:")
for a in yemekler:
    print(a)

