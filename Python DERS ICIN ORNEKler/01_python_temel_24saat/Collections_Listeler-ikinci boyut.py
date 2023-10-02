ist=0
matris=[(2,4,8),(6,8,1),(9,3,5)]
for i,j,k in matris:
    print(i,j,k)

for i,j,k in matris:
    ist+=i
print("İlk sütun toplamı:",ist)

a,b,c=matris[0]
print("İlk satır toplamı:",a+b+c)
