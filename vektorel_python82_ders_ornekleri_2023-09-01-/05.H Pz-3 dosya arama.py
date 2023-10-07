okunan = open("rehber.txt", "r")
liste = []

print("\n\nNormal liste")
print("==============")
for item in okunan:
    liste.append(item)
    print(item)


print("\n\nSıralı liste")
print("==============")
liste.sort()
for a in liste:
    print(a)


print("\n\nSıralı liste parçaları")
print("==============")
aranan = input("Aranan nedir?")
liste.sort()
for a in liste:
    print(a)
    veriler = a.split(" ")
    for x in veriler:
        if aranan == x: print ("var")
        print(x) 
