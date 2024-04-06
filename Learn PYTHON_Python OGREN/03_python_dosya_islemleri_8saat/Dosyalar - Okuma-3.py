f = open("deneme.txt") # mod yazılı değilse r kabul eder.
print("Tüm dosya içeriği: ",f.read())
f.seek(0)
for a in range(len(f.read())):
    f.seek(a)
    print(f.read(2))
