# 45,5 + (2,3 / 2,54) x (boy(cm) - 152,4)
# 50 + (2,3 / 2,54) x (boy(cm) - 152,4)

print("    İDEAL KİLO HESAPLAYICI")
ad = input("Adın nedir? ")
boy = int(input(f"{ad} boyun kaç (cm olarak)? "))
ikk = 45.5 + (2.3/2.54) * boy - 152.4
ike = 50 + (2.3/2.54) * boy - 152.4
print(f"{boy}cm boy için ideal erkek kilosu",ike ,"kilodur.")
print(f"{boy}cm boy için ideal kadın kilosu",ikk ,"kilodur.")

