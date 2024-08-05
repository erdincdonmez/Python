# while True:
#     print("merhaba")

# a = True
# while a: print("Selam")

# a = 1
# while a<10:
#     print(a)
#     a +=2

meyveler = []
meyve = " "
while meyve!="":
    meyve = input("Meyve giriniz:")
    if meyve !="": meyveler.append(meyve)
else:
    print("\n","="*33)
print("Girdiğiniz meyveler:", *meyveler, sep="\n")

