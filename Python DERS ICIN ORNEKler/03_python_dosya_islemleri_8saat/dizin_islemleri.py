# klasör konumunu değiştirme
import os
yer = os.getcwd()
print("KONUM: ", yer)
for a in os.listdir(): print(a)
yer += "/deneme"
os.chdir(yer)
print(os.getcwd())
print("KONUM: ", yer)
for b in os.listdir(): print(b)
