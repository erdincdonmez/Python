d = open("rehber.txt",encoding="utf-8")
# okunan = d.read()
# okunan = d.readline() # sadece bir satır.
# print(okunan)
# okunan = d.readline() # sadece bir satır.
# print(okunan)
okunan = d.readlines() # kalınan yerden.
# print(okunan)
# print(okunan[3])
# print(okunan[3][4:17])
# print(okunan[3][24:37])
# print(*okunan)
for a in okunan:
    print(a)