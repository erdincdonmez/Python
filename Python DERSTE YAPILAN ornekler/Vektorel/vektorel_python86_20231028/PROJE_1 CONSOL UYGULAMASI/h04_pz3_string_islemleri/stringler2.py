# a = "VEktörel Bilişim"
a = input("Bir metin girin:")
# for b in a:
#     print(b)

# print(a[6])
yeniS = ""
for c in range(len(a)-1,-1,-1):
    yeniS += a[c]
print(yeniS)