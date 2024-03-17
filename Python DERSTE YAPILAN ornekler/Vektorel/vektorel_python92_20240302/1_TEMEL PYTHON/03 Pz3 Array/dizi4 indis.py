corbalar = ["Tarhana","Mercimek"]
print(corbalar)
# print(corbalar[1])

yemek1 = "Makarna"
yemek2 = "Mantı"
yemek3 = "Döner"
yemekler = [yemek1,yemek2, yemek3,"İskender","Dolma"]
print(yemekler)
print("Aradan alma : ",yemekler[1:3])
print("Aradan alma : ",yemekler[:3])
print("Aradan alma : ",yemekler[3:])
print("Aradan alma : ",yemekler[:])

print("\nÇORBALAR:")
for a in corbalar:
    print(a)

print("\nYEMEKLER:")
for a in yemekler:
    print(a)

