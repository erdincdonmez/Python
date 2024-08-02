corbalar = []
print(corbalar)
corbalar = ["Tarhana"]
print(corbalar)
corbalar = ["Şehriye","Mercimek"]
print(corbalar)
corbalar += ["Domates","Ezogelin","Paça"]
print(corbalar)

print(type(corbalar))

yemekler = ("köfte","tavuk haşlama")
print(yemekler)
# yemekler += ("mantı")
print(yemekler)
print(type(yemekler))

print(corbalar[1])
# print(*corbalar,sep="\n")
print(corbalar[1:4])
print(corbalar[:])
print(corbalar[::2])
print(corbalar.index("Domates"))

# corbalar.append("İşkembe")
corbalar.insert(1,"Yoğurt")
print(corbalar)