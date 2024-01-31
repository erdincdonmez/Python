import os 
# print(os.listdir())
print("Şuan :",os.getcwd())
pySayisi = 0
deSayisi = 0
for a in os.listdir():
    if os.path.isfile(a): print("dosya","\t\t",end="")
    if os.path.isdir(a): print("<DIR>","\t\t",end="")
    print(os.stat(a).st_size,"\t\t",end="")
    if a.endswith(".py"): pySayisi += 1
    if a.startswith("de"): deSayisi += 1
    print(a,"\t\t\t")

print("Python dosyası sayısı : ",pySayisi)
print("de ile başlayan sayısı: ",deSayisi)

input()