araclar1 = ["ferrari","Doğan","bmw"] # en çok kullanılan collection 
araclar2 = ("Şahin","TOGG","Ford") # değiştirilemez 
araclar3 = {"Mazda","Volvo","Mercedes"} # set. indexi yok
araclar4 = {"Kıvanç":"Hundai","Uğurhan":"Mercedes","Ahmet":"Honda"} # index yerine key var

print(type(araclar1))
print(type(araclar2))
print(type(araclar3))
print(type(araclar4))

print(araclar1)
print(araclar2)
print(araclar3)
print(araclar4)

print(araclar1[1])
print(araclar2[1])
# print(araclar3[1])
print(araclar4["Ahmet"])

araclar1 += ["Volvo"]
print(araclar1)

# araclar2 += ("Volvo")
# print(araclar2)

# araclar3 += {"Volvo"}
# print(araclar3)
araclar4 += {"Erdinç":"Volvo"}
print(araclar4)
